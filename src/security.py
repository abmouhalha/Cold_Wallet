from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64

""" Fonction pour dériver une clé à partir d'un mot de passe"""
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Longueur de la clé de chiffrement (256 bits)
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

""" Fonction pour chiffrer une clé privée"""
def encrypt_private_key(private_key: bytes, password: str) -> str:
    """Chiffrer une clé privée en utilisant AES avec un mot de passe."""
    salt = os.urandom(16)  # Générer un sel aléatoire
    iv = os.urandom(16)  # Générer un vecteur d'initialisation (IV)
    
    # Utilisation de PBKDF2 pour dériver une clé à partir du mot de passe et du sel
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = kdf.derive(password.encode())

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Appliquer le padding PKCS7
    padding_length = 16 - len(private_key) % 16
    private_key_padded = private_key + bytes([padding_length] * padding_length)

    ciphertext = encryptor.update(private_key_padded) + encryptor.finalize()
    
    # Retourner le chiffrement sous forme base64 (salt + iv + ciphertext)
    return base64.b64encode(salt + iv + ciphertext).decode()

def decrypt_private_key(encrypted_private_key: str, password: str) -> str:
    """
    Fonction pour déchiffrer la clé privée.
    
    :param encrypted_private_key: La clé privée chiffrée en base64
    :param password: Le mot de passe pour déchiffrer la clé privée
    :return: La clé privée déchiffrée
    """
    # Décoder les données chiffrées
    encrypted_data = base64.b64decode(encrypted_private_key)
    
    # Extraire le sel, l'IV et le texte chiffré
    salt = encrypted_data[:16]  # 16 premiers octets pour le sel
    iv = encrypted_data[16:32]  # 16 suivants pour l'IV
    ciphertext = encrypted_data[32:]  # Reste pour le texte chiffré
    
    # Générer la clé de décryptage à partir du mot de passe et du sel
    key = derive_key(password, salt)
    
    # Initialiser le décryptage avec AES en mode CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Déchiffrer la clé privée
    decrypted_padded_private_key = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Retirer le padding PKCS7
    padding_length = decrypted_padded_private_key[-1]
    decrypted_private_key = decrypted_padded_private_key[:-padding_length]  # Supprimer le padding
    
    # Essayer de décoder en UTF-8
    try:
        return decrypted_private_key.decode('utf-8')  # Retourner la clé privée déchiffrée en UTF-8
    except UnicodeDecodeError:
        # Si l'erreur survient, on retourne les données binaires sous forme hexadécimale
        return decrypted_private_key.hex()