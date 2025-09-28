import pygame
import sys
from src.map_manager import *

cell_size = 20

def draw_board(screen, manager : MapManager):
    for x, row in enumerate(manager.board):
        for y, cell in enumerate(row):
            rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size)

            if cell == 0:  # vacío
                color = (200, 200, 200)
            elif cell == "person":
                screen.blit(manager.people[0].current_sprite, (x * cell_size, y * cell_size))
            elif cell == "mine":
                color = (200, 0, 0)
            else:
                color = (50, 50, 50)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # borde

    for vehicle in manager.vehicles:
        x, y = vehicle.position
        screen.blit(vehicle.current_sprite, (x * cell_size, y * cell_size))

def main():
    ppl_cycle_count = 0
    pygame.init()
    manager = MapManager()
    manager.generate_map()

    screen = pygame.display.set_mode((manager.width * cell_size, manager.height * cell_size))
    clock = pygame.time.Clock()

    update_event = pygame.USEREVENT + 1
    pygame.time.set_timer(update_event, 500)  # lanza un evento cada 0.5s

    while True:
        ppl_cycle = ppl_cycle_count % 6
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == update_event:
                """----------------------------------------------------------------"""
                print("Actualizo el estado del juego")
                screen.fill((255, 255, 255))
                draw_board(screen, manager)
                manager.vehicles[0].move("right")
                "------------------------------------------------------------------"""
                manager.people[0].current_sprite = manager.people[0].sprites[0][ppl_cycle]
                ppl_cycle_count += 1

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()