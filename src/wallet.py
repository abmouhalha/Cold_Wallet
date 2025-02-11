#https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch04_keys.adoc

import os
import hashlib
from security import encrypt_private_key, decrypt_private_key  # Assurez-vous que ces fonctions existent dans security.py

# Paramètres de la courbe elliptique secp256k1 pour Bitcoin
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0
B = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
G = (Gx, Gy)
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

def generate_private_key():
    """Générer une clé privée de 256 bits (32 octets), inférieure à n."""
    while True:
        private_key = os.urandom(32)  # Générer une clé privée de 256 bits
        """1. Entropie théorique

    32 octets correspondent à 256 bits.

    Si les données sont parfaitement aléatoires, l'entropie est de 256 bits 
    (car chaque bit peut être 0 ou 1 avec une probabilité égale et indépendante
      des autres bits).
        Événements matériels : mouvements de souris, frappes au clavier, délais entre les interruptions matérielles, etc.

    Données environnementales : température du processeur, bruit du disque dur, etc.

    Générateurs de nombres aléatoires matériels (HRNG) : certains processeurs modernes (comme ceux d'Intel ou AMD) incluent 
    des circuits dédiés pour générer de l'entropie (par exemple, l'instruction RDRAND).

    Sur les systèmes Unix (Linux, macOS, etc.), os.urandom utilise généralement /dev/urandom, qui est alimenté par un 
    pool d'entropie géré par le noyau. Sur Windows, il utilise des API cryptographiques comme BCryptGenRandom
    
    hello@hello-HP-EliteBook-x360-1030-G2:~$ cat /proc/sys/kernel/random/entropy_avail
    256
"""
        private_key_int = int.from_bytes(private_key, byteorder="big") #permet de convertir une séquence d'octets (un bytearray) en un entier (int)
        if 0 < private_key_int < N:  # Vérifier si elle est valide
            return private_key
            
# Addition de points sur la courbe elliptique secp256k1
def point_addition(P1, P2):
    """Addition de points sur la courbe elliptique secp256k1."""
    if P1 == (0, 0):
        return P2
    if P2 == (0, 0):
        return P1

    x1, y1 = P1
    x2, y2 = P2

    if x1 == x2 and y1 != y2:
        return (0, 0)

    if x1 == x2:
        # Doublage de point
        m = (3 * x1 * x1 + A) * pow(2 * y1, -1, P) % P
    else:
        # Addition de points différents
        m = (y2 - y1) * pow(x2 - x1, -1, P) % P

    x3 = (m * m - x1 - x2) % P
    y3 = (m * (x1 - x3) - y1) % P

    return (x3, y3)

# Multiplication scalaire sur la courbe elliptique
def scalar_multiplication(k, point):
    """Multiplication scalaire sur une courbe elliptique."""
    result = (0, 0)
    addend = point

    while k:
        if k & 1:
            result = point_addition(result, addend)
        addend = point_addition(addend, addend)
        k >>= 1

    return result



# Fonction pour convertir la clé privée en clé publique
def private_key_to_public_key(private_key):
    """Générer une clé publique à partir de la clé privée."""
    int_private_key = int.from_bytes(private_key, 'big') #permet de convertir une séquence d'octets (un bytearray) en un entier (int)
    public_key = scalar_multiplication(int_private_key, G)
    return public_key

# Fonction pour convertir une clé publique (tuple) en bytes pour le hashing
def public_key_to_bytes(public_key):
    """Convertir une clé publique (tuple) en bytes pour le hashing."""
    x, y = public_key
    x_bytes = x.to_bytes(32, byteorder='big')
    y_bytes = y.to_bytes(32, byteorder='big')
    return b'\x04' + x_bytes + y_bytes  # Format non compressé

# Fonction pour convertir la clé publique en adresse Bitcoin
def public_key_to_address(public_key):
    """Convertir une clé publique en adresse Bitcoin."""
    public_key_bytes = public_key_to_bytes(public_key)  # Conversion de la clé publique en bytes
    sha256 = hashlib.sha256(public_key_bytes).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()

    prefixed_key = b'\x00' + ripemd160
    checksum = hashlib.sha256(hashlib.sha256(prefixed_key).digest()).digest()[:4]
    final_key = prefixed_key + checksum
    return base58_encode(final_key)

# Fonction pour encoder en base58
def base58_encode(data):
    """Encodage Base58."""
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    num = int.from_bytes(data, 'big')
    encoded = ''
    while num > 0:
        num, rem = divmod(num, 58)
        encoded = alphabet[rem] + encoded

    for byte in data:
        if byte == 0:
            encoded = '1' + encoded
        else:
            break
    return encoded

""" Fonction pour sauvegarder la clé privée chiffrée"""
def save_encrypted_private_key(private_key, password):
    """Sauvegarder la clé privée chiffrée."""
    encrypted_key = encrypt_private_key(private_key, password)
    with open("keys/private/private_key.enc", "w") as file:
        file.write(encrypted_key)

""" Fonction pour charger et déchiffrer la clé privée"""
def load_and_decrypt_private_key(password):
    with open("keys/private/private_key.enc", "r") as file:
        encrypted_key = file.read()
    return decrypt_private_key(encrypted_key, password)
