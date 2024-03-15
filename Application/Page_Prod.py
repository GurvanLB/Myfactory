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
        image_pil = Image.open("Image/HGABADCO without button-2.png")
        image_pil = image_pil.resize((1920, 1080), Image.LANCZOS)
        self.image_de_fond = ImageTk.PhotoImage(image_pil)

        # Charger et redimensionner l'image de croix
        croix_pil = Image.open("Image/croix.png")
        croix_pil = croix_pil.resize((40, 40), Image.LANCZOS)
        self.croix = ImageTk.PhotoImage(croix_pil)

        # Créer un Canvas pour afficher l'image en fond
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack()

        # Placer l'image sur le Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_de_fond)

        self.button_deconnexion = tk.Button(self.master, command=self.deconnexion, image=self.croix, borderwidth=0, highlightthickness=0)
        self.canvas.create_window(1790, 75, anchor=tk.NW, window=self.button_deconnexion)
        
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
        self.valider_button.place(x=1625, y=825)
        
        self.attenteencours_button = tk.Button(self.master, text=">", width=9, height=3, command=self.OF_Status_Wait_Doing_B_Cliked, font=("Helvetica", 32, "bold"), fg="white", bg="#757575", activebackground="#929292", activeforeground="white", bd=3)
        self.attenteencours_button.place(x=835, y=460)
       
        self.encoursattente_button = tk.Button(self.master, text="<", width=9, height=3, command=self.OF_Status_Doing_Wait_B_Cliked, font=("Helvetica", 32, "bold"), fg="white", bg="#757575", activebackground="#929292", activeforeground="white", bd=3)
        self.encoursattente_button.place(x=835, y=630)
        
        self.entry_quantite_produite = tk.Entry(self.master, width=10, font=("Helvetica", 28), bg="#757575", fg="white", bd=3)
        self.entry_quantite_produite.place(x=1110, y=860)

            
        self.of_en_attente = self.erp_instance.recuperer_of_en_attente(self.utilisateur.uid, self.utilisateur.password)
        self.of_en_cours = self.erp_instance.recuperer_of_en_cours(self.utilisateur.uid,self.utilisateur.password)

        self.label_attente = tk.Label(master, text="OF en attente:")
        self.tree_attente = ttk.Treeview(master, selectmode="browse", columns=("Product", "Qty to Produce", "Qty Produced"))
        self.tree_attente.configure(height=29)
        self.tree_attente.column("#0", width=220,anchor= "center")  # Première colonne
        self.tree_attente.column("Product", width=175,anchor= "center")  # Deuxième colonne
        self.tree_attente.column("Qty to Produce", width=175,anchor= "center")  # Troisième colonne
        self.tree_attente.column("Qty Produced", width=150,anchor= "center")  # Quatrième colonne
        self.tree_attente.heading("#0", text="Ordre de fabrication")
        self.tree_attente.heading("Product", text="Article")
        self.tree_attente.heading("Qty to Produce", text="Quantité à produire")
        self.tree_attente.heading("Qty Produced", text="Quantité produite")
        self.tree_attente.place(x=92, y=298)
        for of in self.of_en_attente:
            self.tree_attente.insert("", tk.END, text=of['name'], values=(of['product_id'][1], of['product_qty'], of['qty_producing']))

        self.label_cours = tk.Label(master, text="OF en cours:")
        self.tree_cours = ttk.Treeview(master, selectmode="browse", columns=("Product", "Qty to Produce", "Qty Produced"))
        self.tree_cours.configure(height=15)
        self.tree_cours.column("#0", width=220, anchor= "center")  # Première colonne
        self.tree_cours.column("Product", width=175,anchor= "center")  # Deuxième colonne
        self.tree_cours.column("Qty to Produce", width=175,anchor= "center")  # Troisième colonne
        self.tree_cours.column("Qty Produced", width=150,anchor= "center")  # Quatrième colonne
        self.tree_cours.heading("#0", text="Ordre de fabrication")
        self.tree_cours.heading("Product", text="Article")
        self.tree_cours.heading("Qty to Produce", text="Quantité à produire")
        self.tree_cours.heading("Qty Produced", text="Quantité produite")
        self.tree_cours.place(x=1108, y=470)
        for of in self.of_en_cours:
            self.tree_cours.insert("", tk.END, text=of['name'], values=(of['product_id'][1], of['product_qty'], of['qty_producing']))

    def deconnexion(self):
        # Fonction à exécuter lors du clic sur le bouton de déconnexion
        # Ajoutez ici le code de déconnexion
        messagebox.showinfo("Déconnexion", "Vous êtes maintenant déconnecté.")
        self.master.destroy()

    def actualiser_listbox(self):
        # Effacer et réinsérer les éléments dans les listbox
        for of in self.of_en_attente:
            self.tree_attente.insert("", tk.END, text=of['name'], values=(of['product_id'][1], of['product_qty'], of['qty_producing']))

        for of in self.of_en_cours:
            self.tree_cours.insert("", tk.END, text=of['name'], values=(of['product_id'][1], of['product_qty'], of['qty_producing']))

    def OF_Status_Wait_Doing_B_Cliked(self):
        # Changer le statut de l'ordre de fabrication: Attente vers En cours
        selected_item = self.tree_attente.focus()  # Récupérer l'élément sélectionné dans le Treeview
        if selected_item:
            selected_of = self.tree_attente.item(selected_item)['text']  # Récupérer le nom de l'OF sélectionné
            for of in self.of_en_attente:
                if of['name'] == selected_of:
                    self.erp_instance.passer_en_cours(of, self.utilisateur.uid, self.utilisateur.password)
                    self.Refresh_B_Cliked()
                    return

    def OF_Status_Doing_Wait_B_Cliked(self):
        # Changer le statut de l'ordre de fabrication: En cours vers Attente
        selected_item = self.tree_cours.focus()  # Récupérer l'élément sélectionné dans le Treeview
        if selected_item:
            selected_of = self.tree_cours.item(selected_item)['text']  # Récupérer le nom de l'OF sélectionné
            for of in self.of_en_cours:
                if of['name'] == selected_of:
                    self.erp_instance.passer_en_attente(of, self.utilisateur.uid, self.utilisateur.password)
                    self.Refresh_B_Cliked()
                    return

    def OF_Status_Doing_Done_B_Cliked(self):
        # Changer le statut de l'ordre de fabrication: En cours vers Fait
        selected_item = self.tree_cours.focus()  # Récupérer l'élément sélectionné dans le Treeview
        if selected_item:
            selected_of = self.tree_cours.item(selected_item)['text']  # Récupérer le nom de l'OF sélectionné
            for of in self.of_en_cours:
                if of['name'] == selected_of:
                    self.erp_instance.passer_en_fait(of, self.utilisateur.uid, self.utilisateur.password)
                    self.Refresh_B_Cliked()
                    return

    def OF_Quantities_B_Cliked(self):
        # Changer la quantité produite de l'OF en cours
        selected_item = self.tree_cours.focus()  # Récupérer l'élément sélectionné dans le Treeview
        if selected_item:
            selected_of = self.tree_cours.item(selected_item)['text']  # Récupérer le nom de l'OF sélectionné
            for of in self.of_en_cours:
                if of['name'] == selected_of:
                    nouvelle_quantite_produite = self.entry_quantite_produite.get()

                    # Vérifier si la saisie est un nombre valide en tant que float
                    try:
                        nouvelle_quantite_produite = float(nouvelle_quantite_produite)
                    except ValueError:
                        messagebox.showerror("Erreur", "Veuillez entrer une quantité produite valide (nombre).")
                        return
                    # Mettre à jour la quantité produite dans Odoo
                    self.erp_instance.modifier_quantite_en_cours(of, nouvelle_quantite_produite, self.utilisateur.uid, self.utilisateur.password)
                    # Actualiser la liste OF en cours
                    of['qty_producing'] = nouvelle_quantite_produite
                    self.Refresh_B_Cliked()
                    self.entry_quantite_produite.delete(0, 'end')
                    return

    def Refresh_B_Cliked(self):
        #Actualiser l'affichage des OF
        self.of_en_attente = self.erp_instance.recuperer_of_en_attente(self.utilisateur.uid, self.utilisateur.password)
        self.of_en_cours = self.erp_instance.recuperer_of_en_cours(self.utilisateur.uid,self.utilisateur.password)
        self.tree_attente.delete(*self.tree_attente.get_children())
        self.tree_cours.delete(*self.tree_cours.get_children())
        self.actualiser_listbox()
