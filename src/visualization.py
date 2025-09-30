from pathlib import Path
import pygame


def load_sprite(path,   frame_width, frame_height, rows, columns):
    path = Path(path).resolve()
    if not path.is_file():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")

    sheet = pygame.image.load(path)
    sheet_width, sheet_height = sheet.get_size()

    frames = []
    for row in range(rows):
        row_frames = []
        for column in range(columns):
            # Calculate rectangle position and size
            x = column * frame_width
            y = row * frame_height
            rect = pygame.Rect(x, y, frame_width, frame_height) #Recorre filas y columnas para recortar cada sprite

            # Validate rectangle is within sheet bounds
            if x + frame_width <= sheet_width and y + frame_height <= sheet_height:
                frame = sheet.subsurface(rect)
                frame = pygame.transform.scale(frame, (20, 20)) #Escala cada sprite a 20x20 píxeles para mantener un tamaño uniforme en pantalla.
                row_frames.append(frame)
            else:
                raise ValueError(
                    f"Frame at ({x}, {y}) with size ({frame_width}, {frame_height}) exceeds sheet dimensions ({sheet_width}, {sheet_height})")
        frames.append(row_frames)
    return frames #Devuelve la matriz de sprites