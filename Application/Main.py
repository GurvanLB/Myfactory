from  Page_Login import LoginPage
from  Odoo import ErpOdoo
import tkinter as tk

root = tk.Tk()
root.geometry('1280x720')
erp_instance = ErpOdoo()
login_page = LoginPage(root, erp_instance)

# Lancement de la boucle principale
root.mainloop()