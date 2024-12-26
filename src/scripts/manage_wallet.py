import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from getpass import getpass
import base64

# Fonction pour afficher les erreurs dans l'interface graphique
def show_error(message):
    messagebox.showerror("Erreur", message)

# Fonction pour générer une clé Bitcoin (la logique est à ajuster selon vos besoins)
def generate_key():
    try:
        # Remplacer par la logique pour générer la clé Bitcoin
        messagebox.showinfo("Succès", "Clé Bitcoin générée avec succès!")
    except Exception as e:
        show_error(str(e))

# Fonction pour lire la clé privée depuis un fichier
def read_key():
    try:
        with open("/home/hello/Cold_Wallet/keys/private/private_key.txt", "r") as file:
            private_key = file.read().strip()
            messagebox.showinfo("Clé Privée", f"Clé privée lue : {private_key}")
    except Exception as e:
        show_error(str(e))

# Fonction pour chiffrer la clé privée
def encrypt_key():
    try:
        password = input("Entrez une phrase secrète pour la clé de chiffrement : ").encode()

        # Générer la clé de chiffrement à partir de la phrase secrète (scrypt est plus sécurisé)
        encryption_key = scrypt(password, salt=b'some_salt_value', key_len=32, N=16384, r=8, p=1)

        # Chiffrer la clé privée
        private_key = "votre_clé_privée"  # Utilisez la clé privée générée ou lue
        cipher = AES.new(encryption_key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(private_key.encode())

        # Sauvegarder la clé chiffrée dans un fichier
        with open("/home/hello/Cold_Wallet/keys/private/private_key.enc", "wb") as file_out:
            for x in (cipher.nonce, tag, ciphertext):
                file_out.write(x)

        messagebox.showinfo("Succès", "Clé privée chiffrée et sauvegardée.")
    except Exception as e:
        show_error(f"Erreur lors du chiffrement : {str(e)}")

# Fonction pour déchiffrer la clé privée
def decrypt_key():
    try:
        # Lire la clé chiffrée depuis le fichier 'private_key.enc' dans le dossier 'keys/private'
        with open("/home/hello/Cold_Wallet/keys/private/private_key.enc", "rb") as file_in:
            # Charger le nonce, le tag et le ciphertext du fichier
            nonce = file_in.read(16)
            tag = file_in.read(16)
            ciphertext = file_in.read()

            # Afficher pour déboguer
            print(f"Nonce: {nonce.hex()}")
            print(f"Tag: {tag.hex()}")
            print(f"Ciphertext: {ciphertext.hex()}")

        # Demander la clé de chiffrement à l'utilisateur via une boîte de dialogue sécurisée
        encryption_key = getpass("Entrez la clé de chiffrement : ").encode()

        # Générer la clé de chiffrement à partir de la phrase secrète (comme lors du chiffrement)
        encryption_key = scrypt(encryption_key, salt=b'some_salt_value', key_len=32, N=16384, r=8, p=1)

        # Initialiser le cipher pour déchiffrer
        cipher = AES.new(encryption_key, AES.MODE_EAX, nonce=nonce)

        # Déchiffrer la clé privée
        private_key = cipher.decrypt_and_verify(ciphertext, tag)

        # Affichage du résultat
        print(f"Clé privée déchiffrée : {private_key.decode()}")
        messagebox.showinfo("Clé Privée Déchiffrée", f"Clé privée déchiffrée : {private_key.decode()}")

    except Exception as e:
        show_error(f"Erreur lors du déchiffrement : {str(e)}")
# Fonction pour créer une transaction (juste un placeholder pour l'exemple)
def create_tx():
    try:
        # Logic pour créer une transaction (à ajuster selon votre code)
        messagebox.showinfo("Transaction", "Transaction créée avec succès!")
    except Exception as e:
        show_error(str(e))

# Fonction pour signer une transaction (juste un placeholder pour l'exemple)
def sign_tx():
    try:
        # Logic pour signer une transaction (à ajuster selon votre code)
        messagebox.showinfo("Signature", "Transaction signée avec succès!")
    except Exception as e:
        show_error(str(e))

# Création de la fenêtre principale de Tkinter
root = tk.Tk()
root.title("Cold Wallet - Interface de gestion")

# Ajouter un cadre pour un design plus propre
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Titre de l'application
title_label = tk.Label(frame, text="Interface de gestion du Cold Wallet", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Ajouter des boutons pour chaque fonctionnalité
btn_generate = tk.Button(frame, text="Générer une clé Bitcoin", width=30, command=generate_key)
btn_generate.grid(row=1, column=0, pady=5)

btn_read = tk.Button(frame, text="Lire la clé privée", width=30, command=read_key)
btn_read.grid(row=2, column=0, pady=5)

btn_encrypt = tk.Button(frame, text="Chiffrer la clé privée", width=30, command=encrypt_key)
btn_encrypt.grid(row=3, column=0, pady=5)

btn_decrypt = tk.Button(frame, text="Déchiffrer la clé privée", width=30, command=decrypt_key)
btn_decrypt.grid(row=4, column=0, pady=5)

btn_create_tx = tk.Button(frame, text="Créer une transaction", width=30, command=create_tx)
btn_create_tx.grid(row=5, column=0, pady=5)

btn_sign_tx = tk.Button(frame, text="Signer une transaction", width=30, command=sign_tx)
btn_sign_tx.grid(row=6, column=0, pady=5)

# Ajouter un bouton de sortie
btn_exit = tk.Button(frame, text="Quitter", width=30, command=root.quit)
btn_exit.grid(row=7, column=0, pady=10)

# Lancer la boucle principale de Tkinter
root.mainloop()
