import random as ran
import time

class Room:
    def __init__(self, symbole:str, shape:list, doors:list):
        self.symbole = symbole
        self.shape = shape
        self.doors = doors

def show():
    for i in range(size):
        line = ""
        for j in range(size):
            line+=Dungeon[i][j]
        print(line)

def rotate(room):
    shape = []
    door = []
    for coo in room.shape:
        shape.append((coo[1],-coo[0]))
    for coo in room.doors:
        door.append((coo[1],-coo[0]))
    return Room(room.symbole, shape, door)

R1 = Room("#",[(0,0),(0,1),(1,0)],[(0,2),(1,1)])
R2 = Room("/",[(0,0),(1,0),(0,1),(1,1)],[(2,1),(1,2),(0,-1)])
R3 = Room("%",[(0,0),(0,1),(0,-1),(1,0)],[(2,0),(0,2),(0,-2)])
R4 = Room("!",[(0,0)],[(1,0),(-1,0)])

Rooms = [R1,R2,R3,R4]

size = 10
Dungeon = [[" " for i in range(size)] for j in range(size)]
Took_pos = []
Sizes_left = size**2
Full = False
positions = [(0,5)]

while not Full:
    ok = True
    room = ran.choice(Rooms)
    pos = positions[0]
    checked = False
    if Sizes_left-len(room.shape) > 0:
        for i in range(4):
            ok = True
            room = rotate(room)
            for coo in room.shape:
                new_coo = (pos[0] + coo[0], pos[1] + coo[1])
                if new_coo[0] < 0 or new_coo[1] < 0 or new_coo in Took_pos or new_coo[0] >= size or new_coo[1] >= size:
                    ok = False
            if ok:
                break
        if ok:
            for coo in room.shape:
                new_coo = (pos[0] + coo[0], pos[1] + coo[1])
                Dungeon[new_coo[0]][new_coo[1]] = room.symbole
                Took_pos.append(new_coo)
                if new_coo in positions:
                    positions.remove(new_coo)
            for coo in room.doors:
                new_coo = (pos[0] + coo[0], pos[1] + coo[1])
                if new_coo not in Took_pos and new_coo[0] > 0 and new_coo[1] > 0 and new_coo[0] < size and new_coo[1] < size and new_coo not in positions:
                    positions.append(new_coo)
            Sizes_left -= len(room.shape)
            if len(positions) == 0:
                Full = True

show()