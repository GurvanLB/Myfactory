import tkinter as tk
from PIL import Image, ImageTk
import base64
from tkinter import ttk
from io import BytesIO
from Image import *

class LogistiquePage(tk.Frame):
    def __init__(self, master, erp_instance, Utilisateur):
        tk.Frame.__init__(self, master)
        self.master = master
        self.erp_instance = erp_instance
        self.utilisateur = Utilisateur
        master.title("Page Logistique")



        # Charger et redimensionner l'image avec Pillow
        image_pil = Image.open("Application/Image/new interface-3V3.png")
        image_pil = image_pil.resize((1920, 1080), Image.LANCZOS)
        self.image_de_fond = ImageTk.PhotoImage(image_pil)

        # Créer un Canvas pour afficher l'image en fond
        self.canvas = tk.Canvas(self.master, width=self.image_de_fond.width(), height=self.image_de_fond.height())
        self.canvas.pack()

        # Afficher l'image en fond
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_de_fond)



        # Calculer les coordonnées pour centrer
        center_x = self.image_de_fond.width() // 2
        center_y = self.image_de_fond.height() // 2

        # Police
        bouton_font = ("Helvetica", 25, "bold")  # Ajuste la taille de la police des boutons
        titre_page_font = ("Helvetica", 45, "bold")  # Ajuste la taille de la police du titre de la page
        titre_font = ("Helvetica", 28, "bold")  # Ajuste la taille de la police des titres de zones
        list_font = ("Helvetica", 14) # Ajuste la taille de la police des listes


        # Céation des boutons
        self.refresh_button = tk.Button(self.master, text="ACTUALISER", command=self.bouton_actualiser, font=bouton_font, bg="#757575", activebackground="#929292", fg="white", activeforeground="white", bd=3)
        self.valider_livraison_button = tk.Button(self.master, text="VALIDER", command=self.bouton_valider, font=bouton_font, width=13, height=2, bg="#757575", activebackground="#929292", fg="white", activeforeground="white", bd=3)
        # Positionner les boutons à des coordonnées centrées sur le Canvas
        self.canvas.create_window(center_x + 0, center_y + 99, window=self.refresh_button, height=100, width=300)
        self.canvas.create_window(center_x + 0, center_y + 330, window=self.valider_livraison_button, height=100, width=300)

        # Création des labels
        self.label_titre_page = tk.Label(self.master, text="MENU LOGISTIQUE", font=titre_page_font, fg="white", bg="#006FC0")
        self.label_titre_inventaire = tk.Label(self.master, text="INVENTAIRE", font=titre_font, fg="white", bg="#006FC0")
        self.label_titre_livraison = tk.Label(self.master, text="LIVRAISON EN ATTENTE", font=titre_font, fg="white", bg="#006FC0")
        self.label_titre_reception = tk.Label(self.master, text="RECEPTION EN ATTENTE", font=titre_font, fg="white", bg="#006FC0")
        # Positionner les labels à des coordonnées spécifiques sur le Canvas
        self.canvas.create_window(center_x, center_y - 440, window=self.label_titre_page)
        self.canvas.create_window(center_x, center_y - 310, window=self.label_titre_inventaire)
        self.canvas.create_window(center_x + 510, center_y +80, window=self.label_titre_livraison)
        self.canvas.create_window(center_x - 510, center_y +80, window=self.label_titre_reception)

        # Créez des Treeviews à la place des Listbox
        self.reception_attente_treeview = ttk.Treeview(self.master, height=14, columns=('id','Nom', 'Date','partner_id'), show='headings', selectmode="browse")
        self.livraison_attente_treeview = ttk.Treeview(self.master, height=14, columns=('id','Nom', 'Date','partner_id'), show='headings', selectmode="browse")

        #Definition taille colonne
        self.reception_attente_treeview.column('id', width=50, anchor='center')
        self.reception_attente_treeview.column('Nom', width=100, anchor='center')  
        self.reception_attente_treeview.column('Date', width=100, anchor='center')
        self.reception_attente_treeview.column('partner_id', width=100, anchor='center')

        self.livraison_attente_treeview.column('id', width=50, anchor='center')
        self.livraison_attente_treeview.column('Nom', width=100, anchor='center')  
        self.livraison_attente_treeview.column('Date', width=100, anchor='center')
        self.livraison_attente_treeview.column('partner_id', width=100, anchor='center')
        # Configurez les colonnes pour les Treeviews
        self.reception_attente_treeview.heading('id', text='ID')
        self.reception_attente_treeview.heading('Nom', text='Nom')
        self.reception_attente_treeview.heading('Date', text='Date')
        self.reception_attente_treeview.heading('partner_id', text='Fournisseur')

        self.livraison_attente_treeview.heading('id', text='ID')
        self.livraison_attente_treeview.heading('Nom', text='Nom')
        self.livraison_attente_treeview.heading('Date', text='Date')
        self.livraison_attente_treeview.heading('partner_id', text='Client')
        # Positionnez les Treeviews à la place des Listbox
        self.canvas.create_window(center_x - 511, center_y + 245, window=self.reception_attente_treeview, height=260, width=637)
        self.canvas.create_window(center_x + 511, center_y + 245, window=self.livraison_attente_treeview, height=260, width=637)

        # ... (le reste de votre code reste inchangé)

        # Affichez les items des Treeviews
        self.actualiser_liste_expedition()

        # Conteneur pour les articles
        self.container_frame = tk.Frame(self.master, background="white")  
        self.container_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Positionner le container_frame au centre de la fenêtre
        self.container_frame.place(relx=0.5, rely=0.37, anchor="center")

        # Afficher les articles initiaux
        self.afficher_articles()
        
        
    def afficher_articles(self):
        # Récupérer les articles
        articles = self.erp_instance.obtenir_artcles_photo(self.utilisateur.uid, self.utilisateur.password)
        name_font = ("Helvetica", 16, "bold")
        stock_font = ("Helvetica", 14)
        modif_font = ("Helvetica", 14)
        button_font =("Helvetica", 14)
        # Boucle pour créer et afficher les articles avec champs de saisie et bouton
        for article in articles:
            frame_article = tk.Frame(self.container_frame, bg="white")
            frame_article.pack(side=tk.LEFT, padx=10)

            label_nom = tk.Label(frame_article, text=article['name'].upper(), justify='center',bg='white',font=name_font)
            label_nom.pack(side='top')

            # Décoder l'image en base 64
            image_data = base64.b64decode(article['image_1920'])

            # Convertir l'image en format Tkinter
            image = Image.open(BytesIO(image_data))
            image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label_image = tk.Label(frame_article, image=photo)
            label_image.image = photo  
            label_image.pack(side='top', pady=5, anchor='center')

            # Ajouter le stock en dessous de l'image
            label_stock = tk.Label(frame_article, text=f"Stock: {article['qty_available']}", justify='center',bg='white',font=stock_font)
            label_stock.pack(side='top')

            # Ajouter un champ de saisie pour le nouveau stock
            entry_nouveau_stock = tk.Entry(frame_article,font=modif_font, width=8,bd=2, justify="center")
            entry_nouveau_stock.pack(side='top', pady=5)

            # Ajouter un bouton pour modifier le stock
            button_modifier = tk.Button(frame_article,height=1,width=8, text="Modifier", font=button_font,
                                        command=lambda id=article['id'], entry=entry_nouveau_stock, label=label_stock:
                                        self.modifier_stock(id, entry, label))
            button_modifier.pack(side='top', pady=5)

    def actualiser_liste_expedition(self):
        # Rafraîchir les Treeviews
        self.livraison = self.erp_instance.obtenir_livraison_en_attente(self.utilisateur.uid, self.utilisateur.password)
        self.reception = self.erp_instance.obtenir_reception_en_attente(self.utilisateur.uid, self.utilisateur.password)

        self.reception_attente_treeview.delete(*self.reception_attente_treeview.get_children())
        self.livraison_attente_treeview.delete(*self.livraison_attente_treeview.get_children())

        for item in self.livraison:
            self.livraison_attente_treeview.insert("", tk.END, values=(item['id'], item['name'], item['date'], item['partner_id']))

        for item in self.reception:
            self.reception_attente_treeview.insert("", tk.END, values=(item['id'], item['name'], item['date'],item['partner_id']))




        pass

    def modifier_stock(self,id, entry_nouveau_stock, label_stock):
        print("Valeur saisie:", entry_nouveau_stock.get())

        stock_actuel = int(float(label_stock.cget("text").split(":")[1].strip()))
        nouveau_stock = int(entry_nouveau_stock.get())
        nouveau_stock_relatif = stock_actuel + nouveau_stock
        self.erp_instance.modifier_stock_article(id,nouveau_stock_relatif,self.utilisateur.uid, self.utilisateur.password)
        self.bouton_actualiser()
    
    """def bouton_valider_reception(self):
        # Obtenez l'élément sélectionné dans le Treeview
        selected_item = self.reception_attente_treeview.selection()
        if selected_item:
            item_id = self.reception_attente_treeview.item(selected_item, 'values')[0]
            self.erp_instance.passer_a_fait_expedition(item_id, self.utilisateur.uid, self.utilisateur.password)
            self.bouton_actualiser()
        else:
            print("Sélectionnez une réception avant de valider.")
    """
    def bouton_valider(self):
        selected_item_liv = self.livraison_attente_treeview.selection()
        if selected_item_liv:
            item_id = self.livraison_attente_treeview.item(selected_item_liv, 'values')[0]
            self.erp_instance.passer_a_fait_expedition(item_id, self.utilisateur.uid, self.utilisateur.password)

        selected_item_rec = self.reception_attente_treeview.selection()
        if selected_item_rec:
            item_id = self.reception_attente_treeview.item(selected_item_rec, 'values')[0]
            self.erp_instance.passer_a_fait_expedition(item_id, self.utilisateur.uid, self.utilisateur.password)
        else:
            print("Sélectionnez une réception avant de valider.")
        self.bouton_actualiser()

    def bouton_actualiser(self):
        for widget in self.container_frame.winfo_children():
            widget.destroy()
        self.actualiser_liste_expedition()
        self.afficher_articles()


