import numpy as np
import random
from agent import Agent
from board import Board

class HitCloseAgent(Agent):
    def __init__(self):
        pass
    
    
    def choose_action(self, state:Board):
        adjacent_moves = state.get_adjacent_moves()
        # Choose a random action from valid moves
        if len(adjacent_moves) > 0 :
            action = random.choice(adjacent_moves)
        else :
            valid_moves = state.get_valid_moves()
            action  = random.choice(valid_moves)
        return action

    def update(self, state, action, next_state, reward):
        pass