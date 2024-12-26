import os
import hashlib
import tkinter as tk
from tkinter import messagebox
from getpass import getpass

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
        with open("keys/private/private_key.txt", "r") as file:
            private_key = file.read().strip()
            messagebox.showinfo("Clé Privée", f"Clé privée lue : {private_key}")
    except Exception as e:
        show_error(str(e))

# Fonction pour chiffrer la clé privée
def encrypt_key():
    try:
        password = getpass("Entrez une phrase secrète pour la clé de chiffrement : ")

        # Dériver la clé de chiffrement sans dépendances supplémentaires
        salt = b'some_salt_value'
        encryption_key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)

        # Chiffrer la clé privée
        private_key = "votre_clé_privée"  # Utilisez la clé privée générée ou lue
        cipher = hashlib.sha256(private_key.encode() + encryption_key).hexdigest()

        # Sauvegarder la clé chiffrée dans un fichier
        with open("keys/private/private_key.enc", "w") as file_out:
            file_out.write(cipher)

        messagebox.showinfo("Succès", "Clé privée chiffrée et sauvegardée.")
    except Exception as e:
        show_error(f"Erreur lors du chiffrement : {str(e)}")

# Fonction pour déchiffrer la clé privée
def decrypt_key():
    try:
        # Lire la clé chiffrée depuis le fichier 'private_key.enc'
        with open("keys/private/private_key.enc", "r") as file_in:
            cipher = file_in.read().strip()

        # Demander la clé de chiffrement à l'utilisateur
        password = getpass("Entrez la clé de chiffrement : ")

        # Générer la clé de déchiffrement à partir de la phrase secrète
        salt = b'some_salt_value'
        encryption_key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)

        # Déchiffrer la clé privée
        private_key_decrypted = hashlib.sha256(cipher.encode() + encryption_key).hexdigest()

        messagebox.showinfo("Clé Privée Déchiffrée", f"Clé privée déchiffrée : {private_key_decrypted}")

    except Exception as e:
        show_error(f"Erreur lors du déchiffrement : {str(e)}")

# Fonction pour créer une transaction (juste un placeholder pour l'exemple)
def create_tx():
    try:
        messagebox.showinfo("Transaction", "Transaction créée avec succès!")
    except Exception as e:
        show_error(str(e))

# Fonction pour signer une transaction (juste un placeholder pour l'exemple)
def sign_tx():
    try:
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
