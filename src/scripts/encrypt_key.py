import os
import hashlib

def derive_key(password, salt=None):
    if salt is None:
        salt = os.urandom(16)  # Générer un sel aléatoire si non fourni
    # Dériver une clé à partir d'une phrase secrète et d'un sel
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)
    return key, salt
