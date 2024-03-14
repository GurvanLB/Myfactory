# HGABADCO PROJET NUMERISATION INDUSTRIEL
Bienvenue sur la page d'accueil du projet numérisation industriel de l'entreprise HGABadCo.
##  OBJECTIF PROJET
L'objectif de ce projet est de faire évoluer la communication entre les postes de travails et l'administration afin de simplifier et centralisé les informations sur un serveur Commun.

Notre but est de faire communiquer 4 postes de travails différents par le biais de notre ERP et d'un client lourd.Ainsi de centraliser les informations sur notre ERP.

* Poste Administrateur 
* Poste Vente 
* Poste Production 
* Poste Logistique 

## ORGANISATION PROJET 
### ARCHITECTURE MATERIEL
* Poste Administrateur -> ordinateur portable :OS non definis
* Poste Vente -> ordinateur portable :OS non definis
* Poste Production -> Odinateur fixe avec VM : OS Windows
* Poste Logistique -> Odinateur fixe avec VM : OS linux
  
### ARCHITECTURE RESEAU
  ![Photo de l'architecture des postes de travails et réseaux](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Architecture%20reseau.PNG?raw=true)
### ARCHITECTURE LOGICIEL
Notre projet est divisé en 2 parties logiciels

* Le serveur ERP et client léger ODOO (Interface Web ERP) -> Poste Administrateur / Vente
* Client lourd (Interface Python avec tkinter) -> Poste Production / Logistique
  

### FONCTIONNALITES LOGICIEL
#### CLIENT LEGER / ERP ODOO
* [x] Création de compte "Modification BDD login"
* [x] Gestion des accès utilisateur
* [x] Création D'articles (Nom, Prix, Image)
* [x] Création d'Ordre de fabrication
* [x] Historique des actions utilisateurs
* [x] Création des Bons de Livraison et de Réception

      
#### CLIENT LOURD / APPLICATION PYTHON
* [x] Connexion compte utilisateur Odoo
* [x] Redirection page département ( Logistique/ Production )
* [x] Modification des stocks et visualtisation des articles
* [x] Modification des etats des ordres de fabrication
* [x] Bouton de deconnexion (Fermer application pour le moment)
* [x] Interface Administrateur, accès page production et logisitque
* [ ] Actualisation automatique de l'interface toutes les 30 secondes (Bouton d'actualisation pour le moment)

## ARCHITECTURE APPLICATION
### CLIENT LOURD
### ARCHITECTURE PROGRAMME
  ![Architecture programme](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Architecture_prog-Page-2.jpg)
### VISUALISATION INTERFACE
#### PAGE DE CONNEXION
  ![PAGE CONNEXION](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Page_login.png)
#### PAGE LOGISTIQUE
  ![PAGE LOGISTIQUE](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Page_logistique.png)
#### PAGE PRODUCTION
### CLIENT LEGER / SERVEUR ODOO
### ARCHITECTURE PROGRAMME
 ![ARCHITECTURE CLIENT LEGER](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Archi_leger.jpg)
### VISUALISATION INTERFACE
#### PAGE CONNEXION 
 ![ARCHITECTURE CLIENT LEGER](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Archi_leger.jpg)
 #### PAGE EMPLOYES
 ![ARCHITECTURE CLIENT LEGER](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Archi_leger.jpg)
#### PAGE LOGISTIQUE
 ![ARCHITECTURE CLIENT LEGER](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Archi_leger.jpg)
 #### PAGE PRODUCTION
 ![ARCHITECTURE CLIENT LEGER](https://github.com/GurvanLB/Myfactory/blob/main/Application/Image/Archi_leger.jpg)
