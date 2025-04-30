import tkinter as tk

WIDTH = 400
HEIGHT = 400

window = tk.Tk()
window.title("Vers les L-systèmes - Partie 1")

canvas = tk.Canvas(window, width = WIDTH, height = HEIGHT, bg = 'ivory')
canvas.pack(padx = 10, pady = 10)

### Début de la partie à modifier ###
def carre(lg:int, origine:tuple, color='black', pcolor='black') -> None:
    A = (origine[0]-lg, origine[1]-lg)
    B = (origine[0]+lg, origine[1]+lg)
    canvas.create_rectangle(A,B, outline=color, width=3)
    for i in range(-lg, lg*2+1, lg*2):
        for j in range(-lg, lg*2+1, lg*2):
            canvas.create_oval((origine[0]+i+2,origine[0]+j+2),(origine[0]+i-2,origine[0]+j-2), outline=pcolor, width=5)
### Fin de la partie à modifier ###

carre(100, (200,200), 'blue', '')

window.mainloop()