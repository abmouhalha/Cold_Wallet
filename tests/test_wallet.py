import os
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

# Fonction pour générer une clé privée aléatoire
def generate_private_key():
    return os.urandom(32)  # 32 octets pour une clé privée de 256 bits

# Fonction pour chiffrer la clé privée
def encrypt_private_key(private_key, password):
    # Générer un sel (salt) aléatoire de 16 octets
    salt = get_random_bytes(16)
    
    # Générer une clé de chiffrement avec scrypt, à partir du mot de passe et du sel
    key = scrypt(password.encode(), salt, key_len=32, N=2**14, r=8, p=1)
    
    # Générer un nonce (nombre aléatoire) pour AES-GCM
    nonce = get_random_bytes(16)
    
    # Initialiser le chiffreur AES en mode GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    # Chiffrer la clé privée
    ciphertext, tag = cipher.encrypt_and_digest(private_key)
    
    # Retourner le sel, le nonce, le ciphertext et le tag encodés en Base64
    encrypted_data = salt + nonce + ciphertext + tag
    return base64.b64encode(encrypted_data).decode()

# Fonction pour déchiffrer la clé privée
def decrypt_private_key(encrypted_data_base64, password):
    # Décoder les données Base64
    encrypted_data = base64.b64decode(encrypted_data_base64)
    
    # Extraire le sel, le nonce, le ciphertext et le tag
    salt = encrypted_data[:16]
    nonce = encrypted_data[16:32]
    ciphertext = encrypted_data[32:-16]
    tag = encrypted_data[-16:]
    
    # Générer la clé de chiffrement avec scrypt
    key = scrypt(password.encode(), salt, key_len=32, N=2**14, r=8, p=1)
    
    # Initialiser le déchiffreur AES en mode GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    # Déchiffrer la clé privée
    private_key = cipher.decrypt_and_verify(ciphertext, tag)
    
    return private_key

# Exemple de test
if __name__ == "__main__":
    # 1. Générer une clé privée aléatoire
    private_key = generate_private_key()
    print(f"Clé privée générée (hex) : {private_key.hex()}")
    
    # 2. Chiffrer la clé privée avec un mot de passe
    password = "mon_mot_de_passe_securise"  # Mot de passe de chiffrement
    encrypted_data = encrypt_private_key(private_key, password)
    print(f"Clé privée chiffrée (Base64) : {encrypted_data}")
    
    # 3. Déchiffrer la clé privée
    decrypted_private_key = decrypt_private_key(encrypted_data, password)
    print(f"Clé privée déchiffrée (hex) : {decrypted_private_key.hex()}")
    
    # Vérifier si la clé privée déchiffrée est la même que l'originale
    assert private_key == decrypted_private_key, "La clé privée déchiffrée ne correspond pas à la clé privée originale"
    print("Le déchiffrement a réussi et la clé est correcte.")
