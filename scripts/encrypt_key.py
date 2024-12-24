# encrypt_key.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_private_key(private_key):
    # Générer une clé de chiffrement AES (256 bits)
    encryption_key = get_random_bytes(32)

    # Initialiser le cipher (mode EAX pour l'authentification)
    cipher = AES.new(encryption_key, AES.MODE_EAX)

    # Chiffrer la clé privée
    ciphertext, tag = cipher.encrypt_and_digest(private_key.encode())

    # Sauvegarder la clé chiffrée dans un fichier
    with open("Cold_Wallet/keys/private_key.enc", "wb") as file_out:
        for x in (cipher.nonce, tag, ciphertext):
            file_out.write(x)

    print("Clé privée chiffrée sauvegardée dans 'Cold_Wallet/keys/private_key.enc'.")

if __name__ == "__main__":
    # Exemple de clé privée à chiffrer
    private_key = "L4Rit3UNarEFnjkpc2VM1LzjTYrdPFgpDd6vJvNsxHWa8jbskDkF"
    encrypt_private_key(private_key)
