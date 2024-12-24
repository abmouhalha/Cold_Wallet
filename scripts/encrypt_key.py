from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from Crypto.Protocol.KDF import scrypt

def encrypt_private_key(private_key):
    # Demander à l'utilisateur une phrase secrète
    password = input("Entrez une phrase secrète pour la clé de chiffrement : ").encode()

    # Générer la clé de chiffrement à partir de la phrase secrète (scrypt est plus sécurisé que get_random_bytes)
    encryption_key = scrypt(password, salt=b'some_salt_value', key_len=32)

    # Initialiser le cipher (mode EAX pour l'authentification)
    cipher = AES.new(encryption_key, AES.MODE_EAX)

    # Chiffrer la clé privée
    ciphertext, tag = cipher.encrypt_and_digest(private_key.encode())

    # Sauvegarder la clé chiffrée dans un fichier
    with open("/home/hello/Cold_Wallet/keys/private/private_key.enc", "wb") as file_out:
        for x in (cipher.nonce, tag, ciphertext):
            file_out.write(x)

    print("Clé privée chiffrée sauvegardée dans '/home/hello/Cold_Wallet/keys/private/private_key.enc'.")
