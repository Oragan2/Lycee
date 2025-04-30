class Attack:
    def __init__(self,name:str,dmg:int,t:str):
        if t not in ["Single","All"]:
            raise TypeError
        self.dmg = dmg
        self.t = t
        self.name = name

class Spell:
    def __init__(self,name:str,dmg:int,t:str,mc:int):
        if t not in ["Single","All"]:
            raise TypeError
        self.dmg = dmg
        self.t = t
        self.mc = mc
        self.name = name

# Base player attack
Punch = Attack("Punch",2.0,"Single")
Fire_Ball = Spell("Fire Ball",5.0,"All",3)
# Monster attack
Bone_throw = Attack("Bone Throw",1.0,"Single")
Bite = Attack("Bite",2.0,"Single")
Sword_slash = Attack("Sword Slash",3.0,"Single")