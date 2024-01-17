import tkinter as tk
from tkinter import messagebox
import xmlrpc.client

class LoginPage:
    def __init__(self, root):
        self.ip = "172.31.11.122"
        self.db = "HGABadCo"
        self.port = "8069"
        self.common = None
        self.models = None
        self.uid = None

        # Titre de la page
        self.root = root
        self.root.title("Page de Connexion")

        # Texte et champ de saisie pour nom d'utilisateur
        self.username_label = tk.Label(root, text="Nom d'utilisateur:")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=10)

        # Texte et champ de saisie pour mot de passe
        self.password_label = tk.Label(root, text="Mot de passe:")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=10)

        # Bouton de connexion
        self.login_button = tk.Button(root, text="Connexion", command=self.authenticate)
                                      
        self.login_button.pack(pady=20)

    def authenticate(self):
        
        identifiant = self.username_entry.get()
        mot_de_passe = self.password_entry.get()

        # Vérifier les identifiants
        self.connexion(self.ip, self.db, self.port),
        self.uid = self.common.authenticate(self.db, identifiant, mot_de_passe, {})
        print (self.uid)

        if self.uid:
            messagebox.showinfo("Connexion Réussie", "Bienvenue, " + identifiant + "!")
        else:
            messagebox.showerror("Echec de connexion", "Identifiants incorrects")

    def connexion(self):
        # Connexion à Odoo
        url = f"http://{self.ip}:{self.port}/xmlrpc/2"
        self.common = xmlrpc.client.ServerProxy(f'{url}/common')
        self.models = xmlrpc.client.ServerProxy(f'{url}/object')
        print (url)

    def close(self):
        self.common = None
        self.models = None
        self.uid = None
        
   

# Création de la fenêtre principale
root = tk.Tk()
login_page = LoginPage(root)

# Lancement de la boucle principale de tkinter
root.mainloop()