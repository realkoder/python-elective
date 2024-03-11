# =================================== ANGRY BIRD CLI ==============================
import random
import os

# =================================== BIRD CLASS ==============================
class Bird:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.direction = "right"
        self.bird_body = "._."

    def game_win():
        pass    

    def game_end():
        pass

# =================================== PIG CLASS ==============================
class Pig:
    def __init__(self, row, col):
        self.row = row
        self.col = col        
        self.pig_body = "O_O"
        self.is_alive = True

    def game_win():
        pass    

    def game_end():
        pass

# =================================== BOARD CLASS ==============================

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [[" x " for _ in range(columns)] for _ in range(rows)]
        self.spawn_bird()
        self.spawn_pig()      

    def spawn_bird(self):
        randomRow = random.randint(0, self.rows - 1)
        randomCol = random.randint(0, self.columns - 1)
        self.bird = Bird(randomRow, randomCol)

    def spawn_pig(self):
        randomRow = random.randint(0, self.rows - 1)
        randomCol = random.randint(0, self.columns - 1)
        self.pig = Pig(randomRow, randomCol)

    def move_bird(self, direction):
        if direction == "R":
            if self.bird.col < self.columns - 1:
                self.bird.col += 1
        elif direction == "L":
            if self.bird.col > 0:
                self.bird.col -= 1
        elif direction == "U":
            if self.bird.row > 0:
                self.bird.row -= 1
        elif direction == "D":
            if self.bird.row < self.rows - 1:
                self.bird.row += 1
    
    def check_if_bird_win(self):
        if self.bird.row == self.pig.row and self.bird.col == self.pig.col:
            return True        
        return False

    
    def print_board(self):
        print("=========================== ANGRY BIRD BOARD =======================")
        print("\n PIG: O_O \n BIRD: ._. \n")        

        print(f" ", end="")
        for col in range(self.columns):            
            print(f" {col} ", end="")
        print()   

        for i, row in enumerate(self.board):
            print(f"{i}", end="")
            for j, cell in enumerate(row):
                if i == self.bird.row and j == self.bird.col:
                    print(f"{self.bird.bird_body} ", end="")
                elif i == self.pig.row and j == self.pig.col:
                    print(f"{self.pig.pig_body} ", end="")
                else:
                    print(cell, end="")
            print()    
        

# =================================== WORKSPACE CLASS ==============================

class Workspace:
    def display_bird_move():
        print("Bird have to move - which direction: L (LEFT), R (RIGHT), U (UP), D (DOWN)")


# =================================== INSTANTIATING THE OBJECTS ==============================
workspace = Workspace
gameBoard = Board(10, 10)
print("ANGRY BIRDS")  
gameBoard.print_board()


# =================================== START THE GAME ==============================

while gameBoard.pig.is_alive:    
    workspace.display_bird_move()
    direction_input = input("Move (U/D/L/R): ").strip().upper()

    gameBoard.move_bird(direction_input)
    
    if gameBoard.check_if_bird_win():
        gameBoard.pig.is_alive = False
        print("======================== YOU WON! ====================")
    else:
        gameBoard.print_board()