# =================================== ANGRY BIRD CLI ==============================
import random

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
    
    def print_board(self):
        print("=========================== ANGRY BIRD BOARD =======================")
        print("PIG: O_O \n BIRD: ._. \n")        

        for col in range(self.columns):
            print(f" {col:} ", end="")
        print()   

        for i, row in enumerate(self.board):
            print(f"{i:2}", end="")
            for j, cell in enumerate(row):
                if i == self.bird.row and j == self.bird.col:
                    print(f"{self.bird.bird_body} ", end="")
                elif i == self.pig.row and j == self.pig.col:
                    print(f"{self.pig.pig_body} ", end="")
                else:
                    print(cell, end="")
            print()    
        

# =================================== INSTANTIATING THE OBJECTS ==============================

gameBoard = Board(10, 10)
gameBoard.print_board()
