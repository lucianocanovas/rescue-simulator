import random
from src.classes import Vehicles
from src.classes import Items

class MapManager:
    def __init__(self, width = 50, height = 50):
        self.width = width
        self.height = height
        self.board = [[0 for column in range(width)] for row in range(height)]
        self.items = []
        self.people = []
        self.mines = []
        self.vehicles = []

    def generate_map(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for i in range(10):
            x, y = self.random_empty_position()
            self.board[x][y] = "person"
            person = Items.Person((x, y))
            self.people.append(person)

        for i in range(50):
            x, y = self.random_empty_position()
            self.board[x][y] = "mine"
            self.items.append([x, y])

        for i in range(15):
            x, y = self.random_empty_position()
            self.board[x][y] = "mine"
            self.mines.append([x, y])

        """-----------------------------------------------------------------------------------------------"""
        # Bloque de prueba
        vehicle = Vehicles.Car(0, 0)
        self.vehicles.append(vehicle)

        """-----------------------------------------------------------------------------------------------"""

    def random_empty_position(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[x][y] == 0:
                return x, y

    def get_position(self):
        pass

    def is_safe(self):
        pass