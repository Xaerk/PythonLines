import pygame
import os
import menu
from Algoritmos.linea_dda import DDA
from Algoritmos.linea_bresenham import Bresenham

pygame.init()

screen = pygame.display.set_mode((854, 480))




asset_path = os.path.join("..","assets") #<- variable de la ruta a assets


# Mantener la ventana corriendo hasta que se presione la X
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    option = menu.options()
    if option == 1:
        x1,y1,x2,y2,color = menu.datos_linea()
        DDA.dibujar_DDA(screen,x1,y1,x2,y2,color)
    elif option == 2:
        x1, y1, x2, y2, color = menu.datos_linea()
        Bresenham.dibujar_Bresenham(screen, x1, y1, x2, y2, color)
    pygame.display.flip()


pygame.quit()
