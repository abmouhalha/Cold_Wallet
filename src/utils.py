import os

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except Exception as e:
        raise Exception(f"Erreur lors de la sauvegarde du fichier {file_path}: {str(e)}")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Erreur lors de la lecture du fichier {file_path}: {str(e)}")

def generate_unique_filename(base_path, extension=".txt"):
    import time
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return f"{base_path}_{timestamp}{extension}"