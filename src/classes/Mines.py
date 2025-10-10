import pygame

class Mine:
    def __init__(self, x, y, radius_x, radius_y, sprite_path):
        self.position = [x, y]
        self.radiusX = radius_x
        self.radiusY = radius_y
        self.current_sprite = pygame.image.load(sprite_path)

class MineG2(Mine):
    def __init__(self, x, y):
        super().__init__(x, y, 7, 7,sprite_path="assets/resources/mine.png")

    def teleport(self):
        pass