import random
from src.classes import Vehicles
from src.classes import Items
from src.classes import Mines
import pygame
def printMatrix(matrix):
    print("Current Map State:")
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

class MapManager:
    def __init__(self, width = 40, height = 40):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(height)] for _ in range(width)] #una matriz de height filas y width columnas llena de ceros. Doble bucle.
        self.medkit = [] #Luego separar en listas de cada item
        self.clothes = []
        self.food = []
        self.weapons = []
        self.people = []
        self.mines = []
        self.vehicles = []

    def generate_map(self):

        for _ in range(10): #Instancia 10 personas aleatoriamente
            x, y = self.random_empty_position()  # x=col, y=row
            self.board[x][y] = "person"
            person = Items.Person((x, y))
            self.people.append(person)

        random_quantity = 50
        x = random.randint(1, random_quantity)

        for _ in range (x):
            x, y = self.random_empty_position()  # x=col, y=row
            self.board[x][y] = "medkit"
            supply = Items.Medkit((x, y))
            self.medkit.append(supply) #Para probar la aparicion de items

        random_quantity -= x 
        x = random.randint(1, random_quantity)

        for _ in range (x):
            x, y = self.random_empty_position()  # x=col, y=row
            self.board[x][y] = "weapon"
            weapon = Items.Weapons((x, y))
            self.weapons.append(weapon) #Para probar la aparicion de items

        random_quantity -= x 
        x = random.randint(1, random_quantity)

        for _ in range (x):
            x, y = self.random_empty_position()  # x=col, y=row
            self.board[x][y] = "food"
            food = Items.Food((x, y))
            self.food.append(food) #Para probar la aparicion de items

        random_quantity -= x 

        for _ in range (x):
            x, y = self.random_empty_position()  # x=col, y=row
            self.board[x][y] = "clothes"
            clothes = Items.Clothes((x, y))
            self.clothes.append(clothes) #Para probar la aparicion de items

        for _ in range(15): #Instancia 15 personas aleatoriamente
            x, y = self.random_empty_position()  
            self.board[x][y] = "mine"
            mine = Mines.MineG2(x, y)
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

    def draw(self, screen, cell_size):
        # dibuja la cuadrícula y objetos. `screen` es la surface actual
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # borde celda

                cell = self.board[row][col]
                # Si el objeto tiene sprite/image, escalar y blitear:
                if isinstance(cell, str):
                    if cell == "person":
                        pygame.draw.circle(screen, (255, 200, 0), rect.center, max(1, cell_size//3))
                    elif cell == "supply":
                        pygame.draw.rect(screen, (0, 0, 200), rect.inflate(-cell_size//4, -cell_size//4))
                    elif cell == "mine":
                        pygame.draw.rect(screen, (100, 0, 0), rect.inflate(-cell_size//4, -cell_size//4))
                else:
                    # si guardaste objetos con .image o .sprite:
                    obj = cell
                    if hasattr(obj, "image") and obj.image:
                        img = obj.image
                        img_s = pygame.transform.scale(img, (cell_size, cell_size))
                        screen.blit(img_s, (col * cell_size, row * cell_size))

    def get_position(self):
        pass

    def is_safe(self):
        pass