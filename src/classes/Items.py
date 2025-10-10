from src.visualization import load_sprite
import pygame
from pathlib import Path

class Item :
    pygame.init()
    def __init__(self, value : int, position : tuple[int, int], sprite_path : str):
        path = Path(sprite_path).resolve()
        sheet = pygame.image.load(str(path))
        sheet_width, sheet_height = sheet.get_size()
        self.value = value
        self.position = position
        self.sprites = load_sprite(sprite_path, sheet_width // 6, sheet_height // 1, 1, 6)
        self.current_sprite = self.sprites[0][0]
        
class Person (Item):
    def __init__(self, position, sprite_path = "assets/resources/person_idle.png"):
        super().__init__(50, position, sprite_path)

class Medkit (Item):
    def __init__(self, position, sprite_path = "assets/resources/medkit.png"):
        super().__init__(20, position, sprite_path)

class Clothes (Item):
    def __init__(self, position, sprite_path = "assets/resources/clothes.png"):
        super().__init__(5, position, sprite_path)

class Food (Item):
    def __init__(self, position, sprite_path = "assets/resources/food.png"):
        super().__init__(10, position, sprite_path)

class Weapons (Item):
    def __init__(self, position, sprite_path = "assets/resources/weapon.png"):
        super().__init__(50, position, sprite_path)