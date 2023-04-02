import random
import numpy as np

from board import Board
from boat import Boat
from agent import Agent
# Game configuration
BOATS = {
    "carrier" : 5,
    "battleship" : 4,
    "submarine" : 3,
    "cruiser" : 3,
    "destroyer" : 2
}

GAME_CONFIG = {
    "width" : 8,
    "length" : 8,
    "carrier" : 1,
    "battleship" : 1,
    "cruiser" : 1,
    "submarine" : 1,
    "destroyer" : 1
}



def place_boats():
    board = Board()
    for boat_name, boat_size in BOATS.items():
        num_boats = GAME_CONFIG[boat_name]
        for i in range(num_boats):
            while True:
                row = random.randint(0, GAME_CONFIG["width"] - 1)
                col = random.randint(0, GAME_CONFIG["length"] - 1)
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    if col + boat_size > GAME_CONFIG["length"]:
                        continue
                    position = (row, col)
                else:
                    if row + boat_size > GAME_CONFIG["width"]:
                        continue
                    position = (row, col)
                if not board.grid[position[0]:position[0]+boat_size, position[1]:position[1]+1].any():
                    board.add_boat(boat_name, boat_size, position, orientation)
                    break
    return board

def play_game(agent:Agent):
    board = place_boats()
    while not board.is_game_over():
        state = board.get_state()
        valid_moves = board.get_valid_moves()
        action = agent.choose_action(state, valid_moves)
        row, col = action
        reward = board.fire_shot(row, col)
        next_state = board.get_state()
        agent.update(state, action, next_state, reward)
    return board.boats

