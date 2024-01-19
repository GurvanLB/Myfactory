import tkinter as tk
from PIL import Image, ImageTk
import base64
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
        image_pil = Image.open("Application/Image/HGABADCO without button-3.png")
        image_pil = image_pil.resize((1920, 1080), Image.ANTIALIAS)
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
        self.valider_reception_button = tk.Button(self.master, text="VALIDER", command=self.bouton_valider_reception, font=bouton_font,  width=13, height=3, bg="#757575", activebackground="#929292", fg="white", activeforeground="white", bd=3)
        self.valider_livraison_button = tk.Button(self.master, text="VALIDER", command=self.bouton_valider_livraison, font=bouton_font, width=13, height=3, bg="#757575", activebackground="#929292", fg="white", activeforeground="white", bd=3)
        # Positionner les boutons à des coordonnées centrées sur le Canvas
        self.canvas.create_window(center_x + 692, center_y + 92, window=self.refresh_button, height=100, width=300)
        self.canvas.create_window(center_x - 555, center_y + 425, window=self.valider_reception_button)
        self.canvas.create_window(center_x + 190, center_y + 425, window=self.valider_livraison_button)

        # Création des labels
        self.label_titre_page = tk.Label(self.master, text="MENU LOGISTIQUE", font=titre_page_font, fg="white", bg="#006FC0")
        self.label_titre_inventaire = tk.Label(self.master, text="INVENTAIRE", font=titre_font, fg="white", bg="#006FC0")
        self.label_titre_livraison = tk.Label(self.master, text="LIVRAISON EN ATTENTE", font=titre_font, fg="white", bg="#006FC0")
        self.label_titre_reception = tk.Label(self.master, text="RECEPTION EN ATTENTE", font=titre_font, fg="white", bg="#006FC0")
        # Positionner les labels à des coordonnées spécifiques sur le Canvas
        self.canvas.create_window(center_x, center_y - 435, window=self.label_titre_page)
        self.canvas.create_window(center_x, center_y - 310, window=self.label_titre_inventaire)
        self.canvas.create_window(center_x + 190, center_y - 20, window=self.label_titre_livraison)
        self.canvas.create_window(center_x - 555, center_y - 20, window=self.label_titre_reception)

        # Listes des réceptions et des livraisons en attente
        self.reception_attente_listbox = tk.Listbox(self.master, height=14, width=63, background="white", bd=3, font=list_font, selectforeground="#ffffff")
        self.livraison_attente_listbox = tk.Listbox(self.master, background="white", bd=3, font=list_font, selectforeground="#ffffff", )
        # Positionnement des listes
        self.canvas.create_window(center_x - 554, center_y + 180, window=self.reception_attente_listbox, height=300, width=640)
        self.canvas.create_window(center_x + 190, center_y + 180, window=self.livraison_attente_listbox, height=300, width=640)
        # Affichage des items des listes
        self.actualiser_liste_expedition()


        # Conteneur pour les articles
        self.container_frame = tk.Frame(self.master, background="grey")
        self.canvas.create_window(center_x, center_y - 190, window=self.container_frame, width=1660,height=250)

        
        # Afficher les articles initiaux
        self.afficher_articles()
        
        
        

        

        


    def afficher_articles(self):
        # Récupérer les articles
        articles = self.erp_instance.obtenir_artcles_photo(self.utilisateur.uid, self.utilisateur.password)

        # Boucle pour créer et afficher les articles avec champs de saisie et bouton
        for article in articles:
            frame_article = tk.Frame(self.container_frame)
            frame_article.pack(side=tk.LEFT, padx=10)

            label_nom = tk.Label(frame_article, text=article['name'], justify='center')
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
            label_stock = tk.Label(frame_article, text=f"Stock: {article['qty_available']}", justify='center')
            label_stock.pack(side='top')

            # Ajouter un champ de saisie pour le nouveau stock
            entry_nouveau_stock = tk.Entry(frame_article, width=10)
            entry_nouveau_stock.pack(side='top', pady=5)

            # Ajouter un bouton pour modifier le stock
            button_modifier = tk.Button(frame_article, text="Modifier Stock",
                                        command=lambda id=article['id'], entry=entry_nouveau_stock, label=label_stock:
                                        self.modifier_stock(id, entry, label))
            button_modifier.pack(side='top', pady=5)

    def actualiser_liste_expedition(self):

        # Rafraîchir les listes
        self.livraison = self.erp_instance.obtenir_livraison_en_attente(self.utilisateur.uid,self.utilisateur.password)
        self.reception = self.erp_instance.obtenir_reception_en_attente(self.utilisateur.uid, self.utilisateur.password)
        self.livraison_attente_listbox.delete(0, tk.END)
        self.reception_attente_listbox.delete(0, tk.END)
        for item in self.livraison:
           self.livraison_attente_listbox.insert(tk.END, f"Livraison {item['name']} - Date: {item['date']}")
        for item in self.reception:
            self.reception_attente_listbox.insert(tk.END, f"Réception {item['name']} - Date: {item['date']}")


        pass

    def modifier_stock(self,id, entry_nouveau_stock, label_stock):
        print("Valeur saisie:", entry_nouveau_stock.get())

        stock_actuel = int(float(label_stock.cget("text").split(":")[1].strip()))
        nouveau_stock = int(entry_nouveau_stock.get())
        nouveau_stock_relatif = stock_actuel + nouveau_stock
        self.erp_instance.modifier_stock_article(id,nouveau_stock_relatif,self.utilisateur.uid, self.utilisateur.password)
    
    def bouton_valider_reception(self):
        # Obtenez l'élément sélectionné dans la Listbox
        selected_item = self.reception_attente_listbox.curselection()
        if selected_item:
            item_index = selected_item[0]
            reception_id = self.reception[item_index]['id']
            self.erp_instance.passer_a_fait_expedition(reception_id, self.utilisateur.uid, self.utilisateur.password)
        else:
            print("Sélectionnez une réception avant de valider.")

    def bouton_valider_livraison(self):
        selected_item = self.livraison_attente_listbox.curselection()
        if selected_item:
            item_index = selected_item[0]
            livraison_id = self.livraison[item_index]['id']
            self.erp_instance.passer_a_fait_expedition(livraison_id, self.utilisateur.uid, self.utilisateur.password)
        else:
            print("Sélectionnez une réception avant de valider.")
        pass

    def bouton_actualiser(self):
        for widget in self.container_frame.winfo_children():
            widget.destroy()
        self.actualiser_liste_expedition()
        self.afficher_articles()


