import pygame
import sys

# Variables
WIDTH = 800
HEIGHT = 600
FPS = 60

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Window dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rescue Simulator")

# Clock for controlling frame rate

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((135, 206, 235))
    pygame.display.flip()
    clock.tick(FPS)