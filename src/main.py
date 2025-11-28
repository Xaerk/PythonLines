import pygame
import os
import menu
from Algoritmos.linea_dda import DDA
from Algoritmos.linea_bresenham import Bresenham
from Algoritmos.circulo_dda import Circulo_DDA
from Algoritmos.circulo_punto_medio import Punto_Medio

pygame.init()
screen = pygame.display.set_mode((854, 480))
asset_path = os.path.join("..", "assets")


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

running = True
while running:
    if not process_events():
        break

    option = menu.options()

    if not process_events():
        break

    if option == 1:
        x1, y1, x2, y2, color = menu.datos_linea()
        DDA.dibujar_DDA(screen, x1, y1, x2, y2, color)
    elif option == 2:
        x1, y1, x2, y2, color = menu.datos_linea()
        Bresenham.dibujar_Bresenham(screen, x1, y1, x2, y2, color)
    elif option == 3:
        x1, y1, r, color = menu.datos_circulo()
        Circulo_DDA.circulo_DDA(screen, x1, y1,r,color)
    elif option == 4:
        x1, y1, radio, color = menu.datos_circulo()
        Punto_Medio.Circulo_Medio(screen, x1, y1, radio, color)
    pygame.display.flip()

pygame.quit()