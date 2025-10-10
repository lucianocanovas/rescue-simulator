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
        # Try to create a standard 1x6 sprite matrix. Some sheets are single-frame;
        # normalize them so code can index sprites[0][frame_index] safely.
        try:
            frames = load_sprite(sprite_path, sheet_width, sheet_height, 1, 6)
        except Exception:
            # If the standard split failed (for single-frame images), load as single frame
            single = sheet.subsurface(pygame.Rect(0, 0, sheet_width, sheet_height)).copy()
            # build a 1x6 frame list by duplicating the single frame
            frames = [[single for _ in range(6)]]

        # Ensure the outer structure is rows -> columns and rows>=1 and columns>=6
        if len(frames) == 0:
            # fallback: create a 1x6 grid with blank surface
            blank = pygame.Surface((sheet_width, sheet_height), pygame.SRCALPHA)
            frames = [[blank for _ in range(6)]]
        elif len(frames[0]) < 6:
            # duplicate frames to reach 6 columns
            row = frames[0]
            while len(row) < 6:
                row.append(row[-1])
            frames[0] = row

        self.sprites = frames
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