from Game_class import *
import pyxel
import time

class App:
    def __init__(self):
        pyxel.init(256,256)
        self.dg = Dungeon(128,128,15,7,1)
        self.dglv = 1
        self.player = Player(1,1)
        self.state = 1
        self.c = 2
        self.cs = 1
        self.i = 0
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if self.state == 1:
            if pyxel.btn(pyxel.KEY_Z) and not pyxel.pget(self.player.x*2,(self.player.y-1)*2) == 0:
                self.player.pp = (self.player.x, self.player.y)
                self.player.y -= 1
            elif pyxel.btn(pyxel.KEY_S) and not pyxel.pget(self.player.x*2,(self.player.y+1)*2) == 0:
                self.player.pp = (self.player.x, self.player.y)
                self.player.y += 1
            if pyxel.btn(pyxel.KEY_Q) and not pyxel.pget((self.player.x-1)*2,self.player.y*2) == 0:
                self.player.pp = (self.player.x, self.player.y)
                self.player.x -= 1
            elif pyxel.btn(pyxel.KEY_D) and not pyxel.pget((self.player.x+1)*2,self.player.y*2) == 0:
                self.player.pp = (self.player.x, self.player.y)
                self.player.x += 1
            self.dg,t,self.monst = self.player.over_p(self.dg)
            if t:
                for m in self.monst:
                    m.hp = m.hp_max
                self.state = 2
        elif self.state == 2:
            if self.cs == 1:
                if pyxel.btnp(pyxel.KEY_DOWN) and self.c+1 != 5:
                    self.c += 1
                elif pyxel.btnp(pyxel.KEY_UP) and self.c-1 != 1:
                    self.c -= 1
                if pyxel.btnp(pyxel.KEY_RETURN):
                    self.cs = self.c
                    self.c = 0
            elif self.cs == 2 or self.cs == 3:
                if pyxel.btnp(pyxel.KEY_DOWN) and self.c+1 != len([[],[],self.player.att,self.player.spe][self.cs]):
                    self.c += 1
                elif pyxel.btnp(pyxel.KEY_UP) and self.c-1 != -1:
                    self.c -= 1
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if self.cs == 2:
                        self.att = self.player.att[self.c]
                    elif self.cs == 3:
                        self.att = self.player.spe[self.c]
                    self.cs = 5
                elif pyxel.btnp(pyxel.KEY_BACKSPACE):
                    self.cs = 1
                    self.c = 2
            elif self.cs == 4:
                if pyxel.btnp(pyxel.KEY_BACKSPACE):
                    self.cs = 1
                    self.c = 2
            elif self.cs == 5:
                if pyxel.btnp(pyxel.KEY_DOWN) and self.c+1 != len(self.monst):
                    self.c += 1
                elif pyxel.btnp(pyxel.KEY_UP) and self.c-1 != -1:
                    self.c -= 1
                if pyxel.btnp(pyxel.KEY_BACKSPACE):
                    self.cs = 1
                    self.c = 2
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if type(self.att) == Spell and self.player.mp-self.att.mc >= 0:
                        self.player.mp -= self.att.mc
                        self.dmg(self.monst[self.c])
                    else:
                        self.dmg(self.monst[self.c])
                    if self.monst != []:
                        self.cs = 6
                    else:
                        self.cs = 1
                        self.c = 2
                        if self.player.hp != self.player.hp_max:
                            self.player.hp += self.player.hp_max//5
                        if self.player.mp != self.player.mp_max:
                            self.player.mp += self.player.mp_max//5
                        if self.player.hp > self.player.hp_max:
                            self.player.hp = self.player.hp_max
                        if self.player.mp > self.player.mp_max:
                            self.player.mp = self.player.mp_max
                        self.state = 1
            elif self.cs == 6:
                self.cs = 1
                self.state = 3
                self.c = 2
                self.time = time.time()
        elif self.state == 3:
            if self.monst[self.i].sp == [] and self.monst[self.i].ca:
                self.att = random.choice(self.monst[self.i].att)
            elif self.monst[self.i].att == [] and self.monst[self.i].ca:
                self.att = random.choice(self.monst[self.i].sp)
            elif self.monst[self.i].ca:
                self.att = random.choice(self.monst[self.i].att+self.monst[self.i].sp)
            if type(self.att) == Spell and self.monst[self.i].mp-self.att.mc > 0 and self.monst[self.i].ca:
                self.monst[self.i].ca = False
                self.dmg(self.player)
                self.monst[self.i].mp -= self.att.mc
            elif type(self.att) == Attack and self.monst[self.i].ca:
                self.monst[self.i].ca = False
                self.dmg(self.player)
            if self.i + 1 <= len(self.monst)-1 and (time.time()-self.time) > 2.0:
                self.monst[self.i].ca = True
                self.i += 1
                self.time = time.time()
                self.att = None
            elif self.i + 1 >= len(self.monst) and (time.time()-self.time) > 2.0:
                self.monst[self.i].ca = True
                self.i = 0
                self.state = 2
        elif self.state == 4:
            if self.cs == 1:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    self.c = 1
                    self.cs = 2
            elif self.cs == 2:
                if pyxel.btnp(pyxel.KEY_DOWN) and self.c+1 != 3:
                    self.c += 1
                elif pyxel.btnp(pyxel.KEY_UP) and self.c-1 != 0:
                    self.c -= 1
                elif pyxel.btnp(pyxel.KEY_RETURN):
                    if self.c == 1:
                        self.player.hp_max += 5
                        self.player.mp_max += 2
                        self.player.f += 0.1
                    elif self.c == 2:
                        self.player.hp_max += 2
                        self.player.mp_max += 5
                        self.player.int += 0.1
                    self.cs = 3
                    self.c = 2
                    self.player.hp = self.player.hp_max
                    self.player.mp = self.player.mp_max
            elif self.cs == 3:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    self.cs = 1
                    self.state = 1
        elif self.state == 5:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.dg = Dungeon(128,128,15,7)
                self.player = Player(1,1)
                self.state = 1
                self.c = 2
                self.cs = 1
                self.i = 0
        if self.player.exp >= self.player.lvl*10 and self.state == 1:
                self.player.exp -= self.player.lvl*10
                self.player.lvl += 1
                self.state = 4
            
    def draw(self):
        pyxel.cls(0)
        if self.state == 1:
            for x in range(128):
                for y in range(128):
                    d = self.dg.dg[x][y]
                    if x == self.player.x and y == self.player.y:
                        pyxel.rect(x*2,y*2,2,2,9)
                    elif d == "/":
                        pyxel.rect(x*2,y*2,2,2,8)
                    elif d == ",":
                        pyxel.rect(x*2,y*2,2,2,11)
                    elif d == ".":
                        pyxel.rect(x*2,y*2,2,2,5)
        elif self.state == 2:
            self.show_ennemy()
            pyxel.rect(32,112,30,60,9)
            if self.cs == 1:
                self.text_box(["Health : "+str(self.player.hp)+"/"+str(self.player.hp_max),"Mana : "+str(self.player.mp)+"/"+str(self.player.mp_max),"Attack","Spell","Items"],True)
            elif self.cs == 2:
                self.text_box([self.player.att[i].name+" : Damage : "+str(self.player.att[i].dmg) for i in range(len(self.player.att))]+["" for i in range(5-len(self.player.att))],True)
            elif self.cs == 3:
                self.text_box([self.player.spe[i].name+" : "+str(self.player.spe[i].mc)+" Mana, Damage : "+str(self.player.spe[i].dmg) for i in range(len(self.player.spe))]+["" for i in range(5-len(self.player.spe))],True)
            elif self.cs == 4:
                self.text_box([],True)
            elif self.cs == 5:
                self.text_box([mst.name+" : "+str(mst.hp)+"/"+str(mst.hp_max)+" hp, lvl : "+str(mst.lvl) for mst in self.monst]+["" for i in range(5-len(self.monst))],True)
        elif self.state == 3:
            print(self.monst)
            self.show_ennemy()
            pyxel.rect(32,112,30,60,9)
            if type(self.att) == Spell and self.monst[self.i].mp - self.att.mc > 0:
                self.text_box([f"{self.monst[self.i].name} tried to use {self.att.name} but failed","","","",""])
            elif self.att in self.monst[self.i].att:
                self.text_box([f"{self.monst[self.i].name} use {self.att.name}",f"You took {self.att.dmg} damage","","",""])
        elif self.state == 4:
            if self.cs == 1:
                self.text_box([f"Congrats you leveled up to level {self.player.lvl}!","","","","Press enter to continue"])
            elif self.cs == 2:
                self.text_box(["What do you want to level up ?","Attack","Intelligence","",""],True)
            elif self.cs == 3:
                self.text_box([f"Max health augmented to {self.player.hp_max}",f"Max mana augmented to {self.player.mp_max}","","","Press enter to continue"])
        elif self.state == 5:
            self.text_box([f"You died at level {self.player.lvl}","Press enter to restart","","",""])
            
    
    def text_box(self,text:list,c=False):
        pyxel.rect(4,172,244,4,7)
        pyxel.rect(4,248,244,4,7)
        pyxel.rect(0,176,4,72,7)
        pyxel.rect(248,176,4,72,7)
        for i in range(5):
            if i == self.c and c:
                pyxel.text(21,185+13*i,text[i],7)
                pyxel.line(16,185+13*i,18,187+13*i,7)
                pyxel.line(16,189+13*i,18,187+13*i,7)
            else:
                pyxel.text(16,185+13*i,text[i],7)
    
    def show_ennemy(self):
        for i in range(len(self.monst)):
            pyxel.rect(145+35*i,0+35*i,32,32,4)
    
    def dmg(self,v):
        if type(v) != Player and type(self.att) == Spell:
            if self.att.t == "All":
                for m in self.monst:
                    m.hp -= self.att.dmg*self.player.int
            else:
                v.hp -= self.att.dmg*self.player.int
        elif type(v) != Player and type(self.att) == Attack:
            if self.att.t == "All":
                for m in self.monst:
                    m.hp -= self.att.dmg*self.player.f
            else:
                v.hp -= self.att.dmg*self.player.f
        else:
            v.hp -= self.att.dmg
        for m in self.monst:
            if m.hp <= 0:
                self.death(m)
    
    def death(self,v):
        if type(v) == Player:
            self.state = 5
        else:
            self.monst.pop(self.monst.index(v))
            self.player.exp += random.randint(2*v.lvl,5*v.lvl)

App()