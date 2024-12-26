import sys
import os

# Ajouter le répertoire 'src' au path pour que Python puisse importer les modules de 'src/scripts'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'scripts')))

from generate_keys import generate_private_key, private_key_to_public_key, public_key_to_address, base58_encode
import unittest

class TestGenerateKeys(unittest.TestCase):

    def test_generate_private_key(self):
        private_key = generate_private_key()
        self.assertEqual(len(private_key), 32)

    def test_public_key_to_address(self):
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        address = public_key_to_address(public_key)
        self.assertTrue(address.startswith('1'))

    def test_base58_encode(self):
        data = b'\x00\x14\x85'  # Exemple de donnée
        encoded = base58_encode(data)
        self.assertIsInstance(encoded, str)
        self.assertGreater(len(encoded), 0)

if __name__ == '__main__':
    unittest.main()
