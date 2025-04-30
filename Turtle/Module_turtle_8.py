<<<<<<< HEAD
import turtle as t
import random as ran

def face_1() -> None:
    t.penup()
    t.home()
    t.right(90)
    t.forward(15)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.circle(15, 360)
    t.end_fill()

def face_2() -> None:
    for i in range(2):
        t.penup()
        if i == 0:
            t.goto(35, 40)
        elif i == 1:
            t.goto(-35, -30)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.begin_fill()
        t.circle(15, 360)
        t.end_fill()

def face_3() -> None:
    face_2()
    face_1()

def face_4() -> None:
    for i in range(4):
        t.penup()
        if i == 0:
            t.goto(35, 40)
        elif i == 1:
            t.goto(-35, -30)
        elif i == 2:
            t.goto(-35, 40)
        else:
            t.goto(35, -30)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.begin_fill()
        t.circle(15, 360)
        t.end_fill()

def face_5() -> None:
    face_4()
    face_1()

def face_6() -> None:
    for i in range(6):
        t.penup()
        if i == 0:
            t.goto(35, 40)
        elif i == 1:
            t.goto(-35, -30)
        elif i == 2:
            t.goto(-35, 40)
        elif i == 3:
            t.goto(35, -30)
        elif i == 4:
            t.goto(-35, 5)
        elif i == 5:
            t.goto(35, 5)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.begin_fill()
        t.circle(15, 360)
        t.end_fill()

t.speed(5)
face = ran.randint(1, 6)
t.penup()
t.goto(-60, 60)
t.pendown()
for i in range(4):
    t.forward(120)
    t.right(90)
if face == 1:
    face_1()
elif face == 2:
    face_2()
elif face == 3:
    face_3()
elif face == 4:
    face_4()
elif face == 5:
    face_5()
else:
    face_6()

=======
import turtle as t
import random as ran

def face_1() -> None:
    t.penup()
    t.home()
    t.right(90)
    t.forward(15)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.circle(15, 360)
    t.end_fill()

def face_2() -> None:
    for i in range(2):
        t.penup()
        if i == 0:
            t.goto(35, 40)
        elif i == 1:
            t.goto(-35, -30)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.begin_fill()
        t.circle(15, 360)
        t.end_fill()

def face_3() -> None:
    face_2()
    face_1()

def face_4() -> None:
    for i in range(4):
        t.penup()
        if i == 0:
            t.goto(35, 40)
        elif i == 1:
            t.goto(-35, -30)
        elif i == 2:
            t.goto(-35, 40)
        else:
            t.goto(35, -30)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.begin_fill()
        t.circle(15, 360)
        t.end_fill()

def face_5() -> None:
    face_4()
    face_1()

def face_6() -> None:
    for i in range(6):
        t.penup()
        if i == 0:
            t.goto(35, 40)
        elif i == 1:
            t.goto(-35, -30)
        elif i == 2:
            t.goto(-35, 40)
        elif i == 3:
            t.goto(35, -30)
        elif i == 4:
            t.goto(-35, 5)
        elif i == 5:
            t.goto(35, 5)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.begin_fill()
        t.circle(15, 360)
        t.end_fill()

t.speed(5)
face = ran.randint(1, 6)
t.penup()
t.goto(-60, 60)
t.pendown()
for i in range(4):
    t.forward(120)
    t.right(90)
if face == 1:
    face_1()
elif face == 2:
    face_2()
elif face == 3:
    face_3()
elif face == 4:
    face_4()
elif face == 5:
    face_5()
else:
    face_6()

>>>>>>> fc9acc5024275baf41e857549168f97a380f1a0b
t.exitonclick()