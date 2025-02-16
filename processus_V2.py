import tkinter as tk
from point import Point

class Processus:
    def __init__(self, nom:str, arrive:int, duree:int):
        self.name = nom
        self.arrive = arrive
        self.duree = duree
    
    def get_name(self):
        return self.name
    
    def get_arrive(self):
        return self.arrive
    
    def get_duree(self):
        return self.duree
    
    def duree_m1(self):
        self.duree -= 1
    
def RR(ls:list) -> list:
    r = []
    res = []
    tt = 0
    for d in ls:
        tt += d.get_duree()
    for i in range(tt):
        for d in ls:
            if i >= d.get_arrive() and d.get_duree() > 0 and d not in r:
                r.append(d)
                d.duree_m1()
        res.append(r.pop(0).get_name())
    return res

def SJF(ls:list) -> list:
    r = []
    res = []
    a = None
    tt = 0
    for d in ls:
        tt += d.get_duree()
    for i in range(tt):
        for pr in ls:
            if i == pr.get_arrive():
                r.append(pr)
                if a == None:
                    a = pr
        if a != None:
            if a.get_duree() > 0:
                res.append(a.get_name())
                a.duree_m1()
            if a.get_duree() == 0:
                r.pop(r.index(a))
                a = None
                for p in r:
                    if a == None:
                        a = p
                    elif a.get_duree() > p.get_duree() and p.get_duree() != 0:
                        a = p
    return res

def FIFO(ls:list) -> list:
    r = []
    res = []
    tt = 0
    for d in ls:
        tt += d.get_duree()
    for i in range(tt):
        for pr in ls:
            if i == pr.get_arrive():
                r.append(pr)
        if r != []:
            res.append(r[0].get_name())
            r[0].duree_m1()
            if r[0].get_duree() == 0:
                r.pop(0)
    return res

def graph(ls:list,md:str):
    tt = 0 # temps totale d'execution
    rf1 = 0
    l = [d.get_name() for d in ls]
    la = [d.get_arrive() for d in ls]
    #### Obtient l'enchainement des executions suivant le mode demander et le nombre totale de quantum de temps
    for d in ls:
        tt += d.get_duree()
    if md == "RR":
        r = RR(ls)
    elif md == "SJF":
        r = SJF(ls)
    else:
        r = FIFO(ls)
    ####
    #### Afficher les lignes du graphique
    P1 = Point(25,375)
    P1.drawLine(canvas, P1.translate(0, -350))
    P1.drawLine(canvas, P1.translate(760,0))
    ####
    ds = 350/len(ls) # Pour les lignes
    dls = 760/tt # Pour les colognes 
    P2 = Point(25+dls,375)
    P1 = P1.translate(0, -ds) # Place les point sur la première ligne
    P2 = P2.translate(0, -ds)
    for d in ls:
        canvas.create_text((10,P1.y),text=d.get_name())
        P1 = P1.translate(0,-ds)
    P1 = Point(25,375-ds)
    for i in range(tt):
        P1 = P1.translate(0,ds*-(l.index(r[i])-rf1))  # Fais monter les point a la ligne qu'il faut
        P2 = P2.translate(0,ds*-(l.index(r[i])-rf1))
        rf1 = l.index(r[i])
        P1.drawLine(canvas, P2)
        canvas.create_line(P2.x,P2.y-5,P2.x,P2.y+5,width=2) # Ajoute la bordure Droite
        canvas.create_line(P1.x,P1.y-5,P1.x,P1.y+5,width=2) # Ajoute la bordure Gauche
        if i in la:
           P1 = P1.translate(0,ds*-(la.index(i)-rf1))
           P1.draw(canvas,'red')
           P1 = P1.translate(0,ds*-(l.index(r[i])-la.index(i)))
        canvas.create_text((P1.x,390),text=str(i)) # Affiche les quantum de temps en bas du graphique
        P1 = P1.translate(dls,0) # Fais avancer les points pour peut-être afficher le porchain quantum de temps
        P2 = P2.translate(dls,0)
    canvas.create_text((785,390),text=str(tt))
    #### Légende
    P1 = Point(25,410)
    P1.draw(canvas,'red')
    P1 = P1.translate(70,0)
    canvas.create_text((P1.x,P1.y),text="Arrivé du processus")
    P1 = P1.translate(0,20)
    P2 = P1.translate(-70,0)
    P1.drawLine(canvas,P2)
    canvas.create_line(P2.x,P2.y-5,P2.x,P2.y+5,width=2)
    canvas.create_line(P1.x,P1.y-5,P1.x,P1.y+5,width=2)
    canvas.create_text((240,430),text="Execution du processus par quantum de temps")
    ####
    
            

window = tk.Tk()
window.title("Graph processus")

canvas = tk.Canvas(window, width = 810, height = 440, bg = 'ivory')
canvas.pack(padx = 10, pady = 10)

p1 = Processus("P1", 1, 8)
p2 = Processus("P2", 0, 5)
p3 = Processus("P3", 2, 9)
p4 = Processus("P4", 3, 2)
p5 = Processus("P5", 4, 6)
p6 = Processus("P6", 6, 8)
p7 = Processus("P7", 5, 4)        

graph([p1,p2,p3,p4,p5,p6,p7],"RR")

window.mainloop()
