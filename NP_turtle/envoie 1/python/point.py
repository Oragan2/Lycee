from math import pi, cos, sin

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def draw(self, surface, color='black', rayon=5):
        surface.create_oval((self.x+rayon,self.y+rayon),(self.x-rayon,self.y-rayon), fill=color, width=0)

    def drawLine(self, surface, point, color='black', width=3):
        surface.create_line((self.x, self.y), (point.x, point.y), fill=color, width=width)
    
    def translate(self, dx:int, dy:int):
        return Point(self.x+dx,self.y+dy)
    
    def rotate(self, angle:int, origine):
        a = (pi*angle)/180
        x = (self.x-origine.x)*cos(a)-(self.y-origine.y)*sin(a)+origine.x
        y = (self.x-origine.x)*sin(a)+(self.y-origine.y)*cos(a)+origine.y
        return Point(x, y)