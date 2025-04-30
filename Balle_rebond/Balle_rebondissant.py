import pygame, sys
import time
from Balle import Balle
import random as ran

WIDTH = 1920
HEIGHT = 1080
#Nb = int(input("Nombre de Balle voulue = "))
Balles = [Balle(20,ran.randint(50,WIDTH),ran.randint(50,HEIGHT),ran.randint(1,20),(ran.randint(0,255),ran.randint(0,255),ran.randint(0,255))) for i in range(200)]

pygame.display.init()
pygame.display.set_caption("Balles rebondissantes")

fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
fenetre.fill([232, 229, 221])

while True :
    fenetre.fill([232, 229, 221])
    Balles_save = []
    for balle in Balles:
        Balles_save.append(balle)
    for i in range(len(Balles)):
        Balles[0].draw(fenetre)
        Balles[0].move(WIDTH,HEIGHT)
        for i in Balles:
            Balles[0].colision(i)
        Balles.pop(0)
    Balles = Balles_save
    pygame.display.update()
    time.sleep(0.015)


for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.display.quit()
        sys.exit()

time.sleep(0.05)