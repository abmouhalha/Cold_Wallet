import os
import hashlib

# Paramètres de la courbe elliptique secp256k1 pour Bitcoin
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0
B = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
G = (Gx, Gy)
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

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

def generate_private_key():
    """Générer une clé privée de 256 bits (32 octets)."""
    return os.urandom(32)

def private_key_to_public_key(private_key):
    """Générer une clé publique à partir de la clé privée."""
    int_private_key = int.from_bytes(private_key, 'big')
    public_key = scalar_multiplication(int_private_key, G)
    return public_key

def public_key_to_address(public_key):
    """Convertir une clé publique en adresse Bitcoin."""
    public_key_bytes = public_key_to_bytes(public_key)  # Appel à la fonction définie ci-dessous
    sha256 = hashlib.sha256(public_key_bytes).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()

    # Préfixe réseau pour les adresses Bitcoin (0x00 pour le réseau principal)
    prefixed_key = b'\x00' + ripemd160

    # Calcul du checksum (4 premiers octets du double SHA-256)
    checksum = hashlib.sha256(hashlib.sha256(prefixed_key).digest()).digest()[:4]

    # Ajouter le checksum et encoder en Base58
    final_key = prefixed_key + checksum
    return base58_encode(final_key)

def public_key_to_bytes(public_key):
    """Convertir une clé publique (tuple) en bytes pour le hashing."""
    x, y = public_key
    x_bytes = x.to_bytes(32, byteorder='big')
    y_bytes = y.to_bytes(32, byteorder='big')
    return b'\x04' + x_bytes + y_bytes  # Format non compressé

def base58_encode(data):
    """Encodage Base58."""
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    encoded = ''
    num = int.from_bytes(data, 'big')
    while num > 0:
        num, rem = divmod(num, 58)
        encoded = alphabet[rem] + encoded

    # Ajouter des préfixes '1' pour les zéros initiaux
    for byte in data:
        if byte == 0:
            encoded = '1' + encoded
        else:
            break

    return encoded
