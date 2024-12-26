import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scripts.generate_keys import generate_private_key, private_key_to_public_key, public_key_to_address  # Import correct

class TestGenerateKeys(unittest.TestCase):
    def test_generate_private_key(self):
        private_key = generate_private_key()
        self.assertEqual(len(private_key), 32)  # Vérifiez que la clé privée est de 32 octets

    def test_private_key_to_public_key(self):
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        self.assertEqual(len(public_key), 2)  # Vérifiez que la clé publique a 2 valeurs (x, y)

    def test_public_key_to_address(self):
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        address = public_key_to_address(public_key)
        self.assertTrue(address.startswith("1") or address.startswith("3"))  # Vérifiez que l'adresse commence par 1 ou 3

if __name__ == '__main__':
    unittest.main()
