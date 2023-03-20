'''
Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
'''
from random import randint

class GameOfLife:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.board:
            print(row)

    def randboard(self):
        self.board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(randint(0, 1))
            self.board.append(row)

    def set_alive(self, row, col):
        self.board[row][col] = 1

    def set_dead(self, row, col):
        self.board[row][col] = 0

    def count_live_neighbors(self, row, col):
        count = 0
        for i in range(max(0, row-1), min(self.size, row+2)):
            for j in range(max(0, col-1), min(self.size, col+2)):
                if i == row and j == col:
                    continue
                if self.board[i][j] == 1:
                    count += 1
        return count

    def update_board(self):
        new_board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                live_neighbors = self.count_live_neighbors(i, j)
                if self.board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
                else:
                    if live_neighbors == 3:
                        new_board[i][j] = 1
                    else:
                        new_board[i][j] = 0
        self.board = new_board
