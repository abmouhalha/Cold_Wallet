from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction

def create_transaction():
    try:
        # Demander à l'utilisateur l'adresse du destinataire et le montant
        recipient_address = input("Entrez l'adresse du destinataire : ")
        amount = float(input("Entrez le montant en BTC : "))

        # Créer une transaction non signée
        tx = Transaction()

        # Ajouter des entrées et des sorties
        tx.add_input("txid_input", 0)  # ID de la transaction source (à personnaliser)
        tx.add_output(recipient_address, amount)  # Montant à envoyer

        print("Transaction créée : ", tx.as_dict())
        return tx
    except Exception as e:
        print("Erreur lors de la création de la transaction :", str(e))
        return None
