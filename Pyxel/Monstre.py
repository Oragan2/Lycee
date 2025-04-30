from Fight import *

class Monster:
    def __init__(self,name:str,pv:int,lvl:int,att:list,sp:list,mp:list,loot=[]):
        self.name = name
        self.hp = pv
        self.hp_max = pv
        self.mp = mp
        self.mp_max = mp
        self.lvl = lvl
        self.loot = loot
        self.att = att
        self.sp = sp
        self.ca = True
<<<<<<< HEAD
        self.statue = "Alive"
=======
>>>>>>> fc9acc5024275baf41e857549168f97a380f1a0b

lv1_ennemy = [Monster("Bat",2.0,1,[Bite],[],0) for i in range(6)]+[Monster("Skeleton",5.0,1,[Bone_throw],[],0) for i in range(3)]+[Monster("Skeleton Warrior",10.0,2,[Sword_slash],[Fire_Ball],2) for i in range(1)]
