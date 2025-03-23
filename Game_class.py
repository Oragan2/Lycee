import random
import math
from Monstre import *
from Fight import *

class Dungeon:
    def __init__(self, w:int, h:int, r:int, rs:int, lv:int):
        self.w = w  # Store width and height for later use
        self.h = h
        self.r = r
        self.rs = rs # room size
        self.lv = lv
        self.dg = self.simulated_annealing(w, h, r, rs)
        self.rooms = []

    def __str__(self):
        return "\n".join(str(l) for l in self.dg)

    def energy(self, state):  # Add overlap_penalty parameter
        energy = 0
        overlap_penalty = self.r
        temp_dg = [[' ' for _ in range(self.w)] for _ in range(self.h)]
        for room in state:
            temp_dg = room.draw_room(temp_dg)
        for j in range(len(temp_dg)):
            for i in range(len(temp_dg[0])):
                if temp_dg[j][i] == '#':
                    count = 0
                    for k in range(len(temp_dg)):
                        for l in range(len(temp_dg[0])):
                            if temp_dg[k][l] == '#':
                                if (i == l and j == k):
                                    count += 1
                    if count > 1:
                        energy += overlap_penalty * (count-1)  # Apply the penalty for each overlap. Substract 1 so it doesnt count the current room.
        return energy

    def generate_neighbor(self, state):
        neighbor = [x for x in state]
        operation = random.choice(["move", "swap"])  # Choose operation
        if operation == "move":
            room_to_move = random.randint(0, len(neighbor) - 1)
            dx = random.randint(-10, 10)  # Larger moves
            dy = random.randint(-10, 10)
            new_x = max(1, min(self.w - 2, neighbor[room_to_move].center[0] + dx))
            new_y = max(1, min(self.h - 2, neighbor[room_to_move].center[1] + dy))
            neighbor[room_to_move] = Room(self.rs,(new_x, new_y),self.lv)
        elif operation == "swap":
            room1, room2 = random.sample(range(len(neighbor)), 2)
            neighbor[room1], neighbor[room2] = neighbor[room2], neighbor[room1]
        return neighbor
    
    def simulated_annealing(self, w, h, r, rs):
        dg = [[' ' for _ in range(w)] for _ in range(h)]  # Local dg

        entrance = Room(rs,(2, 2),True,1)
        exit = Room(rs,(w - 2, h - 2),self.lv)
        
        initial_state = [entrance, exit]
        
        for _ in range(r):
            p = Room(rs,(random.randint(1, w - 2), random.randint(1, h - 2)),self.lv)
            initial_state.append(p)

        current_state = initial_state
        self.rooms = current_state
        current_energy = self.energy(current_state)
        best_energy = current_energy

        T = 100.0  # Initial temperature
        cooling_rate = 0.90  # Cooling rate

        while T > 0.1:  # Stopping criterion
            neighbor_state = self.generate_neighbor(current_state)
            neighbor_energy = self.energy(neighbor_state)
            delta_energy = neighbor_energy - current_energy

            if delta_energy < 0:
                current_state = neighbor_state
                current_energy = neighbor_energy

                if current_energy < best_energy:
                    self.rooms = current_state
                    best_energy = current_energy
            else:
                acceptance_probability = math.exp(-delta_energy / T)
                if random.random() < acceptance_probability:
                    current_state = neighbor_state
                    current_energy = neighbor_energy

            T *= cooling_rate  # Cool down

        

        self.dg = dg  # Assign the local dg to self.dg  <- Crucial!

        self.connect_rooms()

        dg = entrance.draw_room(dg)
        dg = exit.draw_room(dg)
        for room in self.rooms:
            dg = room.draw_room(dg)
        self.room = self.rooms
        self.dg = dg
        
        return self.dg
    
    def create_path(self, room1, room2):
        start = room1.center  # Use room centers for pathfinding
        end = room2.center    # Use room centers for pathfinding

        open_set = {start}
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}

        while open_set:
            current = min(open_set, key=f_score.get)

            if current == end: # Compare tuples
                path = self.reconstruct_path(came_from, current)
                self.draw_path(path)
                return

            open_set.remove(current)
            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, end)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

    def heuristic(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)  # Euclidean distance

    def get_neighbors(self, node):
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = node[0] + dx
            y = node[1] + dy
            if 0 <= x < self.w and 0 <= y < self.h:  # Bounds check only
                neighbors.append((x, y))
        return neighbors

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def draw_path(self, path):
        for x, y in path:
            self.dg[y][x] = '.'  # Or any other character you want for the path
            
    def connect_rooms(self):
        for i in range(len(self.rooms)):
            nearest_neighbors = []
            for j in range(len(self.rooms)):
                if i != j:
                    dist = self.distance(self.rooms[i], self.rooms[j])
                    nearest_neighbors.append((dist, self.rooms[j]))

            nearest_neighbors.sort(key=lambda x: x[0])  # Sort by distance (x[0])
            num_connections = min(3, len(nearest_neighbors)) # Connect to at most 2 nearest neighbors
            for k in range(num_connections):
                while len(self.rooms[i].connected) <  3 and len(nearest_neighbors) != 0:
                    if len(nearest_neighbors[0][1].connected) < 3 and self.rooms not in nearest_neighbors[0][1].connected:
                        self.create_path(self.rooms[i], nearest_neighbors[0][1])
                        self.rooms[i].connected.append(nearest_neighbors[0][1])
                        nearest_neighbors[k][1].connected.append(self.rooms[i])
                    nearest_neighbors.pop(0)

    def distance(self, room1, room2):
        return math.sqrt((room1.center[0] - room2.center[0])**2 + (room1.center[1] - room2.center[1])**2)

