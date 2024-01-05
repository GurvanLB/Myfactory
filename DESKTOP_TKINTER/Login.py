import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk

class App(ThemedTk):
    def __init__(self):
        super().__init__()

        self.set_theme("plastik")

        self.title("Login")
        self.geometry("600x400")

        self.login_page = LoginPage(self)
        self.production_page = ProductionPage(self)
        self.logistique_page = LogistiquePage(self)

        self.show_login_page()

    def show_login_page(self):
        self.production_page.pack_forget()
        self.logistique_page.pack_forget()
        self.title("Login")
        self.login_page.clear_fields()
        self.login_page.pack()

    def show_production_page(self, username):
        self.login_page.pack_forget()
        self.logistique_page.pack_forget()
        self.title("Production")
        self.production_page.update_label(username)
        self.production_page.pack()

    def show_logistique_page(self, username):
        self.login_page.pack_forget()
        self.production_page.pack_forget()
        self.title("Logistique")
        self.logistique_page.update_label(username)
        self.logistique_page.pack()

    def on_logout(self):
        self.production_page.pack_forget()
        self.logistique_page.pack_forget()
        self.show_login_page()

class BasePage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

    def on_btn_logout(self):
        self.master.on_logout()

class LoginPage(BasePage):
    def __init__(self, master):
        super().__init__(master)

        self.user = tk.StringVar()
        self.pwd = tk.StringVar()

        self.style = ttk.Style()
        self.style.configure("TLabel", padding=5)
        self.style.configure("TButton", padding=(5, 5))

        lbl_user = ttk.Label(self, text="Utilisateur", font=("Arial", 12))
        lbl_user.grid(row=0, column=0, sticky="e")

        ent_user = ttk.Entry(self, textvariable=self.user, font=("Arial", 12))
        ent_user.grid(row=0, column=1, pady=5, sticky="w")

        lbl_pwd = ttk.Label(self, text="Mot de passe", font=("Arial", 12))
        lbl_pwd.grid(row=1, column=0, sticky="e")

        ent_pwd = ttk.Entry(self, textvariable=self.pwd, show="*", font=("Arial", 12))
        ent_pwd.grid(row=1, column=1, pady=5, sticky="w")

        btn_login = ttk.Button(self, text="Connexion", command=self.on_btn_login, style="TButton")
        btn_login.grid(row=2, column=0, columnspan=2, pady=10)

    def on_btn_login(self):
        username = self.user.get()
        password = self.pwd.get()

        if username == "production" and password == "prod":
            self.master.show_production_page(username)
        elif username == "logistique" and password == "log":
            self.master.show_logistique_page(username)
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

    def clear_fields(self):
        self.user.set("")
        self.pwd.set("")

class ProductionPage(BasePage):
    def __init__(self, master):
        super().__init__(master)

        self.label = ttk.Label(self, text="", font=("Arial", 14, "bold"))
        self.label.grid(row=0, column=0, pady=10)

        btn_logout = ttk.Button(self, text="Déconnexion", command=self.on_btn_logout, style="TButton")
        btn_logout.grid(row=1, column=0, pady=10)

    def update_label(self, username):
        self.label["text"] = f'Bienvenue sur la page de production, {username}'

class LogistiquePage(BasePage):
    def __init__(self, master):
        super().__init__(master)

        self.label = ttk.Label(self, text="", font=("Arial", 14, "bold"))
        self.label.grid(row=0, column=0, pady=10)

        btn_logout = ttk.Button(self, text="Déconnexion", command=self.on_btn_logout, style="TButton")
        btn_logout.grid(row=1, column=0, pady=10)

    def update_label(self, username):
        self.label["text"] = f'Bienvenue sur la page logistique, {username}'

if __name__ == "__main__":
    app = App()
    app.mainloop()