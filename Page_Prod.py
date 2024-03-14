import tkinter as tk
from tkinter import messagebox
from Odoo import *
from PIL import Image, ImageTk
from tkinter import ttk

class ProdPage(tk.Frame):
    def __init__(self, master, erp_instance, Utilisateur):
        tk.Frame.__init__(self, master)

        self.master = master
        self.erp_instance = erp_instance
        self.utilisateur = Utilisateur
        self.master.geometry("1920x1080")
        image_pil = Image.open("Application/Image/HGABADCO without button-2.png")
        image_pil = image_pil.resize((1920, 1080), Image.LANCZOS)
        self.image_de_fond = ImageTk.PhotoImage(image_pil)

        # Charger et redimensionner l'image de croix
        croix_pil = Image.open("Application/Image/Croixfondbleu.png")
        croix_pil = croix_pil.resize((40, 40), Image.LANCZOS)
        self.croix = ImageTk.PhotoImage(croix_pil)

        # Créer un Canvas pour afficher l'image en fond
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack()

        # Placer l'image sur le Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_de_fond)

        self.button_deconnexion = tk.Button(self.master, command=self.deconnexion, image=self.croix, borderwidth=0, highlightthickness=0)
        self.canvas.create_window(1850, 60, anchor=tk.NW, window=self.button_deconnexion)
        
        self.label_texte = tk.Label(self.canvas, text="MENU PRODUCTION", font=("Helvetica", 45, "bold"), fg="white", bg="#006FC0")
        self.label_texte_window = self.canvas.create_window(680, 75, anchor=tk.NW, window=self.label_texte)

        self.label_texte = tk.Label(self.canvas, text="ORDRE DE FABRICATION EN ATTENTE", font=("Helvetica", 28, "bold"), fg="white", bg="#006FC0", wraplength=500)
        self.label_texte_window = self.canvas.create_window(230, 210, anchor=tk.NW, window=self.label_texte)

        self.label_texte = tk.Label(self.canvas, text="ORDRE DE FABRICATION EN COURS", font=("Helvetica", 28, "bold"), fg="white", bg="#006FC0", wraplength=500)
        self.label_texte_window = self.canvas.create_window(1250, 382, anchor=tk.NW, window=self.label_texte)

        self.refresh_button = tk.Button(self.master, text="ACTUALISER", width=15, height=3, command=self.Refresh_B_Cliked, font=("Helvetica", 25, "bold"), fg="white", bg="#757575", activebackground="#929292", activeforeground="white", bd=3)
        self.refresh_button.place(x=1512, y=188)
       
        self.change_button = tk.Button(self.master, text="MODIFIER", width=9, height=3, command=self.OF_Quantities_B_Cliked, font=("Helvetica", 25, "bold"), fg="white", bg="#757575", activebackground="#929292", activeforeground="white", bd=3)
        self.change_button.place(x=1348, y=825)

        self.valider_button = tk.Button(self.master, text="VALIDER", width=9, height=3, command=self.OF_Status_Doing_Done_B_Cliked, font=("Helvetica", 25, "bold"), fg="white", bg="#757575", activebackground="#929292", activeforeground="white", bd=3)
        self.valider_button.place(x=1608, y=825)
        
        self.attenteencours_button = tk.Button(self.master, text=">", width=9, height=3, command=self.OF_Status_Wait_Doing_B_Cliked, font=("Helvetica", 32, "bold"), fg="white", bg="#757575", activebackground="#929292", activeforeground="white", bd=3)
        self.attenteencours_button.place(x=835, y=460)
       
        self.encoursattente_button = tk.Button(self.master, text="<", width=9, height=3, command=self.OF_Status_Doing_Wait_B_Cliked, font=("Helvetica", 32, "bold"), fg="white", bg="#757575", activebackground="#929292", activeforeground="white", bd=3)
        self.encoursattente_button.place(x=835, y=630)
        

        """self.label_texte = tk.Label(self.canvas, text="ORDRE DE FABRICATION EN COURS", font=("Helvetica", 28, "bold"), fg="white", bg="#006FC0", wraplength=500)
        self.label_texte_window = self.canvas.create_window(1250, 382, anchor=tk.NW, window=self.label_texte)"""
    def deconnexion(self):
        # Fonction à exécuter lors du clic sur le bouton de déconnexion
        # Ajoutez ici le code de déconnexion
        messagebox.showinfo("Déconnexion", "Vous êtes maintenant déconnecté.")
        self.master.destroy()
        
        self.label_attente = tk.Label(self, text="OF en attente:")
        self.label_attente.pack(pady=5)

        # Création de la Listbox pour les ordres en attente
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

       # self.entry_quantite_produite = tk.Entry(self)
        #self.entry_quantite_produite.pack(pady=5)

        #self.button_modifier_quantite = tk.Button(self, text="Modifier Quantité Produite", command=self.OF_Quantities_B_Cliked)
       # self.button_modifier_quantite.pack(pady=5, padx=15)

        #self.button_actualiser = tk.Button(self, text="Actualiser", command=self.Refresh_B_Cliked)
        #self.button_actualiser.pack(pady=5)

        #self.button_passer_en_cours = tk.Button(self, text="Passer en cours", command=self.OF_Status_Wait_Doing_B_Cliked)
        #self.button_passer_en_cours.pack(pady=5)

        #self.button_passer_en_attente = tk.Button(self, text="Passer en attente", command=self.OF_Status_Doing_Wait_B_Cliked)
        #self.button_passer_en_attente.pack(pady=5)

        #self.button_passer_fait = tk.Button(self, text="Passer à Fait", command=self.OF_Status_Doing_Done_B_Cliked)
        #self.button_passer_fait.pack(pady=5)

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


