import tkinter as tk
from tkinter import ttk
import xmlrpc.client
from datetime import datetime

def get_odoo_data(server_url, db_name, username, password, model_name, domain=None, fields=None):
    common = xmlrpc.client.ServerProxy(f'{server_url}/xmlrpc/2/common')
    uid = common.authenticate(db_name, username, password, {})
    models = xmlrpc.client.ServerProxy(f'{server_url}/xmlrpc/2/object')

    if domain is None:
        domain = []

    if fields is None:
        fields = []

    records = models.execute_kw(db_name, uid, password, model_name, 'search_read', [domain], {'fields': fields})
    return records

def format_date(date_str):
    if date_str:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    return ''

# Interface graphique pour afficher les données des OF
class OFApp:
    def __init__(self, root, data, fields, title):
        self.root = root
        self.root.title(title)

        self.tableau = ttk.Treeview(self.root, columns=fields, show="headings")

        for field in fields:
            self.tableau.heading(field, text=field)
            self.tableau.column(field, width=100)

        for record in data:
            values = [record.get(field, '') for field in fields]
            values[3] = format_date(values[3])  # Formatage de la date de début prévue
            values[4] = format_date(values[4])  # Formatage de la date de fin prévue
            print("Values:", values)  # Ajout de cette ligne pour débugger
            self.tableau.insert("", "end", values=values)

        self.tableau.pack(pady=10)

if __name__ == "__main__":
    # Exemple d'utilisation pour récupérer les données des OF en attente
    server_url = 'http://localhost:8069'
    db_name = 'HGABadCo'
    username = 'Hugo'
    password = 'Hugo'

    # Récupérer les données des OF en attente (mrp.production)
    model_name_of_attente = 'mrp.production'
    fields_of_attente = ['name', 'product_id', 'state', 'date_planned_start', 'date_planned_finished', 'product_qty', 'qty_produced']
    domain_of_attente = [('state', '=', 'confirmed')]
    data_of_attente = get_odoo_data(server_url, db_name, username, password, model_name_of_attente, domain=domain_of_attente, fields=fields_of_attente)

    print("Data OF en attente:", data_of_attente)  # Ajout de cette ligne pour débugger

    # Récupérer les données des OF en cours (mrp.production)
    model_name_of_en_cours = 'mrp.production'
    fields_of_en_cours = ['name', 'product_id', 'state', 'date_planned_start', 'date_planned_finished', 'product_qty', 'qty_produced']
    domain_of_en_cours = [('state', '=', 'progress')]
    data_of_en_cours = get_odoo_data(server_url, db_name, username, password, model_name_of_en_cours, domain=domain_of_en_cours, fields=fields_of_en_cours)

    print("Data OF en cours:", data_of_en_cours)  # Ajout de cette ligne pour débugger

    root = tk.Tk()

    # Créer une instance de l'interface pour afficher les données des OF en attente
    of_attente_app = OFApp(root, data_of_attente, fields_of_attente, "OF en Attente")

    # Créer une instance de l'interface pour afficher les données des OF en cours
    of_en_cours_app = OFApp(root, data_of_en_cours, fields_of_en_cours, "OF en Cours")

    root.mainloop()

























'''class TableauApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tableaux avec Tkinter")

        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Arial', 12, 'bold'))

        self.tableau1 = ttk.Treeview(self.root, columns=('Nom', 'Âge', 'Ville'), show='headings')
        self.tableau1.heading('Nom', text='Nom')
        self.tableau1.heading('Âge', text='Âge')
        self.tableau1.heading('Ville', text='Ville')

        self.tableau1.column('Nom', width=100, anchor='center')
        self.tableau1.column('Âge', width=50, anchor='center')
        self.tableau1.column('Ville', width=100, anchor='center')

        self.tableau1.pack(pady=10, side=tk.LEFT)
        self.ajouter_entree(self.tableau1, 1, 'Alice', 25, 'Paris')
        self.ajouter_entree(self.tableau1, 2, 'Bob', 30, 'New York')
        self.ajouter_entree(self.tableau1, 3, 'Charlie', 22, 'London')

        self.tableau2 = ttk.Treeview(self.root, columns=('Nom', 'Âge', 'Ville'), show='headings')
        self.tableau2.heading('Nom', text='Nom')
        self.tableau2.heading('Âge', text='Âge')
        self.tableau2.heading('Ville', text='Ville')

        self.tableau2.column('Nom', width=100, anchor='center')
        self.tableau2.column('Âge', width=50, anchor='center')
        self.tableau2.column('Ville', width=100, anchor='center')

        self.tableau2.pack(pady=10, side=tk.LEFT)
        self.ajouter_entree(self.tableau2, 4, 'David', 28, 'Berlin')

        btn_basculer_1_2 = tk.Button(self.root, text="Basculer de 1 vers 2", command=self.basculer_1_2)
        btn_basculer_1_2.pack(pady=10)

        btn_basculer_2_1 = tk.Button(self.root, text="Basculer de 2 vers 1", command=self.basculer_2_1)
        btn_basculer_2_1.pack(pady=10)

    def ajouter_entree(self, tableau, identifiant, nom, age, ville):
        tableau.insert(parent='', index='end', iid=identifiant, text=identifiant,
                       values=(nom, age, ville))

    def basculer_1_2(self):
        selection = self.tableau1.selection()

        if selection:
            item = self.tableau1.item(selection, 'values')
            identifiant = selection[0]
            nom = item[0]
            age = item[1]
            ville = item[2]

            self.ajouter_entree(self.tableau2, identifiant, nom, age, ville)
            self.tableau1.delete(selection)

    def basculer_2_1(self):
        selection = self.tableau2.selection()

        if selection:
            item = self.tableau2.item(selection, 'values')
            identifiant = selection[0]
            nom = item[0]
            age = item[1]
            ville = item[2]

            self.ajouter_entree(self.tableau1, identifiant, nom, age, ville)
            self.tableau2.delete(selection)

if __name__ == "__main__":
    root = tk.Tk()
    app = TableauApp(root)
    root.mainloop()'''