class Vecteur:
    def __init__(self,vx,vy):
        self.vx = vx
        self.vy = vy
        
    def __add__(self,other):
        return (self.vx+other.vx, self.vy+other.vy)
    
    def __str__(self):
        return f"({self.vx} ; {self.vy})"