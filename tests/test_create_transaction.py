import unittest
from unittest import mock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scripts.create_transaction import create_transaction

class TestCreateTransaction(unittest.TestCase):
    def test_create_transaction(self):
        # Simuler l'entrée de l'utilisateur
        with mock.patch('builtins.input', side_effect=["1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", 0.001]):
            tx = create_transaction()
            self.assertIsNotNone(tx)
            self.assertIn('inputs', tx)  # Vérification des clés dans le dictionnaire
            self.assertIn('outputs', tx)  # Vérification des clés dans le dictionnaire
            self.assertEqual(tx['outputs'][0]['address'], "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")  # Vérifier l'adresse
            self.assertEqual(tx['outputs'][0]['amount'], 0.001)  # Vérifier le montant

if __name__ == '__main__':
    unittest.main()
