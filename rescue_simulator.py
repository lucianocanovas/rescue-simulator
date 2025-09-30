import pygame
import sys
from src.map_manager import *

cell_size = 20

def draw_board(screen, manager : MapManager):
    for x, row in enumerate(manager.board):
        for y, cell in enumerate(row):
            rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size) #Pygame necesita coordenadas en píxeles
            #Cada celda del tablero mide cell_size × cell_size píxeles.
            if cell == 0:  # Si la celda esta vacia, la pinta de gris.
                color = (200, 200, 200)
            elif cell == "person": #Si la celda tiene una persona, coloca su sprite
                screen.blit(manager.people[0].current_sprite, (x * cell_size, y * cell_size))
            elif cell == "mine": #Si hay una mina, pinta la celda de rojo
                color = (200, 0, 0)
            else:
                color = (50, 50, 50)

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Dibuja el borde de cada celda

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
  
    while True:  # Bucle principal del juego
        ppl_cycle = ppl_cycle_count % 6  # Calcula el ciclo de animación de la persona
        for event in pygame.event.get():  # Maneja los eventos de Pygame
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                pygame.quit()
                sys.exit()
            elif event.type == update_event:  # Si ocurre el evento de actualización
                # Actualiza el estado del juego
                print("Actualizo el estado del juego")
                screen.fill((255, 255, 255))  # Limpia la pantalla
                draw_board(screen, manager)  # Dibuja el tablero y los objetos
                manager.vehicles[0].move("right")  # Mueve el primer vehículo a la derecha
                # Actualiza el sprite de la persona para animación
                manager.people[0].current_sprite = manager.people[0].sprites[0][ppl_cycle]
                ppl_cycle_count += 1  # Incrementa el contador de ciclos de animación

        pygame.display.flip()
        clock.tick(60) #60 fps

if __name__ == "__main__":
    main()