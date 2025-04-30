import pyxel
import time 

pyxel.init(128, 128, title="Javelin simulator")

nb_lance=1
count = 0
timer = 11
list_circle = [(50, 6, 5), (64, 6, 0), (78, 6, 8), (57, 12, 10), (71, 12, 11)]
coordonee_text = [64, 42]
liste_distance = [0, 20, 40, 60, 80, 100, 120]
pyxel.colors[15] = 0x04FF00
coordonnees_jav=[0,100, 6, 96]
score = []

def nb_appuis(count:int) -> int:
    if pyxel.btnp(pyxel.KEY_SPACE):
        count += 1
    elif pyxel.btn(pyxel.KEY_CTRL) and pyxel.btnp(pyxel.KEY_A):
        count+=2
    return count


def parabole (count: int , coordonnees_jav : list) -> list :
    coordonnees_jav[2]=coordonnees_jav[0]-4
    coordonnees_jav[3]=coordonnees_jav[1]-1
    coordonnees_jav[0]+=1
    coordonnees_jav[1] = round(0.03 *(coordonnees_jav[0]+10)*(coordonnees_jav[0]-count)+100)
    return coordonnees_jav

def reset() :
    global coordonee_text, coordonnees_jav , count , timer
    coordonnees_jav=[0,100, 6, 96]
    coordonee_text = [64, 42]
    count = 0
    timer = 11
    time.sleep(2)


def update():
    global count, timer , coordonnees_jav, distance, nb_lance, score
    if timer != 0:
        count = nb_appuis(count)
    if (pyxel.frame_count%30 == 0) and (timer > 0):       
        timer -= 1
    if timer == 0 and coordonee_text >= [8, 8]:
        coordonee_text[1] -= 2.27
        coordonee_text[0] -= 3.6
    if timer == 0:
        if coordonnees_jav[0]<= count:
            coordonnees_jav= parabole(count, coordonnees_jav)
        if coordonnees_jav[0]==count +1: 
            nb_lance+=1
            score.append(count)
            reset()
    
def draw():
    global count, timer, score
    if nb_lance<=3 :
        pyxel.cls(6)
        pyxel.rect(0, 100, 128, 42, 15)
        pyxel.text(coordonee_text[0], coordonee_text[1], str(count), 7)
        pyxel.text(120, 8, str(timer), 7)
        pyxel.text(1,6, str(nb_lance), 7)
        for circle in list_circle:
            pyxel.circb(circle[0], circle[1], 6, circle[2])
        for line in liste_distance:
            pyxel.line(line, 100, line, 105, 7)
            pyxel.text(line-3, 108 , str(line), 7)
        pyxel.line(coordonnees_jav[2], coordonnees_jav[3], coordonnees_jav[0], coordonnees_jav[1], 8)
    else: 
        pyxel.cls(0)
        pyxel.text(36,44, "PARTIE TERMINEE", 7)
        pyxel.text(18,55,"Premier lance :" + str(score[0])+ " Metres", 7)
        pyxel.text(18,63 ,"Deuxieme lance :" + str(score[1])+ " Metres", 7)
        pyxel.text(18,71,"Troisieme lance :" + str(score[2])+ " Metres", 7)

pyxel.run(update, draw)