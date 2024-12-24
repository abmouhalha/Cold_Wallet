import sys
from read_private_key import read_private_key
from decrypt_key import decrypt_private_key
from generate_keys import generate_bitcoin_key
from create_transaction import create_transaction
from sign_transaction import sign_transaction

def show_menu():
    print("\n### Interface de Gestion du Cold Wallet ###")
    print("1. Générer une nouvelle clé Bitcoin")
    print("2. Lire la clé privée")
    print("3. Déchiffrer la clé privée")
    print("4. Créer une transaction")
    print("5. Signer une transaction")
    print("6. Quitter")

def main():
    while True:
        show_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            generate_bitcoin_key()  # Générer une clé Bitcoin
        elif choix == "2":
            read_private_key()  # Lire la clé privée depuis un fichier
        elif choix == "3":
            decrypt_private_key()  # Déchiffrer la clé privée
        elif choix == "4":
            create_transaction()  # Créer une transaction
        elif choix == "5":
            sign_transaction()  # Signer une transaction
        elif choix == "6":
            print("Au revoir !")
            sys.exit(0)
        else:
            print("Option invalide, essayez de nouveau.")

if __name__ == "__main__":
    main()
