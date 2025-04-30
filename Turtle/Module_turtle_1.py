import turtle as t

t.penup()
t.goto(-200, 60)
t.pendown()

for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(90)
    t.right(90)

t.penup()
t.goto(50, 75)
t.pendown()

for i in range(6):
    t.forward(80)
    t.right(60)
    
t.penup()
t.goto(250, -75)
t.pendown()

for i in range(3):
    t.left(60)
    t.forward(180)
    t.left(120)
    t.penup()
    t.forward(90)
    t.pendown()
    t.left(60)
    
t.exitonclick()