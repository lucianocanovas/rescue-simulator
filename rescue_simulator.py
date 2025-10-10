import pygame
import sys
from src.map_manager import *

def draw_board(screen, manager : MapManager, cell_size):
    
    for x, row in enumerate(manager.board):
        for y, cell in enumerate(row):
            rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size) #Pygame necesita coordenadas en píxeles
            #Cada celda del tablero mide cell_size × cell_size píxeles.

            if cell == 0:  # Si la celda esta vacia, la pinta de gris.
                color = (255, 255, 255)
                pygame.draw.rect(screen, color, rect) #Cada vez que se instancia un color para una posicion de celda, se debe poner+
                #pygame.draw.rect y el color, sino se agarra el ultimo valor
            
            elif cell == "person":
                generalice_adjustement(manager.people,cell_size,screen,x,y)

            elif cell == "mine":
                generalice_adjustement(manager.mines,cell_size,screen,x,y)
            
            elif cell == "medkit": 
                generalice_adjustement(manager.medkit,cell_size,screen,x,y)
            
            elif cell == "weapon": 
                generalice_adjustement(manager.weapons,cell_size,screen,x,y)
            
            elif cell == "clothes": 
                generalice_adjustement(manager.clothes,cell_size,screen,x,y)   
            
            elif cell == "food": 
                generalice_adjustement(manager.food,cell_size,screen,x,y)
            
            else:
                color = (255, 255, 255)
                pygame.draw.rect(screen, color, rect)
            
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Dibuja el borde de cada celda

    for vehicle in manager.vehicles:
        x, y = vehicle.position
        sprite = vehicle.current_sprite
        sprite_s = pygame.transform.scale(sprite, (cell_size, cell_size))
        screen.blit(sprite_s, (x * cell_size, y * cell_size))

def generalice_adjustement(object,cell_size,screen,x,y):
        sprite = object[0].current_sprite
        scale_w = cell_size
        scale_h = cell_size
        sprite_s = pygame.transform.scale(sprite, (scale_w, scale_h))
        sprite_s = pygame.transform.scale(sprite, (scale_w, scale_h))
        # centrar: posición = topleft de la celda + offset
        offset_x = (cell_size - scale_w) // 2
        offset_y = (cell_size - scale_h) // 2
        screen.blit(sprite_s, (y * cell_size + offset_x, x * cell_size + offset_y))
        return

def main():
    ppl_cycle_count = 0
    pygame.init()
    manager = MapManager() 
    manager.generate_map()

     # --- calcular cell_size dinámico según pantalla ---
    info = pygame.display.Info()
    screen_w, screen_h = info.current_w, info.current_h

    cols, rows = manager.width, manager.height
    cell_w = screen_w // cols
    cell_h = screen_h // rows
    cell_size = max(4, min(cell_w-2, cell_h-2))  # Evita valores muy chicos

    # Crear ventana con tamaño ajustado
    screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
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
                draw_board(screen, manager,cell_size)  # Dibuja el tablero y los objetos
                
                manager.vehicles[0].move("right")  # Mueve el primer vehículo a la derecha
                # Actualiza el sprite de la persona para animación

                manager.people[0].current_sprite = manager.people[0].sprites[0][ppl_cycle]
                ppl_cycle_count += 1  # Incrementa el contador de ciclos de animación

        pygame.display.flip()
        clock.tick(60) #60 fps

if __name__ == "__main__":
    main()