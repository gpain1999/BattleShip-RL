import numpy as np
import random
from agent import Agent

class RandomAgent(Agent):
    def __init__(self):
        pass

    def choose_action(self, state, valid_moves):
        # Choose a random action from valid moves
        action = random.choice(valid_moves)
        return action

    def update(self, state, action, next_state, reward):
        pass