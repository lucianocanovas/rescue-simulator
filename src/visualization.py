import pygame
import os

def load_sprite(path, frame_width, frame_height, rows, columns):
    sheet = pygame.image.load(path).convert_alpha()
    frames = []

    for row in range(rows):
        row_frames = []
        for column in range(columns):
            rectangle = pygame.Rect(column * frame_width, row * frame_height, frame_width, frame_height)
            frame = sheet.subsurface(rectangle)
            row_frames.append(frame)
        frames.append(row_frames)
    return frames