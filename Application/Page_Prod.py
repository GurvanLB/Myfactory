import tkinter as tk
from tkinter import messagebox
from Odoo import *
from PIL import Image, ImageTk

class ProdPage(tk.Frame):
    def __init__(self, master, erp_instance, Utilisateur):
        tk.Frame.__init__(self, master)

        self.master = master
        self.erp_instance = erp_instance
        self.utilisateur = Utilisateur
        """self.master.overrideredirect(True)"""
        self.master.geometry("1920x1080")
        """master.title("Page Production")"""
        image_pil = Image.open("Application/Image/HGABADCO WITHOUT TEXT-2.png")
        image_pil = image_pil.resize((1920, 1080), Image.ANTIALIAS)
        self.image_de_fond = ImageTk.PhotoImage(image_pil)

        # Créer un Canvas pour afficher l'image en fond
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack()

        # Placer l'image sur le Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_de_fond)

        self.button_deconnexion = tk.Button(self.canvas, text="Déconnexion", width=100, height=80, bg="red", fg="white", activebackground="red", activeforeground="white", command=self.deconnexion)
        self.button_deconnexion_window = self.canvas.create_window(200, 200, anchor=tk.NW, window=self.button_deconnexion)

    def deconnexion(self):
        # Fonction à exécuter lors du clic sur le bouton de déconnexion
        # Ajoutez ici le code de déconnexion
        messagebox.showinfo("Déconnexion", "Vous êtes maintenant déconnecté.")
        self.master.destroy()  # Fermer la fenêtre principale
    
        """self.of_en_attente = self.erp_instance.recuperer_of_en_attente(self.utilisateur.uid, self.utilisateur.password)
        self.of_en_cours = self.erp_instance.recuperer_of_en_cours(self.utilisateur.uid, self.utilisateur.password)

        self.label_attente = tk.Label(self, text="OF en attente:")
        self.label_attente.pack(pady=5)
        self.listbox_attente = tk.Listbox(self, selectmode=tk.SINGLE, height=10, width=100, font=("Helvetica", 8))
        self.listbox_attente.pack(pady=5)

        for of in self.of_en_attente:
            self.listbox_attente.insert(tk.END, f"{of['name']} - {of['product_id'][1]} - "
                                                 f"Quantité à produire: {of['product_qty']} - Quantité produite: {of['qty_producing']}")

        self.label_cours = tk.Label(self, text="OF en cours:")
        self.label_cours.pack(pady=5)
        self.listbox_cours = tk.Listbox(self, selectmode=tk.SINGLE, height=10, width=100, font=("Helvetica", 8))
        self.listbox_cours.pack(pady=5)

        for of in self.of_en_cours:
            self.listbox_cours.insert(tk.END, f"{of['name']} - {of['product_id'][1]} - "
                                               f"Quantité à produire: {of['product_qty']} - Quantité produite: {of['qty_producing']}")

        self.entry_quantite_produite = tk.Entry(self)
        self.entry_quantite_produite.pack(pady=5)

        self.button_modifier_quantite = tk.Button(self, text="Modifier Quantité Produite", command=self.OF_Quantities_B_Cliked)
        self.button_modifier_quantite.pack(pady=5, padx=15)

        self.button_actualiser = tk.Button(self, text="Actualiser", command=self.Refresh_B_Cliked)
        self.button_actualiser.pack(pady=5)

        self.button_passer_en_cours = tk.Button(self, text="Passer en cours", command=self.OF_Status_Wait_Doing_B_Cliked)
        self.button_passer_en_cours.pack(pady=5)

        self.button_passer_en_attente = tk.Button(self, text="Passer en attente", command=self.OF_Status_Doing_Wait_B_Cliked)
        self.button_passer_en_attente.pack(pady=5)

        self.button_passer_fait = tk.Button(self, text="Passer à Fait", command=self.OF_Status_Doing_Done_B_Cliked)
        self.button_passer_fait.pack(pady=5)"""

    def actualiser_listbox(self):
        # Effacer et réinsérer les éléments dans les listbox
        self.listbox_attente.delete(0, tk.END)
        for of in self.of_en_attente:
            self.listbox_attente.insert(tk.END, f"{of['name']} - {of['product_id'][1]} - "
                                                 f"Quantité à produire: {of['product_qty']} - Quantité produite: {of['qty_producing']}")

        self.listbox_cours.delete(0, tk.END)
        for of in self.of_en_cours:
            self.listbox_cours.insert(tk.END, f"{of['name']} - {of['product_id'][1]} - "
                                               f"Quantité à produire: {of['product_qty']} - Quantité produite: {of['qty_producing']}")

    def OF_Status_Wait_Doing_B_Cliked(self):
        #Changer le statut de l'ordre de fabrication: Attente vers En cours
        if not self.of_en_cours:
            selected_of_index = self.listbox_attente.curselection()
            if selected_of_index:
                selected_of = self.of_en_attente[selected_of_index[0]]
                self.erp_instance.passer_en_cours(selected_of, self.utilisateur.uid, self.utilisateur.password)
                self.Refresh_B_Cliked()

    def OF_Status_Doing_Wait_B_Cliked(self):
        #Changer le statut de l'ordre de fabrication: En cours vers Attente
        if self.of_en_cours:
            selected_of_index = self.listbox_cours.curselection()
            if selected_of_index:
                selected_of = self.of_en_cours[selected_of_index[0]]
                self.erp_instance.passer_en_attente(selected_of, self.utilisateur.uid, self.utilisateur.password)
                self.Refresh_B_Cliked()

    def OF_Status_Doing_Done_B_Cliked(self):
        #Changer le statut de l'ordre de fabrication: Attente vers En cours
        if self.of_en_cours:
            selected_of_index = self.listbox_cours.curselection()
            if selected_of_index:
                selected_of = self.of_en_cours[selected_of_index[0]]
                # Mettre à jour le statut de l'OF à "done" dans Odoo
                self.erp_instance.passer_en_fait(selected_of,self.utilisateur.uid,self.utilisateur.password)
                self.Refresh_B_Cliked()

    def OF_Quantities_B_Cliked(self):
        #Changer la quantité produite de l'OF en cours
        if self.of_en_cours:
            selected_of_index = self.listbox_cours.curselection()
            if selected_of_index:
                selected_of = self.of_en_cours[selected_of_index[0]]
                nouvelle_quantite_produite = self.entry_quantite_produite.get()
                # Vérifier si la saisie est un nombre valide en tant que float
                try:
                    nouvelle_quantite_produite = float(nouvelle_quantite_produite)
                except ValueError:
                    messagebox.showerror("Erreur", "Veuillez entrer une quantité produite valide (nombre).")
                    return
                # Mettre à jour la quantité produite dans Odoo
                self.erp_instance.modifier_quantite_en_cours(selected_of, nouvelle_quantite_produite,self.utilisateur.uid,self.utilisateur.password)
                # Actualiser la liste OF en cours
                selected_of['qty_producing'] = nouvelle_quantite_produite
                self.Refresh_B_Cliked()

    def Refresh_B_Cliked(self):
        #Actualiser l'affichage des OF
        self.of_en_attente = self.erp_instance.recuperer_of_en_attente(self.utilisateur.uid, self.utilisateur.password)
        self.of_en_cours = self.erp_instance.recuperer_of_en_cours(self.utilisateur.uid,self.utilisateur.password)
        self.actualiser_listbox()


