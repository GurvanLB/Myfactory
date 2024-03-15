# INSTALLATION SERVEUR
L'installation du serveur se fait sur une VM linux Debian avec le gestionnaire de VM Virtuabox.

## CONFIGURATION RESEAU SERVEUR
Avant toute configuration du réseau vérifier que le serveur et les clients sont dans le meme réseau.

1. Importer votre VM linux, avant de la lancer. Aller dans l'onglet `Machine` de virtuabox.
2. Cliquer sur l'onglet `Configuration`.
3. Aller dans l'onglet `Réseau`.
4. Aller dans l'onglet `Adptater 1`de la page `Reseau`.
   
   ![Photo de la page réseau](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Page%20Reseau.PNG)
6. Dans la liste déroulante `Mode d'accès réseau`: Choisissez NAT.
7. Dérouler les paramètres `Advanced` de la page `Reseau`.

   ![Photo de la page réseau advanced](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Page%20Reseau%20Advanced.PNG)
8. Cliquer sur le bouton `Redirection des ports`. la page `Règles de redirection ports` doit s'ouvrir.
9. Ajouter une règle en indiquant le protocole : TCP / Port Hôte: 8069  Port Invité: 8069.\
    prendre exemple sur l'image ci-dessous:

    ![Photo de la page réseau advanced](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Table%20Redirection%20ports.PNG)
## INSTALLATION ET CONFIGURATION ODOO

###  INSTALLER DOCKER ET PORTAINER SOUS LINUX
1. Installation du module docker\
   Saisir dans le terminal: 
   ```
   sudo apt update
   sudo apt install docker.io
   ```
2. Lancement du module docker\
   Saisir dans le terminal: 
   ```
   sudo systemctl start docker
   ```
4. Création d'une zone mémoire pour Portainer\
   Saisir dans le terminal:
   ```
   sudo docker volume create portainer_data
   ```
6. Création du container Portainer\
   Saisir dans le terminal:
   ```
   sudo docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
   ```
7. Vérifier l'accés à portainer.io sur la machine du serveur.
   Ouvrir le navigateur web et saisir:
   ```
   http://localhost:9000
   ```
###  INSTALLER  ODOO ET POSTGREESQL SUR PORTAINER
1. Se connecter à l'interface web portainer
   ```
   http://adresse_ip_machine_virtuelle:9000
   ```
    ![Portainer MAINPAGE](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Portainer%20Home.png)
2. Accédez à l'interface Stacks : Dans le panneau de navigation à gauche, cliquez sur "Stacks".
    ![Portainer MAINPAGE](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Portainer%20Home.png)
3. Créez un nouveau stack : Cliquez sur le bouton "Add a stack" (ou "Ajouter un stack"). Cela vous amènera à l'écran de création d'un nouveau stack.
 ![Portainer MAINPAGE](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/portainer%20docker%20compose.png)
4. Importez votre fichier `docker_compose` disponnible sur le git/SSD dans le dossier Odoo : Dans l'interface de création de stack, vous verrez une zone de texte pour "Stack name" (nom du stack) et une autre pour "Web editor" (éditeur web). Collez le contenu du fichier `docker_compose` dans la zone "Web editor".

5. Déployez le stack : Après avoir importé le fichier `docker_compose`, cliquez sur le bouton "Deploy the stack" en bas de la page. Portainer va alors lire le fichier `docker_compose`, créer les services `ODOO` et `POSTGREESQL`

6. Attendez que le déploiement soit terminé
   
7. Vérifier la creatiion des ccontainer Odoo et Postgree sur la page suivante
   

###  INSTALLER LA BASE DE DONNEE ODOO
1. Accéder à l'interface d'administration d'Odoo : Connectez-vous à l'interface d'administration d'Odoo en utilisant un navigateur web. Vous aurez besoin des identifiants d'administration pour accéder à cette interface.

2. Accéder au module "Paramètres" : Dans l'interface d'administration, cliquez sur l'icône de configuration en haut à droite de la page pour accéder au module "Paramètres".

3. Accéder au module "Gestion des bases de données" : Dans le menu déroulant du module "Paramètres", sélectionnez le module "Gestion des bases de données".

4. Sélectionner la base de données à restaurer : Dans la liste des bases de données, recherchez et sélectionnez la base de données que vous souhaitez restaurer.

5. Restaurer la base de données : Une fois que vous avez sélectionné la base de données à restaurer, recherchez l'option ou le bouton qui vous permet de restaurer la base de données. Cela peut être étiqueté comme "Restaurer", "Importer".

6. Sélectionner le fichier de sauvegarde : Lorsque vous êtes invité à sélectionner le fichier de sauvegarde, choisissez le fichier de sauvegarde de la base de données que vous souhaitez restaurer. Assurez-vous que le fichier de sauvegarde est au format compatible avec Odoo.

###  INSTALLER LES MODULES ODOO
Pour Le fonctionnement de l'application python nous utilisons des modules complémentaires de Odoo. Il est important de les installer avant d'utiliser l'application.
  ```
  1. Fabrication (Module de gestion de fabrication et nomenclature d'article) 
  2. Employer (Module de gestion des données des utilisateurs odoo) 
 ```
1. Accéder à l'interface d'administration d'Odoo : Connectez-vous à l'interface d'administration d'Odoo en utilisant un navigateur web. Vous aurez besoin des identifiants d'administration pour accéder à cette interface.

2. Accéder au module "Applications" : Dans l'interface d'administration, recherchez et cliquez sur le module "Applications". Ce module vous permet de rechercher, d'installer et de gérer les applications disponibles dans Odoo.

3. Rechercher l'application à installer : Utilisez la fonction de recherche pour trouver l'application que vous souhaitez installer. Vous pouvez rechercher par nom, catégorie ou mots-clés.

4. Sélectionner l'application : Une fois que vous avez trouvé l'application que vous souhaitez installer, cliquez dessus pour accéder à sa page d'informations.

5. Installer l'application : Sur la page d'informations de l'application, recherchez le bouton "Installer" ou "Get it" (obtenir) et cliquez dessus pour commencer le processus d'installation. Odoo téléchargera et installera automatiquement l'application sur votre instance.
6. Il se peut que le module demande des configurations supplémentaires. Si c'est le cas contacter une personne du service O.T

