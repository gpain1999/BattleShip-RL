from abc import ABC, abstractmethod
from board import Board
class Agent(ABC):
    
    @abstractmethod
    def choose_action(self, state:Board):
        raise NotImplementedError
    
    @abstractmethod
    def update(self,state:Board, action, next_state:Board, reward):
        raise NotImplementedError