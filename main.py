from battleship import play_game
from random_agent import RandomAgent
from qlearning_agent import QLearningAgent
from hit_close_agent import HitCloseAgent

BOATS = {
    "carrier" : {"size" : 5, "number" : 1},
    "battleship" : 4,
    "submarine" : 3,
    "cruiser" : 3,
    "destroyer" : 2
}

GAME_CONFIG = {
    "width" : 8,
    "height" : 8,
    "boats": {
    "carrier" : {"size" : 5, "number" : 1},
    "battleship" : {"size" : 4, "number" : 1},
    "cruiser" : {"size" : 3, "number" : 1},
    "submarine" : {"size" : 3, "number" : 1},
    "destroyer" : {"size" : 2, "number" : 1}
    }
}
random_agent = RandomAgent()
hit_close_agent = HitCloseAgent()
play_game(GAME_CONFIG, hit_close_agent)
