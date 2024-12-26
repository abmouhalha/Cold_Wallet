from mnemonic import Mnemonic

def generate_seed_phrase():
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)  # Assurez-vous que la génération est correcte
    return seed_phrase
