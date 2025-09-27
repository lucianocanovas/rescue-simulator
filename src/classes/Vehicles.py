import pygame.image
from ..visualization import load_sprite

import Items, Mines

class Vehicle:
    def __init__(self, capacity,x,y,image_path):
        self.position = [x,y]
        self.capacity = capacity
        self.sprite = load_sprite(image_path)

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

    def download(self):
        pass

    def find_shortest_path(self):
        pass

    def check_full(self):
        if self.capacity == 0 :
            return True
        return False

class Jeep(Vehicle):
    def __init__(self, x, y):
        super().__init__(2, x, y, "../../assets/vehicles/jeep")


class Truck(Vehicle):
    def __init__(self, x, y):
        super().__init__(3, x, y, "../../assets/vehicles/truck")


class Car(Vehicle):
    def __init__(self, x, y):
        super().__init__(1, x, y, "../../assets/vehicles/car")


class Motorcycle(Vehicle):
    def __init__(self, x, y):
        super().__init__(1, x, y, "../../assets/vehicles/")

    def check_person(self,items):
         pass

    def kamikaze(self):
        pass