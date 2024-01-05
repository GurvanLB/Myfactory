from pathlib import Path
import tkinter as tk
root = tk.Tk()
root.mainloop()


#----------DEBUT------------

class App(tk.TK): 
    """ Application GUI in TKinter"""
    def __init__(self) : 
        """ Application constructor (heritage=Tk object)"""
        super().__init__()

if __name__ == "__main__":
    myApp = App()
    myApp.mainloop()