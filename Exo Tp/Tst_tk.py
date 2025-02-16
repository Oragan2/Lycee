import tkinter as tk

ma_fenetre = tk.Tk()
ma_fenetre.title("Echeque chinoise linéaire")
ma_fenetre.geometry("1024x576")

def quitter():
    ma_fenetre.quit()
    ma_fenetre.destroy()

ma_fenetre.mainloop()