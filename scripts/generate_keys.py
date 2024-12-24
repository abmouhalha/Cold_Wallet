from bitcoinlib.keys import Key

def generate_bitcoin_key():
    # Générer une nouvelle clé privée
    key = Key()
    
    # Clé privée en format WIF (Wallet Import Format)
    private_key = key.wif()
    
    # Clé publique en format hexadécimal
    public_key = key.public_hex
    
    print("Clé privée (WIF) : ", private_key)
    print("Clé publique : ", public_key)

if __name__ == "__main__":
    generate_bitcoin_key()
