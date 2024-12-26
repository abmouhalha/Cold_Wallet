from bitcoinlib.wallets import Wallet

def sign_transaction():
    try:
        wallet_name = input("Entrez le nom du wallet : ")
        wallet = Wallet(wallet_name)
        
        # Charger la transaction non signée (supposons que 'tx' a été créée précédemment)
        tx = wallet.create_transaction()

        # Signer la transaction
        signed_tx = wallet.sign_transaction(tx)

        print(f"Transaction signée : {signed_tx}")
        return signed_tx
    except Exception as e:
        print("Erreur lors de la signature de la transaction :", str(e))
        return None
