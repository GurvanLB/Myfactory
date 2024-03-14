# INSTALLATION CLIENT
# CONFIGURATION RESEAU CLIENT
Avant toute configuration du réseau vérifier que le serveur et les clients sont dans le meme réseau.

1. Après avoir importer votre VM linux, avant de la lancer. Aller dans l'onglet `Machine` de virtuabox.
2. Cliquer sur l'onglet `Configuration`.
3. Aller dans l'onglet `Réseau`.
4. Aller dans l'onglet `Adptater 1`de la page `Reseau`.
   
   ![Photo de la page réseau](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Page%20Reseau.PNG)
5. Dans la liste déroulante `Mode d'accès réseau`: Choisissez NAT.
6. Cocher `Activer l'interface réseau`

## INSTALLATION APPLICATION PYTHON
1. Télécharger le dossier```application``` disponible sur le git.
### MACHINE WINDOWS
1. Installer python
   Dans le microsoft store: télécharger le module python 3.10
   
2. Vérifier la version de python
   Saisir dans le terminal:
     ```
   python3 --version
    ```
3. Télécharger le module complémentaire: Pillow\
    Saisir dans le terminal: 
    ```
   pip install Pillow10
    ```
4. Vérifier la version de Pillow\
    Saisir dans le terminal: 
    ```
   pip list
    ```
    Pillow doit être en version 10
### MACHINE LINUX
1. Installer python
    Saisir dans le terminal: 
    ```
    sudo apt update
    sudo apt install python3
    ```
2. Vérifier la version de python
   Saisir dans le terminal: 
    ```
   python3 --version
    ```
   Python doit être en version 3.9.2
3. Télécharger le module complémentaire: Pillow
    Saisir dans le terminal: 
    ```
   pip install Pillow10
    ```
4. Vérifier la version de Pillow\
    Saisir dans le terminal: 
    ```
   pip list
    ```
    Pillow doit être en version 10
## LANCER L'APPLICATION
1. Ouvrir le terminal
2. Copier le chemain d'acces vers le dossier ```application``` qui est sur votre PC.
3. Saisir dans le terminal:
   ```
   cd chemin_d'acces_vers_dossier_application
    ```
4. Verifier que vous êtes bien dans le bon dossier
5. Lancer l'application
   Saisir dans le terminal:
   ```
   python3 Main.py
    ```
   ##CONFIGURER L'APPLICATION 
Pour que l'application communique correctement avec odoo vous devez rentrer l'adresse ip de la machine physique sur lequel est instalé votre serveur ODOO.Sinon vous n'arriverez meme pas à vous connectez sur l'application.
1. Ouvrir le fichier `Odoo.py` qui est dans votre dossier `Application`.
2. Dans celui-ci vous devez modifier l'addresse ip entre "" pour mettre celle du PC_1 dans votre réseau local.
3. Sauvegarder et relancer l'application
4. Si un problème de communication persiste verifier que le nom de la db sur votre Odoo correspond bien à celui présent dans le fichier Odoo.py qui est dans votre dossier `Application`.
