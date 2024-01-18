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
        self.master.overrideredirect(True)
        # Charger et redimensionner l'image avec Pillow
        image_pil = Image.open("Application/Image/HGABADCO WITHOUT TEXT-1.png")
        image_pil = image_pil.resize((1280, 720), Image.ANTIALIAS)
        self.image_de_fond = ImageTk.PhotoImage(image_pil)

        # Créer un Canvas pour afficher l'image en fond
        self.canvas = tk.Canvas(self.master, width=self.image_de_fond.width(), height=self.image_de_fond.height())
        self.canvas.pack()

        # Création des widgets
        champ_font = ("Helvetica", 15)  # Ajustez la taille de la police
        label_font = ("Helvetica", 18) # Ajustez la taille de la police
        title_font = ("Helvetica", 40, "bold") # Ajustez la taille de la police
        self.username_entry = tk.Entry(self.master, font=champ_font, width=18, bd=5)
        self.password_entry = tk.Entry(self.master, show="*", font=champ_font, width=18, bd=5)
        self.login_button = tk.Button(self.master, text="Connexion", command=self.on_login_clicked, font=champ_font, width=18)

        # Ajouter les labels pour le nom d'utilisateur, le mot de passe et le titre
        self.label_username = tk.Label(self.master, text="Nom d'utilisateur :", font=label_font, bg="white")
        self.label_password = tk.Label(self.master, text="Mot de passe :", font=label_font, bg="white")
        self.label_title = tk.Label(self.master, text="IDENTIFICATION", font=title_font, bg="white")       

        # Calculer les coordonnées pour centrer les champs de saisie
        center_x = self.image_de_fond.width() // 2
        center_y = self.image_de_fond.height() // 2

        # Positionner les champs de saisie à des coordonnées centrées sur le Canvas
        self.canvas.create_window(center_x, center_y - 18, window=self.username_entry)
        self.canvas.create_window(center_x, center_y + 71, window=self.password_entry)

        # Positionner le bouton de connexion à des coordonnées centrées sur le Canvas
        self.canvas.create_window(center_x, center_y + 159, window=self.login_button)

        # Positionner les labels à des coordonnées spécifiques sur le Canvas
        self.canvas.create_window(center_x - 11, center_y - 49, window=self.label_username)
        self.canvas.create_window(center_x - 27, center_y + 40, window=self.label_password)
        self.canvas.create_window(center_x, center_y - 130, window=self.label_title)

        # Afficher l'image en fond
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_de_fond)

        # Empêcher le redimensionnement de la fenêtre
        self.master.resizable(width=False, height=False)

        # Centrer la fenêtre
        self.center_window()  # Modification : Appel de la nouvelle méthode

    def center_window(self):
        # Récupérer la taille de l'écran
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculer les coordonnées pour centrer la fenêtre
        x = (screen_width - self.image_de_fond.width()) // 2
        y = (screen_height - self.image_de_fond.height()) // 2

        # Définir la géométrie de la fenêtre pour la centrer
        self.master.geometry(f"{self.image_de_fond.width()}x{self.image_de_fond.height()}+{x}+{y}")


    def on_login_clicked(self):

        username = self.username_entry.get()
        password = self.password_entry.get()
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
        self.label_title.place_forget()

        # Cacher le bouton de connexion
        self.login_button.pack_forget()

        # Cacher l'image en utilisant pack_forget() sur le Canvas
        self.canvas.pack_forget()

