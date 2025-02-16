import tkinter as tk
import point

WIDTH = 400
HEIGHT = 400

window = tk.Tk()
window.title("Vers les L-systèmes - Partie 2")

canvas = tk.Canvas(window, width = WIDTH, height = HEIGHT, bg = 'ivory')
canvas.pack(padx = 10, pady = 10)

### Début de la partie à modifier ###

p1 = point.Point(100, 100)
p2 = point.Point(300, 100)
p3 = point.Point(300, 300)
p4 = point.Point(100, 300)
p = [p1,p2,p3,p4]
f = p2
for i in p:
    i.draw(canvas, 'red')
    i.drawLine(canvas, f, 'blue')
    if p.index(f)+1 == 4:
        f = p[0]
    else:
        f = p[p.index(f)+1]

### Fin de la partie à modifier ###

window.mainloop()