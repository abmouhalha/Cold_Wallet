# Architecture du Cold Wallet

L'architecture du Cold Wallet est composée de plusieurs composants afin de gérer les clés privées, de permettre le chiffrement et le déchiffrement, ainsi que de gérer les transactions. Cette architecture repose sur une interface graphique simple avec Tkinter, et utilise des mécanismes de sécurité comme le chiffrement AES et la dérivation de clés avec PBKDF2.

## Composants principaux

### 1. **Interface graphique (Tkinter)**

L'interface graphique est construite à l'aide de la bibliothèque Tkinter, qui permet d'afficher une interface utilisateur simple et conviviale. Elle inclut plusieurs boutons pour exécuter différentes actions, telles que la génération de clés, le chiffrement, le déchiffrement, la création et la signature de transactions.

### 2. **Gestion des clés (Cryptographie)**

Le Cold Wallet permet de gérer des clés privées pour des adresses Bitcoin. Ces clés sont stockées dans des fichiers sécurisés. Le système utilise un chiffrement AES pour protéger les clés privées et un mécanisme de dérivation de clés via PBKDF2 pour renforcer la sécurité de l'utilisateur.

#### Fonctionnalités des clés privées :
- **Génération de clé privée** : Les clés privées peuvent être générées et sauvegardées sur le système.
- **Lecture et affichage de clé privée** : Il est possible de lire la clé privée à partir d'un fichier.
- **Chiffrement et déchiffrement de la clé privée** : La clé privée peut être chiffrée avec une phrase secrète et stockée sous forme chiffrée dans un fichier.
- **Sécurisation via une phrase secrète** : La clé de chiffrement est dérivée d'une phrase secrète fournie par l'utilisateur.

### 3. **Création et gestion des transactions**

Le Cold Wallet permet de créer et de signer des transactions. Bien que la logique des transactions soit un simple placeholder, cette partie peut être étendue pour inclure la gestion réelle des transactions Bitcoin.

### 4. **Gestion des fichiers**

Les fichiers sont organisés dans des répertoires spécifiques pour garantir la sécurité et la séparation des données sensibles :

/keys /private - private_key.txt # Clé privée non chiffrée - private_key.enc # Clé privée chiffrée


### 5. **Flux de travail**

1. **Génération de clés** : Un utilisateur peut générer une clé Bitcoin via l'interface graphique.
2. **Chiffrement de la clé privée** : La clé privée générée ou lue peut être chiffrée à l'aide d'une phrase secrète.
3. **Sauvegarde des clés** : Les clés sont sauvegardées dans un fichier sécurisé.
4. **Déchiffrement de la clé privée** : Si nécessaire, l'utilisateur peut déchiffrer sa clé privée en fournissant la phrase secrète.

---

## Technologies utilisées

- **Tkinter** : Bibliothèque standard pour les interfaces graphiques en Python.
- **hashlib** : Utilisé pour le dérivatif de clé sécurisé via PBKDF2.
- **AES** : Algorithme de chiffrement symétrique pour sécuriser la clé privée.

---

## Diagramme de flux

1. L'utilisateur lance l'application via l'interface graphique.
2. Il peut générer une clé privée.
3. Cette clé peut être chiffrée avec une phrase secrète.
4. Les fichiers sont stockés dans le répertoire sécurisé `/keys/private`.
5. L'utilisateur peut déchiffrer les clés privées selon ses besoins, en fournissant la phrase secrète.
