import hashlib

def derive_key(password, salt):
    # Dériver une clé avec le même processus utilisé pour le chiffrement
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)
    return key
