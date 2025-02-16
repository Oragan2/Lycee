import tkinter as tk
import sqlite3

def enregistrer():
    global nom, prenom, note
    n = nom.get()
    pr = prenom.get()
    no = note.get()
    nom.delete(0,1000)
    prenom.delete(0,1000)
    note.delete(0,1000)
    c.execute("""INSERT INTO bulletin VALUES (?,?,?)""",(n,pr,no))
    connexion.commit()

connexion = sqlite3.connect('basedenote.db')

c = connexion.cursor()
c.execute("""
          CREATE TABLE IF NOT EXISTS bulletin(
              nom TEXT,
              prenom TEXT,
              note INT);
          """)

root = tk.Tk()
root.grid()
tk.Label(root, text="Prenom : ").grid(column=0, row=0)

prenom = tk.Entry(root)
prenom.grid(column=1, row=0)

tk.Label(root, text="Nom : ").grid(column=0, row=1)

nom = tk.Entry(root)
nom.grid(column=1, row=1)

tk.Label(root, text="Note : ").grid(column=0, row=2)

note = tk.Entry(root)
note.grid(column=1, row=2)

tk.Button(root, text="Enregistrer", command=enregistrer).grid(column=0, row=4)

root.mainloop()

connexion.close()