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
t = [(200, 0),
(0, 200),
(-200, 0),]
p =  [p1]

for i in t:
    p.append(p[t.index(i)].translate(i[0],i[1]))

for i in p:
    if p.index(i) == 3:
        i.drawLine(canvas, p[0], 'blue')
        i.draw(canvas, 'red')
        p[0].draw(canvas, 'red')
    else:
        i.drawLine(canvas, p[p.index(i)+1], 'blue')
        i.draw(canvas, 'red')

### Fin de la partie à modifier ###

window.mainloop()