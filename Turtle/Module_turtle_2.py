import turtle as t



def print_n():
    """Desinne un N pour écrire NSI"""    
    t.goto(0,50)
    t.goto(10,50)
    t.goto(20,20)
    t.goto(20,50)
    t.goto(30,50)
    t.goto(30,0)
    t.goto(20,0)
    t.goto(10,30)
    t.goto(10,0)
    t.goto(0,0)
        
def print_s():
    """Desinne un S pour écrire NSI"""
    t.goto(70,0)
    t.goto(70,30)
    t.goto(50,30)
    t.goto(50,40)
    t.goto(70,40)
    t.goto(70,50)
    t.goto(40,50)
    t.goto(40,20)
    t.goto(60,20)
    t.goto(60,10)
    t.goto(40,10)
    t.goto(40,0)
    
    
def print_i():
    """Desinne un I pour écrire NSI"""
    t.goto(110,0)
    t.goto(110,10)
    t.goto(100,10)
    t.goto(100,40)
    t.goto(110,40)
    t.goto(110,50)
    t.goto(80,50)
    t.goto(80,40)
    t.goto(90,40)
    t.goto(90,10)
    t.goto(80,10)
    t.goto(80,0)

print_n()
t.penup()
t.goto(40,0)
t.pendown()
print_s()
t.penup()
t.goto(80,0)
t.pendown()
print_i()
t.exitonclick()