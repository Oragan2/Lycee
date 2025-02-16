import tkinter as tk
import sqlite3

def lecture():
    global commande
    c.execute(commande.get())
    Info.set(c.fetchall())

connexion = sqlite3.connect('basedenote.db')

c = connexion.cursor()

root = tk.Tk()
root.grid()

Info = tk.StringVar()

tk.Label(root, text="Votre commande").grid(column=0,row=0)
commande = tk.Entry(root)
commande.grid(column=1,row=0)

tk.Button(root, text="Faire la commande", command=lecture).grid(column=0,row=1)

tk.Label(root, textvariable=Info).grid(column=0,row=2)

root.mainloop()

connexion.close()