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
        master.title("Page Production")
        self.label = tk.Label(self, text="Bienvenue sur la page Production")
        self.label.pack(pady=10)

        self.of_en_attente = self.erp_instance.recuperer_of_en_attente(self.utilisateur.uid, self.utilisateur.password)
        self.of_en_cours = self.erp_instance.recuperer_of_en_cours(self.utilisateur.uid,self.utilisateur.password)

        self.label_attente = tk.Label(master, text="OF en attente:")
        self.listbox_attente = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=100, font=("Helvetica", 8))

        for of in self.of_en_attente:
            self.listbox_attente.insert(tk.END, f"{of['name']} - {of['product_id'][1]} - "
                                                 f"Quantité à produire: {of['product_qty']} - Quantité produite: {of['qty_producing']}")

        self.label_cours = tk.Label(master, text="OF en cours:")
        self.listbox_cours = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=100, font=("Helvetica", 8))
        for of in self.of_en_cours:
            self.listbox_cours.insert(tk.END, f"{of['name']} - {of['product_id'][1]} - "
                                               f"Quantité à produire: {of['product_qty']} - Quantité produite: {of['qty_producing']}")

        self.entry_quantite_produite = tk.Entry(master)
        self.button_modifier_quantite = tk.Button(master, text="Modifier Quantité Produite", command=self.OF_Quantities_B_Cliked)



        self.button_actualiser = tk.Button(master, text="Actualiser", command=self.Refresh_B_Cliked)
        self.button_actualiser.grid(row=5, column=0, columnspan=4, pady=5)


        self.button_passer_en_cours = tk.Button(master, text="Passer en cours", command=self.OF_Status_Wait_Doing_B_Cliked)
        self.button_passer_en_attente = tk.Button(master, text="Passer en attente", command=self.OF_Status_Doing_Wait_B_Cliked)
        self.button_passer_fait = tk.Button(master, text="Passer à Fait", command=self.OF_Status_Doing_Done_B_Cliked)

        # Placement des widgets
        self.label_attente.grid(row=0, column=0, padx=10, pady=5)
        self.listbox_attente.grid(row=1, column=0, padx=10, pady=5)
        self.label_cours.grid(row=0, column=2, padx=10, pady=5)
        self.listbox_cours.grid(row=1, column=2, padx=10, pady=5)
        self.entry_quantite_produite.grid(row=4, column=2, padx=10, pady=5)
        self.button_modifier_quantite.grid(row=5, column=2, pady=5, padx= 15)
        self.button_passer_en_cours.grid(row=2, column=0, pady=5)
        self.button_passer_en_attente.grid(row=2, column=2, pady=5)
        self.button_passer_fait.grid(row=3, column=0, columnspan=4, pady=5)

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
        #Changer le status de l'ordre de fabrication: Attente vers En cours
         if not self.of_en_cours:
            selected_of_index = self.listbox_attente.curselection()
            if selected_of_index:
                selected_of = self.of_en_attente[selected_of_index[0]]
                self.erp_instance.passer_en_cours(selected_of, self.utilisateur.uid, self.utilisateur.password)
                self.Refresh_B_Cliked()
                
    def OF_Status_Doing_Wait_B_Cliked(self):
        #Changer le status de l'ordre de fabrication: En cours vers Attente
         if self.of_en_cours:
            selected_of_index = self.listbox_cours.curselection()
            if selected_of_index:
                selected_of = self.of_en_cours[selected_of_index[0]]
                self.erp_instance.passer_en_attente(selected_of, self.utilisateur.uid, self.utilisateur.password)
                self.Refresh_B_Cliked()

    def OF_Status_Doing_Done_B_Cliked(self):
        #Changer le status de l'ordre de fabrication: Attente vers En cours
        if self.of_en_cours:
            selected_of_index = self.listbox_cours.curselection()
            if selected_of_index:
                selected_of = self.of_en_cours[selected_of_index[0]]
                # Mettre à jour le statut de l'OF à "done" dans Odoo
                self.erp_instance.passer_en_fait(selected_of,self.utilisateur.uid,self.utilisateur.password)
                self.Refresh_B_Cliked()        
        pass
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
        pass 
        
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Fenêtre avec image en fond")

        # Charger l'image
        image = Image.open("Application/Image/HGABADCO MAQUETTE V2-2.png")
        photo = ImageTk.PhotoImage(image)

        # Créer un Canvas pour afficher l'image en fond
        canvas = tk.Canvas(root, width=image.width, height=image.height)
        canvas.pack()

        # Placer l'image sur le Canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)

        # Ajouter d'autres widgets ou fonctionnalités selon vos besoins
        label = tk.Label(root, text="Contenu de la fenêtre")
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()