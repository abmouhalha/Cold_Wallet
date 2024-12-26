import hashlib

def create_transaction():
    try:
        # Demander à l'utilisateur l'adresse du destinataire et le montant
        recipient_address = input("Entrez l'adresse du destinataire : ")
        amount = float(input("Entrez le montant en BTC : "))

        # Simuler une transaction (les entrées et sorties)
        tx = {
            "inputs": [
                {"txid": "sample_txid", "vout": 0}  # Exemple de donnée, nécessite txid réel
            ],
            "outputs": [
                {"address": recipient_address, "amount": amount}
            ]
        }

        # Imprimer la transaction simulée
        print("Transaction créée : ", tx)
        return tx
    except Exception as e:
        print("Erreur lors de la création de la transaction :", str(e))
        return None
