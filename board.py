
from boat import Boat
import numpy as np


class Board:
    def __init__(self,width,height):
        self.width =width
        self.height = height
        self.grid = np.zeros((self.width, self.height))
        self.boats = []

    def add_boat(self, name, size, position, orientation):
        boat = Boat(name, size, position, orientation)
        self.boats.append(boat)
        if orientation == 'horizontal':
            self.grid[position[0], position[1]:position[1]+size] = 1
        else:
            self.grid[position[0]:position[0]+size, position[1]] = 1

    def is_in_grid(self,row,col):
        if row < 0 or row >= self.width or col < 0 or col >= self.height:
            return False
        else : 
            return True

    def is_valid_move(self, row, col):
        if not self.is_in_grid(row,col):
            return False
        if self.grid[row, col] == -1 or self.grid[row, col] == 2:
            return False
        return True

    def fire_shot(self, row, col):
        hit = False
        for boat in self.boats:
            if boat.is_hit(row, col):
                hit = True
                break
        if hit:
            self.grid[row, col] = 2
            return 1  # reward for hitting a boat
        else:
            self.grid[row, col] = -1
            return -0.5  # penalty for missing a boat

    def get_state(self):
        return self.grid

    def get_valid_moves(self):
        valid_moves = []
        for row in range(self.width):
            for col in range(self.height):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def is_game_over(self):
        for boat in self.boats:
            if not self.is_boat_sunk(boat):
                return False
        return True

    def is_boat_sunk(self, boat):
        for row in range(self.width):
            for col in range(self.height):
                if boat.is_hit(row, col) and self.grid[row, col] != 2:
                    return False
        return True

    def is_adjacent_move(self, row, col):
        if (self.is_in_grid(row + 1, col) and (self.grid[row + 1, col] == 2)) or \
        (self.is_in_grid(row - 1, col) and (self.grid[row - 1, col] == 2)) or \
        (self.is_in_grid(row, col + 1) and (self.grid[row, col + 1] == 2)) or \
        (self.is_in_grid(row, col - 1) and (self.grid[row, col - 1] == 2)) :
            return True
        else : 
            return False
    
    
    
    def get_adjacent_moves(self):
        adjacent_move = []
        for row in range(self.width):
            for col in range(self.height):
                if self.is_valid_move(row,col) and self.is_adjacent_move(row, col):
                    adjacent_move.append((row, col))
        return adjacent_move
        
    def print_board(self):
        print(self.grid)
