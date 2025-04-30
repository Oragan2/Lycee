<<<<<<< HEAD
import os
import time
import random
import msvcrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

class Paddle:
    def __init__(self, position, length, board):
        self.position = position
        self.length = length
        self.board = board

    def move(self, direction):
        if direction == "left" and self.position.y > self.length // 2:
            self.position.y -= 2
        elif direction == "right" and self.position.y < self.board.cols - self.length // 2 - 1:
            self.position.y += 2

class Ball:
    def __init__(self, board):
        self.board = board
        self.position = Vector(10,20)
        self.direction = self.initialize_direction()

    def initialize_direction(self):
        directions = [Vector(1, 1), Vector(-1,1), Vector(1,-1), Vector(-1,-1)]
        return random.choice(directions)

    def move(self):
        new_position = self.position + self.direction
        cell_type = self.board.getCell(new_position.x, new_position.y)

        if cell_type == 0:
            self.position = new_position
        elif cell_type == 1:
            if self.position.x == 2 or self.position.x == self.board.rows-3:
                self.direction.x *= -1
            if self.position.y == 1 or self.position.y == self.board.cols-2:
                self.direction.y *= -1
        elif cell_type == 2:
            self.board.game.handle_deadly_collision()

class Board:
    def __init__(self, rows=20, cols=40):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_grid()
        self.paddle1 = None
        self.paddle2 = None
        self.ball = None
        self.game = None

    def create_grid(self):
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if i == 0 or i == self.rows - 1:
                    row.append(2) # 2 obstacle mortel
                elif  j == 0 or j == self.cols - 1:
                    row.append(1) # 1 obstacle
                else:
                    row.append(0) # 0 vide
            grid.append(row)
        return grid

    def add_paddle(self, paddle):
        if not self.paddle1:
            self.paddle1 = paddle
        else:
            self.paddle2 = paddle

    def set_ball(self, ball):
        self.ball = ball

    def set_game(self, game):
        self.game = game

    def getCell(self, x, y):
        if self.paddle1 and self.paddle1.position.x == x and abs(y - self.paddle1.position.y) <= self.paddle1.length // 2:
            return 1
        if self.paddle2 and self.paddle2.position.x == x and abs(y - self.paddle2.position.y) <= self.paddle2.length // 2:
            return 1
        return self.grid[x][y]

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in range(self.rows):
            line = ""
            for y in range(self.cols):
                if self.ball and (x, y) == (self.ball.position.x, self.ball.position.y):
                    line += "O"
                elif self.paddle1 and x == self.paddle1.position.x and abs(y - self.paddle1.position.y) <= self.paddle1.length // 2:
                    line += "x"
                elif self.paddle2 and x == self.paddle2.position.x and abs(y - self.paddle2.position.y) <= self.paddle2.length // 2:
                    line += "x"
                elif self.grid[x][y] == 1:
                    line += "x"
                elif self.grid[x][y] == 2:
                    line += "="
                else:
                    line += " "
            print(line)

