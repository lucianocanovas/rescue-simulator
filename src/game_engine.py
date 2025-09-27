from src.map_manager import MapManager
from src.classes.Player import Player

def player_list():
    players = []
    player1 = Player()
    player2 = Player()
    return [player1, player2]


class GameEngine:
    def __init__(self, fps=60):
        self.board = MapManager
        self.players = player_list()
        self.fps = fps

    def start(self):
        pass

    def update(self):
        pass

    def check_collisions(self):
        pass

    def calculate_points(self):
        pass

    def end(self):
        pass