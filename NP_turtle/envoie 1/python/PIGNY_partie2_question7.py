import tkinter as tk
import point

WIDTH = 400
HEIGHT = 400

window = tk.Tk()
window.title("Vers les L-systèmes - Partie 2")

canvas = tk.Canvas(window, width = WIDTH, height = HEIGHT, bg = 'ivory')
canvas.pack(padx = 10, pady = 10)

### Début de la partie à modifier ###

o = point.Point(200,200)
p = [point.Point(50, 200)]
for i in p:
    pt = i.rotate(36, o)
    p.append(pt)
    if len(p) == 10:
        break

for i in p:
    if p.index(i) == 9:
        i.drawLine(canvas, p[0], 'black', 7)
    else:
        i.drawLine(canvas, p[p.index(i)+1], 'black', 7)
    i.drawLine(canvas, o, 'blue', 5)

for i in p:
    i.draw(canvas, 'red', 7)
o.draw(canvas, 'orange', 30)

### Fin de la partie à modifier ###

window.mainloop()