import turtle as t

def triangleH(cote:int) -> None:
    for i in range(3):
        t.left(120)
        t.forward(cote)

def triangleB(cote:int) -> None:
    for i in range(3):
        t.forward(cote)
        t.right(120)
        
t.speed(20)
t.penup()
t.goto(-200, 0)
t.pendown()
for i in range(5):
    triangleH(60)
    t.penup()
    t.left(90)
    t.forward(51.96)
    t.right(90)
    t.pendown()
    triangleB(60)
    t.penup()
    t.forward(120)
    t.right(90)
    t.forward(51.96)
    t.left(90)
    t.pendown()
t.exitonclick()