import turtle as t

t.penup()
t.goto(-300, 150)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()
t.fillcolor("red")
t.forward(400)
t.begin_fill()
for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()
t.goto(100, -150)
t.goto(-100, -150)

t.exitonclick()