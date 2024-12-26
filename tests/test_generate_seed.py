import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scripts.generate_seed import generate_seed_phrase  # Correction de l'importation

class TestGenerateSeed(unittest.TestCase):
    def test_generate_seed_phrase(self):
        # Générer une phrase mnémotechnique
        seed_phrase = generate_seed_phrase()
        self.assertEqual(len(seed_phrase.split()), 12)  # Vérifier que la seed phrase a 12 mots

if __name__ == '__main__':
    unittest.main()
