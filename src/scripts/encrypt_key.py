import os
import hashlib

def derive_key(password, salt=None):
    """
    Dérive une clé de 256 bits à partir d'un mot de passe et d'un sel
    en utilisant l'algorithme PBKDF2 avec SHA-256. Si aucun sel n'est
    fourni, un sel aléatoire est généré.
    """
    if salt is None:
        salt = os.urandom(16)  # Générer un sel aléatoire de 16 octets
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)
    return key, salt
