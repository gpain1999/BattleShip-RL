from abc import ABC, abstractmethod
class Agent(ABC):
    
    @abstractmethod
    def choose_action(self, state, valid_moves):
        raise NotImplementedError
    
    @abstractmethod
    def update(self,state, action, next_state, reward):
        raise NotImplementedError