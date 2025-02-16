import turtle as t
from turtle import Screen

def niveaux_de_gris(n:int) -> None:
    avancement = 255/n
    screen = Screen()
    screen.colormode(255)
    for i in range(n):
        if i != 0:
            nb = int(0+avancement)
            t.fillcolor(nb, nb, nb)
            t.pencolor(nb, nb, nb)
            avancement = avancement + 255/n
        t.begin_fill()
        t.forward(20)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(100)
        t.end_fill()
        t.right(90)
        t.forward(20)

niveaux_de_gris(10)
t.exitonclick()