import numpy as np
import random
from agent import Agent

class RandomAgent(Agent):
    def __init__(self):
        pass

    def choose_action(self, state):
        # Choose a random action from valid moves
        valid_moves = state.get_valid_moves()
        action  = random.choice(valid_moves)
        return action
    def update(self, state, action, next_state, reward):
        pass