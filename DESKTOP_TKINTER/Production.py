import tkinter as tk
from tkinter import ttk

class TableauApp:
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
    root.mainloop()