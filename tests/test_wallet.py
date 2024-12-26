import unittest
from src.wallet import generate_private_key, private_key_to_public_key, public_key_to_address, public_key_to_bytes

class TestWallet(unittest.TestCase):

    def test_private_key_format(self):
        private_key = generate_private_key()
        # Vérifie que la clé privée est de 32 octets
        self.assertEqual(len(private_key), 32)
        self.assertTrue(all(c in "0123456789abcdef" for c in private_key.hex()))

    def test_public_key_format(self):
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        public_key_bytes = public_key_to_bytes(public_key)
        # Vérifie que la clé publique est bien en format non compressé (65 octets)
        self.assertEqual(len(public_key_bytes), 65)

    def test_address_format(self):
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        address = public_key_to_address(public_key)
        # Vérifie que l'adresse commence par '1' (format Bitcoin standard)
        self.assertTrue(address.startswith('1'))
        self.assertEqual(len(address), 34)

if __name__ == '__main__':
    unittest.main()
