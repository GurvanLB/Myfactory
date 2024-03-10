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
* Création de compte "Modification BDD login"
* Gestion des accès utilisateur
* Création D'articles (Nom, Prix, Image)
* Création d'Ordre de fabrication
#### Client Lourd / application python
* Connexion compte utilisateur Odoo
* Redirection page département ( Logistique/ Production )

 ##  Installation docker de ODOO et POSTGREESQL
1. Installation du module docker\
   Ouvrir un terminal
   
```
sudo apt update
sudo apt install docker.io
```


  
  


