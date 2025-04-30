import pyxel

class App:
    def __init__(self):
        pyxel.init(128, 128)
        pyxel.colors[0] = 0xaac1ff
        self.x = 56
        self.y = 120
        self.p = [(20, 90, 40, 4),(70, 70, 40, 4),(20, 40, 40, 4),(70, 20, 40, 4)]
        self.v = 0
        self.jf = 0
        self.rc = []
        self.onGround = True
        pyxel.run(self.update, self.draw)

    def update(self):
        for i in range(128):
            for j in range(128):
                if pyxel.pget(i,j) == 0:
                    self.rc.append((i,j))
        self.pp = (self.x,self.y)
        if pyxel.btn(pyxel.KEY_SPACE) and self.onGround:
            self.y -= 19
            self.jf = 17
        if pyxel.btn(pyxel.KEY_Q) and not self.x-1 == -1:
            self.x -= 1
        elif pyxel.btn(pyxel.KEY_D) and not self.x+1 == 121:
            self.x += 1
        if self.y >= 120:
            self.g = 0
            self.y = 120
            self.onGround = True
        elif self.y <= 0:
            self.jf = 0
        else:
            self.onGround = False
        if not self.onGround:
            self.g = 9.81
            self.v = self.jf-self.g
            self.y -= int(self.v)
            self.jf -= 1


    def draw(self):
        pyxel.cls(6)
        pyxel.line(self.pp[0],self.pp[1],self.x,self.y,0)
        for p in self.p:
            pyxel.rect(p[0],p[1],p[2],p[3],13)
        pyxel.rect(self.x, self.y, 8, 8, 9)

App()