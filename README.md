#  HGABadCo numérisation industriel
Bienvenue sur la page d'accueil du projet numérisation industriel de l'entreprise HGABadCo.
##  Objectif Projet
L'objectif de ce projet est de faire évoluer la communication entre les postes de travails et l'administration afin de simplifier et centralisé les informations sur un serveur Commun.


### Architecture Projet
Notre but est de faire communiquer 4 postes de travails différents par le biais de notre ERP et d'un client lourd et ainsi centralisé les informations sur notre ERP.

* Poste Administrateur Client léger (accés Web ERP)
* Poste Vente Client léger (accés Web ERP)
* Poste Production Client lourd (Application python)
* Poste Logistique Client lourd (Application python)
 ###
  ![Photo de l'architecture des postes de travails et réseaux](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Architecture%20reseau.PNG?raw=true)
### Modules Projets
Notre projet est divisé en trois modules:
* Le serveur ERP Odoo avec un déploiment docker.
* Client léger (Interface Web ERP)
* Client lourd (Interface Python avec tkinter)
### Fonctionnalitées
#### Client léger / ERP Odoo
* [x] Création de compte "Modification BDD login"
* [x] Gestion des accès utilisateur
* [x] Création D'articles (Nom, Prix, Image)
* [x] Création d'Ordre de fabrication
#### Client Lourd / application python
* [x] Connexion compte utilisateur Odoo
* [x] Redirection page département ( Logistique/ Production )
* [x] Modification des stocks et visualtisation des articles
* [x] Modification des etats des ordres de fabrication
* [ ] Bouton de deconnexion (Fermer application pour le moment)
* [ ] Actualisation automatique de l'interface toutes les 30 secondes (Bouton d'actualisation pour le moment)
* [ ] Interface Administrateur, accès page production et logisitque


## INSTALLATION ET CONFIGURATION ODOO

###  INSTALLER DOCKER ET PORTAINER
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
###  INSTALLER  ODOO ET POSTGREESQL SUR PORTAINER
1. Se connecter à l'interface web portainer
   ```
   http://adresse_ip_machine_virtuelle:9000
   ```
2. Ouvrir le fichier `docker_compose` disponible sur le git.

3. Accédez à l'interface Stacks : Dans le panneau de navigation à gauche, cliquez sur "Stacks".

4. Créez un nouveau stack : Cliquez sur le bouton "Add a stack" (ou "Ajouter un stack"). Cela vous amènera à l'écran de création d'un nouveau stack.

5. Importez votre fichier `docker_compose` : Dans l'interface de création de stack, vous verrez une zone de texte pour "Stack name" (nom du stack) et une autre pour "Web editor" (éditeur web). Collez le contenu du fichier `docker_compose` dans la zone "Web editor".

6. Déployez le stack : Après avoir importé le fichier `docker_compose`, cliquez sur le bouton "Deploy the stack" en bas de la page. Portainer va alors lire le fichier `docker_compose`, créer les services `ODOO` et `POSTGREESQL`

7. Attendez que le déploiement soit terminé

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

## INSTALLATION APPLICATION PYTHON
1. Télécharger le dossier application présent sur le git.
### MACHINE WINDOWS
1. Installer python
   Dans le microsoft store: télécharger le module python 3.10
2. Télécharger le module complémentaire: Pillow
   ```
   1. Fabrication (Module de gestion de fabrication et nomenclature d'article) 
   2. Employer (Module de gestion des données des utilisateurs odoo) 
   ```
### MACHINE LINUX
1. Installer python
   Dans le microsoft store: télécharger le module python 3.10
2. Télécharger le module complémentaire: Pillow
   ```
   1. Fabrication (Module de gestion de fabrication et nomenclature d'article) 
   2. Employer (Module de gestion des données des utilisateurs odoo) 
   ```
