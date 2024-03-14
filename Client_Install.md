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
1. Télécharger le dossier``` application``` disponible sur le git.
### MACHINE WINDOWS
1. Installer python
   Dans le microsoft store: télécharger le module python 3.10
2. Télécharger le module complémentaire: Pillow\
    Saisir dans le terminal: 
    ```
   pip install Pillow
    ```
### MACHINE LINUX
1. Installer python
    Saisir dans le terminal: 
    ```
    sudo apt update
    sudo apt install python3
    ```
 1.1 Vérifier la version de python\
    ```
   python3 --version
    ``` 
    Python doit être en version 3.9.2
2. Télécharger le module complémentaire: Pillow\
    Saisir dans le terminal: 
    ```
   pip install Pillow
    ```
 1.2 Vérifier la version de Pillow\
    Saisir dans le terminal: 
    ```
   pip list
    ```
    Pillow doit être en version 10

