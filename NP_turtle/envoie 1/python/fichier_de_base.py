import tkinter as tk

WIDTH = 600
HEIGHT = 400

window = tk.Tk()
window.title("Vers les L-systèmes - Partie ?")

canvas = tk.Canvas(window, width = WIDTH, height = HEIGHT, bg = 'ivory')
canvas.pack(padx = 10, pady = 10)

### Début de la partie à modifier ###

r = 25
A = (100-r, 100-r)
B = (10+r, 100+r)
canvas.create_line(A, B, width=3, fill="blue")

### Fin de la partie à modifier ###

window.mainloop()