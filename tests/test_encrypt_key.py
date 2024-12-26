import unittest
from scripts.encrypt_key import derive_key  # Assurez-vous d'importer correctement la fonction

class TestEncryptKey(unittest.TestCase):

    def test_derive_key(self):
        password = "password123"
        key, salt = derive_key(password)
        
        # Vérification que le sel est de 16 octets
        self.assertEqual(len(salt), 16, f"Le sel doit avoir 16 octets, mais il a {len(salt)} octets.")
        
        # Vérification que la clé dérivée est bien de 32 octets
        self.assertEqual(len(key), 32, f"La clé dérivée doit avoir 32 octets, mais elle a {len(key)} octets.")
        
        # Vérifiez que la clé est dérivée correctement
        self.assertIsNotNone(key)

if __name__ == '__main__':
    unittest.main()
