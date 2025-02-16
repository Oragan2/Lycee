import turtle as t

def triangle_rect():
    t.pensize(1)
    t.begin_fill()
    t.left(135)
    t.forward(162)
    t.left(165)
    t.forward(134)
    t.left(110)
    t.forward(162)
    t.right(165)
    t.forward(134)
    t.end_fill()

def tri_force():
    t.fillcolor("grey")
    t.begin_fill()
    for i in range(3):
        t.forward(150)
        t.left(120)
    t.end_fill()
    t.fillcolor("white")
    t.forward(75)
    t.left(60)
    t.begin_fill()
    for i in range(3):
        t.forward(75)
        t.left(120)
    t.end_fill()

def boite_croix():
    t.penup()
    t.forward(50)
    t.right(90)
    t.pendown()
    t.begin_fill()
    t.forward(50)
    for i in range(3):
        t.right(90)
        t.forward(100)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.right(90)
    t.forward(0.45*50)
    t.pensize(3)
    t.color("white")
    t.forward(1.1*50)
    t.goto(345, 50)
    t.left(90)
    t.backward(1.1*50/2)
    t.forward(1.1*50)

triangle_rect()
t.penup()
t.home()
t.forward(100)
t.pendown()
tri_force()
t.penup()
t.home()
t.goto(345, 50)
t.pendown()
t.fillcolor("black")
boite_croix()
t.hideturtle()

t.exitonclick()