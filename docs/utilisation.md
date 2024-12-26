
# Lancer l'application

1. Clonez ce projet ou assurez-vous d'avoir les fichiers nécessaires sur votre machine.
2. Ouvrez un terminal et accédez au répertoire contenant le projet.
3. Lancez l'application avec la commande suivante :
   ```bash
    python src/scripts/manage_wallet.py 
   ```
   Cela ouvrira l'interface graphique de gestion du Cold Wallet.

# Fonctionnalités disponibles

### 1. Générer une clé Bitcoin
Cliquez sur le bouton **"Générer une clé Bitcoin"** pour générer une nouvelle clé privée. Une fois générée, la clé sera sauvegardée dans le fichier `private_key.txt`.

### 2. Lire la clé privée
Cliquez sur le bouton **"Lire la clé privée"** pour afficher la clé privée qui a été précédemment générée et sauvegardée dans le fichier `private_key.txt`.

### 3. Chiffrer la clé privée
Cliquez sur le bouton **"Chiffrer la clé privée"** pour chiffrer la clé privée avec une phrase secrète que vous choisissez. Cette clé chiffrée sera sauvegardée dans le fichier `private_key.enc`.

### 4. Déchiffrer la clé privée
Cliquez sur le bouton **"Déchiffrer la clé privée"** pour déchiffrer la clé privée chiffrée. Vous devrez entrer la phrase secrète pour effectuer le déchiffrement et récupérer la clé privée.

### 5. Créer une transaction
Cliquez sur le bouton **"Créer une transaction"** pour lancer le processus de création d'une transaction (bien que cette fonctionnalité soit un placeholder dans la version actuelle).

### 6. Signer une transaction
Cliquez sur le bouton **"Signer une transaction"** pour lancer le processus de signature d'une transaction (également un placeholder).

### 7. Quitter l'application
Cliquez sur le bouton **"Quitter"** pour fermer l'application.