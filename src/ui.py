import os
import tkinter as tk
from tkinter import messagebox
from getpass import getpass
from wallet import generate_private_key, private_key_to_public_key, public_key_to_address, save_encrypted_private_key, load_and_decrypt_private_key
from utils import create_directory_if_not_exists
from wallet import public_key_to_bytes

def show_error(message):
    messagebox.showerror("Erreur", message)

def generate_key():
    try:
        create_directory_if_not_exists('keys/private')
        create_directory_if_not_exists('keys/public')

        # Générer la clé privée
        private_key = generate_private_key()

        # Demander le mot de passe à l'utilisateur
        password = getpass("Entrez un mot de passe pour chiffrer la clé privée: ")

        # Sauvegarder la clé privée chiffrée
        save_encrypted_private_key(private_key, password)

        # Générer la clé publique
        public_key = private_key_to_public_key(private_key)
        
        # Convertir la clé publique en adresse Bitcoin
        address = public_key_to_address(public_key)
        
        # Sauvegarder la clé publique dans un fichier
        with open('keys/public/public_key.txt', 'w') as file:
            file.write(public_key_to_bytes(public_key).hex())
        
        messagebox.showinfo("Succès", f"Clé privée chiffrée sauvegardée!\nAdresse : {address}")
    except Exception as e:
        show_error(str(e))

def read_key():
    try:
        password = getpass("Entrez le mot de passe pour déchiffrer la clé privée: ")
        private_key = load_and_decrypt_private_key(password)
        messagebox.showinfo("Clé Privée", f"Clé privée déchiffrée : {private_key}")
    except Exception as e:
        show_error(str(e))

def main():
    root = tk.Tk()
    root.title("Cold Wallet")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    title_label = tk.Label(frame, text="Cold Wallet - Interface", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    btn_generate = tk.Button(frame, text="Générer et chiffrer la clé", command=generate_key)
    btn_generate.grid(row=1, column=0, pady=10)

    btn_read = tk.Button(frame, text="Lire la clé privée chiffrée", command=read_key)
    btn_read.grid(row=2, column=0, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
