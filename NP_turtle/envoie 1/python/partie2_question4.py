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
p2 = p1.translate(200, 0)
p3 = p2.translate(0, 200)
p4 = p3.translate(-200, 0)

p1.drawLine(canvas, p2, "blue")
p2.drawLine(canvas, p3, "blue")
p3.drawLine(canvas, p4, "blue")
p4.drawLine(canvas, p1, "blue")

p1.draw(canvas, 'red')
p2.draw(canvas, 'red')
p3.draw(canvas, 'red')
p4.draw(canvas, 'red')

### Fin de la partie à modifier ###

window.mainloop()