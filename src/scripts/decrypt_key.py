from Crypto.Cipher import AES
import base64
from getpass import getpass  # Utilisé pour une entrée sécurisée de la clé de chiffrement

def decrypt_private_key():
    try:
        # Lire la clé chiffrée depuis le fichier 'private_key.enc' dans le dossier 'keys/private'
        with open("/home/hello/Cold_Wallet/keys/private/private_key.enc", "rb") as file_in:
            # Charger le nonce, le tag et le ciphertext du fichier
            nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

        # Demander à l'utilisateur la clé de chiffrement (à sécuriser dans un vrai cas)
        encryption_key = getpass("Entrez la clé de chiffrement : ").encode()  # Saisie sécurisée

        # Initialiser le cipher pour déchiffrer
        cipher = AES.new(encryption_key, AES.MODE_EAX, nonce=nonce)

        # Déchiffrer la clé privée
        private_key = cipher.decrypt_and_verify(ciphertext, tag)

        print("Clé privée déchiffrée : ", private_key.decode())
        return private_key.decode()

    except FileNotFoundError:
        print("Le fichier 'private_key.enc' n'a pas été trouvé.")
        return None
    except ValueError:
        print("Échec du déchiffrement, vérifiez la clé de chiffrement.")
        return None

if __name__ == "__main__":
    decrypt_private_key()
