import random
from src.classes import Vehicles
from src.classes import Items
from src.classes import Mines

def printMatrix(matrix):
    print("Current Map State:")
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

class MapManager:
    def __init__(self, width = 40, height = 40):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)] #una matriz de height filas y width columnas llena de ceros. Doble bucle.
        self.items = []
        self.people = []
        self.mines = []
        self.vehicles = []

    def generate_map(self):

        for _ in range(10): #Instancia 10 personas aleatoriamente
            x, y = self.random_empty_position() 
            self.board[x][y] = "person"
            person = Items.Person((x, y))
            self.people.append(person)

        for _ in range(50): #Instancia 50 mercancias (a modificar)
            x, y = self.random_empty_position()
            self.board[x][y] = "supply" #Mercancia deberia ser*
            # Create a Supply item and store the object so it has sprites and position
            try:
                supply = Items.Supply(10, (x, y), "generic", "assets/resources/supply.png")
            except Exception:
                # Fall back to a simple positional record if Item constructor is unavailable
                supply = (x, y)
            self.items.append(supply)

        for _ in range(15): #Instancia las minas.
            x, y = self.random_empty_position()
            self.board[x][y] = Mines.Mine(x, y, 5, 5, "assets/resources/mine.png")
            # Create a Mine object so drawing code can access current_sprite
            try:
                mine = Mine(x, y, 3, 3)
            except Exception:
                # If Mine signature changed, try MineG2
                try:
                    mine = MineG2(x, y)
                except Exception:
                    mine = (x, y)
            self.mines.append(mine)

        printMatrix(self.board)
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