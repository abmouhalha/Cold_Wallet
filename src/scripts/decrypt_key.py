import hashlib

def derive_key(password, salt):
    """
    Dérive une clé de 256 bits à partir d'un mot de passe et d'un sel
    en utilisant l'algorithme PBKDF2 avec SHA-256.
    """
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)
    return key
