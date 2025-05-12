import socket
import pyxel
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0",5005))

class Main:
    def __init__(self):
        self.pos = [[56,56],[-10,-10]]
        pyxel.init(128,128,title="Test Jeu Multijoueur")
        cc = threading.Thread(target=self.connect)
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if pyxel.btn(pyxel.KEY_Z): self.pos[0][1] -= 1
        elif pyxel.btn(pyxel.KEY_S): self.pos[0][1] += 1
        if pyxel.btn(pyxel.KEY_Q): self.pos[0][0] -= 1
        elif pyxel.btn(pyxel.KEY_D): self.pos[0][0] += 1
        #sock.sendto(f"{self.pos[0][0]}{self.pos[0][1]}".encode())

    def draw(self):
        pyxel.cls(0)
        for i, pos in enumerate(self.pos):
            pyxel.rect(pos[0],pos[1],8,8,i+1)

    def connect(self):
        print("test")
        data, addr = sock.recvfrom(1024)

Main()
