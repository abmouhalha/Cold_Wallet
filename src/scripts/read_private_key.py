import os

def read_private_key():
    # Demander à l'utilisateur de spécifier le chemin du fichier contenant la clé privée
    key_file_path = input("Entrez le chemin du fichier contenant la clé privée : ")

    # Vérifier si le fichier existe
    if not os.path.exists(key_file_path):
        print(f"Erreur : Le fichier {key_file_path} n'existe pas.")
        return

    # Ouvrir et lire le contenu du fichier
    try:
        with open(key_file_path, "r") as file:
            private_key = file.read().strip()  # Lire la clé privée et enlever les espaces
            print(f"Clé privée lue : {private_key}")
    except Exception as e:
        print(f"Erreur lors de la lecture de la clé privée : {e}")