class Room:
    def __init__(self, size:int, center:tuple,lv:int, d=False):
        self.size = size
        self.center = center
        self.connected = []
        self.done = d
        self.ennemy = self.ennemys(lv)
    
    def draw_room(self, dg):
        for j in range(len(dg)):
            for i in range(len(dg[0])):
                if (self.center[0] - self.size // 2 <= i <= self.center[0] + self.size // 2) and \
                   (self.center[1] - self.size // 2 <= j <= self.center[1] + self.size // 2) and not self.done:
                    dg[j][i] = '/'
                elif(self.center[0] - self.size // 2 <= i <= self.center[0] + self.size // 2) and \
                    (self.center[1] - self.size // 2 <= j <= self.center[1] + self.size // 2) and self.done:
                    dg[j][i] = ','
        return dg
    
    def ennemys(self,lv):
        ennemy = lv1_ennemy
        c = random.randint(0,100)
        if c in [i for i in range(50)]:
            return [random.choice(ennemy)]
        elif c in [i for i in range(50,90)]:
            d = []
            for i in range(2):
                a = random.choice(ennemy)
                while a in d:
                    a = random.choice(ennemy)
                d.append(a)
            return d
        elif c in [i for i in range(90,100)]:
            d = []
            for i in range(3):
                a = random.choice(ennemy)
                while a in d:
                    a = random.choice(ennemy)
                d.append(a)
            return d
        
class Player:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
        self.lvl = 1
        self.exp = 0
        self.hp = 10
        self.hp_max = 10
        self.mp = 10
        self.mp_max = 10
        self.f = 1.0
        self.int = 1.0
        self.att = [Punch]
        self.spe = [Fire_Ball]
        self.pp = (x,y)
    
    def over_p(self,dg):
        if dg.dg[self.x][self.y] == '/':
            r = sorted([(dg.room[i].center, dg.room[i]) for i in range(len(dg.room))], key=lambda b : dg.heuristic(b[0], (self.y, self.x)))
            if r[0][1].done == False:
                r[0][1].done = True
                dg.dg = r[0][1].draw_room(dg.dg)
            return dg, True, r[0][1].ennemy
        return dg, False, None