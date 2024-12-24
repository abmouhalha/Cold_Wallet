# generate_seed.py
import mnemonic
from bitcoinlib.keys import Key

def generate_seed_phrase():
    # Générer une clé privée
    key = Key()

    # Générer la seed phrase (mnémonique BIP39)
    mnemo = mnemonic.Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)  # 128 bits = 12 mots
    print("Seed Phrase : ", seed_phrase)

if __name__ == "__main__":
    generate_seed_phrase()
