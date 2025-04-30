import turtle as t

def damier(nl:int, nc:int) -> None:
    nl2 = nl/2
    line = 0
    for i in range(1, nc+1):
        if line == 0:
            for i in range(int(nl2)):
                t.begin_fill()
                for i in range(4):
                    t.forward(20)
                    t.right(90)
                t.end_fill()
                t.forward(40)
            t.right(90)
            t.forward(20)
            t.right(90)
            t.forward(20*nl)
            t.right(90)
            t.forward(40)
            t.right(90)
            line = 1
        else:
            t.forward(20)
            for i in range(int(nl2)):
                t.begin_fill()
                for i in range(4):
                    t.forward(20)
                    t.right(90)
                t.end_fill()
                if i+1 != int(nl2):
                    t.forward(40)
                else:
                    t.forward(20)
            t.penup()
            t.right(90)
            t.forward(20)
            t.right(90)
            t.forward(20)
            t.pendown()
            t.forward(20*nl)
            t.right(90)
            t.forward(40)
            t.right(90)
            line = 0
t.speed(100)
damier(10, 10)
t.exitonclick()