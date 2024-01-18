import tkinter as tk
from PIL import Image, ImageTk
import base64
from io import BytesIO


class LogistiquePage(tk.Frame):
    def __init__(self, master, erp_instance, Utilisateur):
        tk.Frame.__init__(self, master)
        self.master = master
        self.erp_instance = erp_instance
        self.utilisateur = Utilisateur

        master.title("Page Logistique")

        # Ajouter un Canvas en haut de la fenêtre
        canvas = tk.Canvas(self, bg='blue', height=30)
        canvas.pack(fill='x')

        # Ajouter le texte "Inventaire" au Canvas, centré horizontalement
        canvas_width = canvas.winfo_reqwidth()
        text_id = canvas.create_text(canvas_width / 2, 15, anchor='center', text="Inventaire", fill='white', font=('Helvetica', 14, 'bold'))

        # Conteneur pour les articles
        self.container_frame = tk.Frame(self)
        self.container_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Afficher les articles initiaux
        self.afficher_articles()

        # Ajuster les coordonnées du texte pour le centrer sur le rectangle bleu
        bbox = canvas.bbox(text_id)
        text_width = bbox[2] - bbox[0]
        canvas.move(text_id, (canvas_width - text_width) / 2 - bbox[0], 0)

        # Liste des réceptions en attente
        self.reception_attente_listbox = tk.Listbox(self, height=10, width=50)
        self.reception_attente_listbox.pack(side='left', padx=10, pady=10)

        # Liste des livraisons en attente
        self.livraison_attente_listbox = tk.Listbox(self, height=10, width=50)
        self.livraison_attente_listbox.pack(side='left', padx=10, pady=10)
        self.actualiser_liste_expedition()
        # Bouton pour rafraîchir les listes
        refresh_list_button = tk.Button(self, text="Actualiser", command=self.bouton_actualiser)
        refresh_list_button.pack(side='left', padx=10, pady=10)

        # Ajout bouton Valider 
        valider_reception_button = tk.Button(self, text="Valider Réception", command=self.bouton_valider_reception)
        valider_reception_button.pack(side='left', padx=10, pady=10)

        # Bouton pour valider la livraison sélectionnée
        valider_livraison_button = tk.Button(self, text="Valider Livraison", command=self.bouton_valider_livraison)
        valider_livraison_button.pack(side='left', padx=10, pady=10)

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
        self.reception_attente_listbox.delete(0,tk.END)
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
