import Vecteur
import pygame
import math

class Balle:
    def __init__(self, radius, x, y, v, color):
        self.radius = radius
        self.x = x
        self.y = y 
        self.v = Vecteur.Vecteur(v,v)
        self. color = color
    
    def draw(self, fenetre):
        pygame.draw.circle(fenetre,self.color,(self.x, self.y),self.radius)
    
    def move(self,w,h):
        self.x += self.v.vx
        self.y += self.v.vy
        if self.x >= w-self.radius or self.x <= 0+self.radius:
            self.v.vx = -self.v.vx
        elif self.y >=h-self.radius or self.y <=0+self.radius:
            self.v.vy = -self.v.vy
            
    def colision(self, other):
        if -40<=math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)<=40:
            self.v.vx = -self.v.vx
            self.v.vy = -self.v.vy
            other.v.vx = -other.v.vx
            other.v.vy = -other.v.vy
        