import tkinter as tk
from tkinter import messagebox
from Odoo import *
from Page_Logisitique import *
from Page_Prod import *
from tkinter import PhotoImage
from Image import *

class LoginPage:
    def __init__(self, master, erp_instance):
        self.master = master
        self.erp_instance = erp_instance
        self.master.title("Page de Connexion")

        # Charger et redimensionner l'image de fond
        image_pil = Image.open("Image/HGABADCO WITHOUT TEXT-1.png")
        image_pil = image_pil.resize((1920, 1080), Image.LANCZOS)
        self.image_de_fond = ImageTk.PhotoImage(image_pil)
        # Créer un Canvas pour afficher l'image en fond
        self.canvas = tk.Canvas(self.master, width=self.image_de_fond.width(), height=self.image_de_fond.height())
        self.canvas.pack()

        # Charger et redimensionner l'image pour l'icône de la fenêtre
        icon_pil = Image.open("Image/icone_odoo.png")
        icon_pil = icon_pil.resize((32, 32), Image.LANCZOS)
        self.icon = ImageTk.PhotoImage(icon_pil)
        # Définir l'icône de la fenêtre
        self.master.iconphoto(True, self.icon)

        # Charger et redimensionner l'image de croix
        croix_pil = Image.open("Image/croix.png")
        croix_pil = croix_pil.resize((40, 40), Image.LANCZOS)
        self.croix = ImageTk.PhotoImage(croix_pil)


        # Définition des tailles de police
        champ_font = ("Helvetica", 15)  # Ajustez la taille de la police des champs de saisie
        label_font = ("Helvetica", 18) # Ajustez la taille de la police des labels
        title_font = ("Helvetica", 40, "bold") # Ajustez la taille de la police du titre

        # Calculer les coordonnées pour centrer
        center_x = self.image_de_fond.width() // 2
        center_y = self.image_de_fond.height() // 2


        # Création des champs de sasie
        self.username_entry = tk.Entry(self.master, font=champ_font, width=18, bd=5)
        self.password_entry = tk.Entry(self.master, show="*", font=champ_font, width=18, bd=5)
        # Positionner les champs de saisie à des coordonnées centrées sur le Canvas
        self.canvas.create_window(center_x, center_y - 18, window=self.username_entry)
        self.canvas.create_window(center_x, center_y + 71, window=self.password_entry)
        
        # Création des boutons 
        self.login_button = tk.Button(self.master, text="Connexion", command=self.on_login_clicked, font=champ_font, width=18)
        self.close_button = tk.Button(self.master, command=self.close, image=self.croix, bg="white", borderwidth=0, highlightthickness=0)
        # Positionnement des boutons sur le Canvas
        self.canvas.create_window(center_x, center_y + 159, window=self.login_button)
        self.canvas.create_window(center_x + 404,  center_y -280, window=self.close_button)

        # Ajouter les labels pour le nom d'utilisateur, le mot de passe et le titre
        self.label_username = tk.Label(self.master, text="Nom d'utilisateur :", font=label_font, bg="white")
        self.label_password = tk.Label(self.master, text="Mot de passe :", font=label_font, bg="white")
        self.label_title = tk.Label(self.master, text="IDENTIFICATION", font=title_font, bg="white")       
        # Positionner les labels
        self.canvas.create_window(center_x - 11, center_y - 50, window=self.label_username)
        self.canvas.create_window(center_x - 27, center_y + 39, window=self.label_password)
        self.canvas.create_window(center_x, center_y - 130, window=self.label_title)


        # Afficher l'image en fond
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_de_fond)

        # Afficher en plein écran
        self.master.attributes('-fullscreen', True)

    def on_login_clicked(self):

        # Récupération du mot de passe et du nom d'utilisateur
        username = self.username_entry.get()
        password = self.password_entry.get()
        #password = "1234"
        #username = "Auxence"
        models, uid = self.erp_instance.connexion(username, password)
        Utilisateur = User(username,password,models,uid)      

        if models and uid:
            
            # Utilisation de la même instance pour récupérer le département_id
            Utilisateur.department_id = self.erp_instance.get_department_id(Utilisateur.uid, Utilisateur.password)

            if Utilisateur.department_id== 4:
                messagebox.showinfo("Connexion réussie", "Bienvenue ! " + Utilisateur.username)
                self.hide_elements()  # Appeler la fonction pour cacher les éléments                
                LogistiquePage(self.master, self.erp_instance, Utilisateur).pack()

            elif  Utilisateur.department_id==3:
                messagebox.showinfo("Connexion réussie", "Bienvenue ! " + Utilisateur.username)
                self.hide_elements()  # Appeler la fonction pour cacher les éléments
                ProdPage(self.master,self.erp_instance, Utilisateur).pack()
            
            elif Utilisateur.department_id==1:
                messagebox.showinfo("Connexion réussie", "Bienvenue ! " + Utilisateur.username)
                self.boutton_admin() # Appeler la fonction pour afficher les boutons admins

            else:
                messagebox.showerror("Acces non autorisé","Connexion réussie, " + Utilisateur.username + " Vous n'avez pas accès à ce logiciel.")
        else:
            messagebox.showerror("Erreur de connexion", "Échec de la connexion. Vérifiez vos informations d'authentification.")

    def hide_elements(self):

        # Cacher les champs de saisie
        self.username_entry.pack_forget()
        self.password_entry.pack_forget()

        # Cacher les labels
        self.label_username.pack_forget()
        self.label_password.pack_forget()
        self.label_title.pack_forget()

        # Cacher les boutons
        self.login_button.pack_forget()
        self.close_button.pack_forget()

        # Cacher l'image en utilisant pack_forget() sur le Canvas
        self.canvas.pack_forget()

    def boutton_admin(self):

        # Récupération du mot de passe et du nom d'utilisateur
        username = self.username_entry.get()
        password = self.password_entry.get()        
        models, uid = self.erp_instance.connexion(username, password)
        Utilisateur = User(username,password,models,uid) 

        # Définition des tailles de police
        admin_font = ("Helvetica", 20)  # Ajustez la taille de la police des champs de saisie

        # Calculer les coordonnées pour centrer
        center_x = self.image_de_fond.width() // 2
        center_y = self.image_de_fond.height() // 2

        # Définir les actions à effectuer lorsque les boutons admins sont cliqués
        def on_logistique_click():
            self.hide_elements()
            LogistiquePage(self.master, self.erp_instance, Utilisateur).pack()

        def on_production_click():
            self.hide_elements()
            ProdPage(self.master, self.erp_instance, Utilisateur).pack()  

        # Création des boutons 
        self.logistique_button = tk.Button(self.master, text="Logistique", command=on_logistique_click, font=admin_font, width=13, height=2, borderwidth=2)
        self.production_button = tk.Button(self.master, text="Production", command=on_production_click, font=admin_font, width=13, height=2, borderwidth=2)
        # Positionnement des boutons 
        self.canvas.create_window(center_x -250, center_y + 250, window=self.logistique_button)
        self.canvas.create_window(center_x + 250,  center_y + 250, window=self.production_button)
                
    def close(self):
        # Fermeture de la page de Log In
        self.master.destroy()
        

