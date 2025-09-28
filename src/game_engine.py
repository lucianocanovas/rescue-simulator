import pygame
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rescue Simulator")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color
    screen.fill((135, 206, 235))

    # Update the display
    pygame.display.flip()
    clock.tick(60),