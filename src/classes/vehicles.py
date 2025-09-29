from src.classes.Strategy import Strategy
from src.visualization import load_sprite
import pygame
from pathlib import Path

class Vehicle:
    pygame.init()
    def __init__(self, x, y, capacity, direction : str =  "", base = None, sprite_path = "assets/vehicles/jeep/blue_jeep_east.png"):
        path = Path("assets/vehicles/jeep/blue_jeep_east.png")
        sheet = pygame.image.load(str(path))
        sheet_width, sheet_height = sheet.get_size()
        self.position = [x,y]
        self.strategy = Strategy
        self.active = True
        self.capacity = capacity
        self.current_trips = 0
        self.inventory = []
        self.direction = direction
        self.base = base
        self.sprites = load_sprite(sprite_path, sheet_width // 4, sheet_height // 3, 3, 4)
        self.current_sprite = self.sprites[0][0]

    def move(self,direction):

        x,y = self.position

        if direction == "left" :
            self.position = [x-1,y]
        elif  direction == "right" :
            self.position = [x+1,y]
        elif  direction == "up" :
            self.position = [x,y+1]
        elif  direction == "down" :
            self.position = [x,y-1] 

        return self.position

    def unload(self):
        pass

    def pick_up(self):
        pass

    def return_to_base(self):
        pass

    def explode(self) :
        pass

    def check_full(self):
        if self.capacity == 0 :
            return True
        return False

class Jeep(Vehicle):
    def __init__(self, x, y):
        super().__init__(x, y, 2)


class Truck(Vehicle):
    def __init__(self, x, y):
        super().__init__(x, y, 3)


class Car(Vehicle):
    def __init__(self, x, y):
        super().__init__(x, y, 1)


class Motorcycle(Vehicle):
    def __init__(self, x, y):
        super().__init__(x, y, 1)

    def check_person(self,items):
         pass