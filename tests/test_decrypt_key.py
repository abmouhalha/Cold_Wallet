import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scripts.decrypt_key import derive_key  # Import correct du module

class TestDecryptKey(unittest.TestCase):
    def test_derive_key(self):
        password = "testpassword"
        salt = b"testsalt"
        key = derive_key(password, salt)
        self.assertEqual(len(key), 32)  # Vérifiez que la clé dérivée est de 32 octets

if __name__ == '__main__':
    unittest.main()
