import random as ran
import tkinter as tk
import tkinter.messagebox as ms

scoreAI = 0
scoreJ = 0

def ciseaux(): 
    global scoreAI, scoreJ
    choixIA = ran.randint(1,3)
    scoreJ, scoreAI = victoire(choixIA, 3, scoreAI, scoreJ)

def feuille(): 
    global scoreAI, scoreJ
    choixIA = ran.randint(1,3)
    scoreJ, scoreAI = victoire(choixIA, 2, scoreAI, scoreJ)

def pierre(): 
    global scoreAI, scoreJ
    choixIA = ran.randint(1,3)
    scoreJ, scoreAI = victoire(choixIA, 1, scoreAI, scoreJ)

def victoire(IA, J, sAI, sJ):
    global Jpoint_var, AIpoint_var
    if IA == J:
        pass
    if IA == 1:
        if J == 2:
            sJ += 1
            Jpoint_var.set(f"Point du Joueur : {sJ}")
        if J == 3:
            sAI += 1
            AIpoint_var.set(f"Point de l'IA : {sAI}")
    if IA == 2:
        if J == 1:
            sAI += 1
            AIpoint_var.set(f"Point de l'IA : {sAI}")
        if J == 3:
            sJ += 1
            Jpoint_var.set(f"Point du Joueur : {sJ}")
    if IA == 3:
        if J == 1:
            sJ += 1
            Jpoint_var.set(f"Point du Joueur : {sJ}")
        if J == 2:
            sAI += 1
            AIpoint_var.set(f"Point de l'IA : {sAI}")
    if sJ == 3:
        ms.showinfo("Resultat", "Bravo Joueur vous avez gagner")
        quitter()
    if sAI == 3:
        ms.showinfo("Resultat", "L'IA a gagner")
        quitter()
    return sJ, sAI

def quitter():
    main.quit()
    main.destroy()

main = tk.Tk()
main.title("Pierre feuille Ciseaux")
main.geometry("435x315")

Ciseaux = tk.PhotoImage(file='images/ciseaux.gif')
Feuille = tk.PhotoImage(file='images/feuille.gif')
Pierre = tk.PhotoImage(file='images/pierre.gif')

Jpoint_var = tk.StringVar()
AIpoint_var = tk.StringVar()

Ci_Button = tk.Button(main, image=Ciseaux, command=ciseaux, height=3, width=8)
Fe_Button = tk.Button(main, image=Feuille, command=feuille, height=3, width=8)
Pi_Button = tk.Button(main, image=Pierre, command=pierre, height=3, width=8)

Jpoint_Label = tk.Label(textvariable=Jpoint_var)
AIpoint_Label = tk.Label(textvariable=AIpoint_var)

Ci_Button.grid(column=2, row=0)
Fe_Button.grid(column=4, row=0)
Pi_Button.grid(column=6, row=0)

Jpoint_Label.grid(column=10, row=4)
AIpoint_Label.grid(column=10, row=5)

Jpoint_var.set("Point du Joueur : 0")
AIpoint_var.set("Point de l'IA : 0")

main.mainloop()