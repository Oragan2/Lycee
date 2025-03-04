import pyxel

class App:
    def __init__(self):
        pyxel.init(128, 128)
        self.m = [[' ']*128 for i in range(128)]
        self.x = 56
        self.y = 120
        self.jf = 0
        self.onGround = True
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE) and self.onGround:
            self.jf = 40
        if pyxel.btn(pyxel.KEY_SPACE) and self.jf > 0:
            self.pp = (self.x,self.y)
            self.y -= 1
            self.jf -= 1
        else:
            self.jf = 0
        if pyxel.btn(pyxel.KEY_Q):
            self.pp = (self.x,self.y)
            self.x -= 1
        elif pyxel.btn(pyxel.KEY_D):
            self.pp = (self.x,self.y)
            self.x += 1
        if self.y >= 120:
            self.onGround = True
        elif self.y <= 0:
            self.jf = 0
        else:
            self.onGround = False
        if not self.onGround and self.jf == 0:
            self.pp = (self.x,self.y)
            self.y += 1

    def draw(self):
        pyxel.cls(12)
        pyxel.rect(self.x, self.y, 8, 8, 9)

App()