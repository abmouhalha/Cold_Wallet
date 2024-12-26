import sys
import os
import tkinter as tk
from tkinter import messagebox
from getpass import getpass
from wallet import generate_private_key, private_key_to_public_key, public_key_to_address
from utils import save_file, read_file, create_directory_if_not_exists  # Assurez-vous que cette fonction existe

# Si public_key_to_bytes n'est pas défini, ajoutez cette fonction ici
def public_key_to_bytes(public_key):
    """Convertir une clé publique (tuple) en bytes pour le hashing."""
    x, y = public_key
    x_bytes = x.to_bytes(32, byteorder='big')
    y_bytes = y.to_bytes(32, byteorder='big')
    return b'\x04' + x_bytes + y_bytes  # Format non compressé

def show_error(message):
    messagebox.showerror("Erreur", message)

def generate_key():
    try:
        # Créer les répertoires si nécessaires
        create_directory_if_not_exists('keys/private')
        create_directory_if_not_exists('keys/public')

        # Générer la clé privée
        private_key = generate_private_key()
        
        # Générer la clé publique
        public_key = private_key_to_public_key(private_key)
        
        # Convertir la clé publique en adresse Bitcoin
        address = public_key_to_address(public_key)
        
        # Sauvegarder la clé privée dans un fichier
        save_file('keys/private/private_key.txt', private_key.hex())
        
        # Sauvegarder la clé publique dans un fichier
        save_file('keys/public/public_key.txt', public_key_to_bytes(public_key).hex())
        
        # Afficher les informations dans une boîte de dialogue
        messagebox.showinfo("Succès", f"Clé privée : {private_key.hex()}\nAdresse : {address}")
    except Exception as e:
        show_error(str(e))

def read_key():
    try:
        private_key = read_file('keys/private/private_key.txt')
        messagebox.showinfo("Clé Privée", f"Clé privée lue : {private_key}")
    except Exception as e:
        show_error(str(e))

def main():
    root = tk.Tk()
    root.title("Cold Wallet")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    title_label = tk.Label(frame, text="Cold Wallet - Interface", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    btn_generate = tk.Button(frame, text="Générer une clé Bitcoin", command=generate_key)
    btn_generate.grid(row=1, column=0, pady=10)

    btn_read = tk.Button(frame, text="Lire la clé privée", command=read_key)
    btn_read.grid(row=2, column=0, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