class Game:
    def __init__(self, rows=20, cols=40):
        self.board = Board(rows, cols)
        self.board.set_game(self)
        self.ball = Ball(self.board)
        self.board.set_ball(self.ball)
        self.paddle1 = Paddle(Vector(1,cols//2),6,self.board)
        self.paddle2 = Paddle(Vector(rows-2,cols//2),6,self.board)
        self.board.add_paddle(self.paddle1)
        self.board.add_paddle(self.paddle2)
        self.running = True

    def handle_input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'q':
                self.paddle1.move("left")
            elif key == b's':
                self.paddle1.move("right")
            elif key == b'4':
                self.paddle2.move("left")
            elif key == b'6':
                self.paddle2.move("right")
            elif key == b'\x1b':
                self.running = False

    def handle_deadly_collision(self):
        self.ball.position = Vector(10,20)
        self.ball.direction = self.ball.initialize_direction()
        self.board.draw()
        time.sleep(0.5)

    def play(self, N, x):
        for _ in range(N):
            if not self.running:
                break
            self.handle_input()
            self.board.draw()
            self.ball.move()
            time.sleep(1/x)

def main():
    game = Game()
    game.play(50000,10)

=======
import os
import time
import random
import msvcrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

class Paddle:
    def __init__(self, position, length, board):
        self.position = position
        self.length = length
        self.board = board

    def move(self, direction):
        if direction == "left" and self.position.y > self.length // 2:
            self.position.y -= 2
        elif direction == "right" and self.position.y < self.board.cols - self.length // 2 - 1:
            self.position.y += 2

class Ball:
    def __init__(self, board):
        self.board = board
        self.position = Vector(10,20)
        self.direction = self.initialize_direction()

    def initialize_direction(self):
        directions = [Vector(1, 1), Vector(-1,1), Vector(1,-1), Vector(-1,-1)]
        return random.choice(directions)

    def move(self):
        new_position = self.position + self.direction
        cell_type = self.board.getCell(new_position.x, new_position.y)

        if cell_type == 0:
            self.position = new_position
        elif cell_type == 1:
            if self.position.x == 2 or self.position.x == self.board.rows-3:
                self.direction.x *= -1
            if self.position.y == 1 or self.position.y == self.board.cols-2:
                self.direction.y *= -1
        elif cell_type == 2:
            self.board.game.handle_deadly_collision()

class Board:
    def __init__(self, rows=20, cols=40):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_grid()
        self.paddle1 = None
        self.paddle2 = None
        self.ball = None
        self.game = None

    def create_grid(self):
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if i == 0 or i == self.rows - 1:
                    row.append(2) # 2 obstacle mortel
                elif  j == 0 or j == self.cols - 1:
                    row.append(1) # 1 obstacle
                else:
                    row.append(0) # 0 vide
            grid.append(row)
        return grid

    def add_paddle(self, paddle):
        if not self.paddle1:
            self.paddle1 = paddle
        else:
            self.paddle2 = paddle

    def set_ball(self, ball):
        self.ball = ball

    def set_game(self, game):
        self.game = game

    def getCell(self, x, y):
        if self.paddle1 and self.paddle1.position.x == x and abs(y - self.paddle1.position.y) <= self.paddle1.length // 2:
            return 1
        if self.paddle2 and self.paddle2.position.x == x and abs(y - self.paddle2.position.y) <= self.paddle2.length // 2:
            return 1
        return self.grid[x][y]

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in range(self.rows):
            line = ""
            for y in range(self.cols):
                if self.ball and (x, y) == (self.ball.position.x, self.ball.position.y):
                    line += "O"
                elif self.paddle1 and x == self.paddle1.position.x and abs(y - self.paddle1.position.y) <= self.paddle1.length // 2:
                    line += "x"
                elif self.paddle2 and x == self.paddle2.position.x and abs(y - self.paddle2.position.y) <= self.paddle2.length // 2:
                    line += "x"
                elif self.grid[x][y] == 1:
                    line += "x"
                elif self.grid[x][y] == 2:
                    line += "="
                else:
                    line += " "
            print(line)

class Game:
    def __init__(self, rows=20, cols=40):
        self.board = Board(rows, cols)
        self.board.set_game(self)
        self.ball = Ball(self.board)
        self.board.set_ball(self.ball)
        self.paddle1 = Paddle(Vector(1,cols//2),6,self.board)
        self.paddle2 = Paddle(Vector(rows-2,cols//2),6,self.board)
        self.board.add_paddle(self.paddle1)
        self.board.add_paddle(self.paddle2)
        self.running = True

    def handle_input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'q':
                self.paddle1.move("left")
            elif key == b's':
                self.paddle1.move("right")
            elif key == b'4':
                self.paddle2.move("left")
            elif key == b'6':
                self.paddle2.move("right")
            elif key == b'\x1b':
                self.running = False

    def handle_deadly_collision(self):
        self.ball.position = Vector(10,20)
        self.ball.direction = self.ball.initialize_direction()
        self.board.draw()
        time.sleep(0.5)

    def play(self, N, x):
        for _ in range(N):
            if not self.running:
                break
            self.handle_input()
            self.board.draw()
            self.ball.move()
            time.sleep(1/x)

def main():
    game = Game()
    game.play(50000,10)

>>>>>>> fc9acc5024275baf41e857549168f97a380f1a0b
main()