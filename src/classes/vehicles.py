import pygame.image

import items, map, mines

class Vehicle:
    def __init__(self, capacity,x,y,image_path):
        self.position = [x,y]
        self.capacity = capacity
        self.image = pygame.image.load(image_path)

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
        super().__init__(2, x, y,)


class Truck(Vehicle):
    def __init__(self, x, y):
        super().__init__(3, x, y,)


class Car(Vehicle):
    def __init__(self, x, y):
        super().__init__(1, x, y)


class Motorcycle(Vehicle):
    def __init__(self, x, y):
        super().__init__(1, x, y,)

    def check_person(self,items):
         pass

    def kamikaze():
        pass