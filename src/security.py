from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64

# Fonction pour dériver une clé à partir d'un mot de passe
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Longueur de la clé de chiffrement (256 bits)
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Fonction pour chiffrer une clé privée
def encrypt_private_key(private_key: str, password: str) -> str:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padding_length = 16 - len(private_key) % 16
    private_key_padded = private_key + chr(padding_length) * padding_length
    
    ciphertext = encryptor.update(private_key_padded.encode()) + encryptor.finalize()
    
    return base64.b64encode(salt + iv + ciphertext).decode()

# Fonction pour déchiffrer la clé privée
def decrypt_private_key(encrypted_private_key: str, password: str) -> str:
    encrypted_data = base64.b64decode(encrypted_private_key)
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded_private_key = decryptor.update(ciphertext) + decryptor.finalize()
    
    padding_length = ord(decrypted_padded_private_key[-1:])
    return decrypted_padded_private_key[:-padding_length].decode()
