import numpy as np
import random
from agent import Agent
class QLearningAgent(Agent):
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=0.9):
        self.q_table = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def choose_action(self, state, valid_moves):
        if np.random.uniform() < self.epsilon:
            # Choose a random action from valid moves
            action = random.choice(valid_moves)
        else:
            # Choose the action with the highest Q-value for this state
            q_values = [self.q_table.get((state, move), 0) for move in valid_moves]
            max_q_value = max(q_values)
            if q_values.count(max_q_value) > 1:
                # If there are multiple actions with the same Q-value, choose one randomly
                best_moves = [i for i in range(len(valid_moves)) if q_values[i] == max_q_value]
                action_index = random.choice(best_moves)
            else:
                action_index = q_values.index(max_q_value)
            action = valid_moves[action_index]
        return action

    def update(self, state, action, next_state, reward):
        old_q_value = self.q_table.get((state, action), None)
        if old_q_value is None:
            self.q_table[(state, action)] = reward
        else:
            next_max_q = max([self.q_table.get((next_state, next_move), 0) for next_move in Board.get_valid_moves(next_state)])
            self.q_table[(state, action)] = old_q_value + self.alpha * (reward + self.gamma * next_max_q - old_q_value)
