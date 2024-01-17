import tkinter as tk
from tkinter import messagebox
from Odoo import *
from Page_Logisitique import *
from Page_Prod import *
from tkinter import PhotoImage

class LoginPage:
    def __init__(self, master, erp_instance):
        self.master = master
        self.erp_instance = erp_instance
        master.title("Page de Connexion")

        # Création des widgets
        self.label_username = tk.Label(master, text="Nom d'utilisateur:")
        self.username_entry = tk.Entry(master)
        self.label_password = tk.Label(master, text="Mot de passe:")
        self.password_entry = tk.Entry(master, show="*")
        self.login_button = tk.Button(master, text="Se connecter", command=self.on_login_clicked)

        # Placement des widgets
        self.label_username.pack()
        self.username_entry.pack()
        self.label_password.pack()
        self.password_entry.pack()
        self.login_button.pack()
        #Recupération of en attente
        

    def title_change(self,new_title):
        self.master.title(new_title)

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
                LogistiquePage(self.master, self.erp_instance, Utilisateur).pack()
                self.label_username.pack_forget()
                self.username_entry.pack_forget()
                self.label_password.pack_forget()
                self.password_entry.pack_forget()
                self.login_button.pack_forget()
            elif  Utilisateur.department_id==3:
                messagebox.showinfo("Connexion réussie", "Bienvenue ! " + Utilisateur.username)
                self.label_username.pack_forget()
                self.username_entry.pack_forget()
                self.label_password.pack_forget()
                self.password_entry.pack_forget()
                self.login_button.pack_forget()
                ProdPage(self.master,self.erp_instance, Utilisateur).pack()
                
            else:
                messagebox.showerror("Acces non autorisé","Connexion réussie, " + Utilisateur.username + " Vous n'avez pas accès à ce logiciel.")
        else:
            messagebox.showerror("Erreur de connexion", "Échec de la connexion. Vérifiez vos informations d'authentification.")
