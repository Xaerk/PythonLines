import pygame
pygame.init()
import math
from ..linea_bresenham import Bresenham
def poligono_regular(surface, xc, yc, radio, lados, color):

    #obtener el angulo y convertirlo en radianes
    angulo = 360 / lados
    angulo = angulo * (math.pi / 180)

    #puntos en el circulo para dibujar el poligono
    puntos = []

    #obtener puntos
    for i in range(0,lados):
        x = xc + radio * math.cos(angulo*i)
        y = yc + radio * math.sin(angulo*i)
        puntos.append((x,y))


    #Loop para renderizarlo (no quiero que algo tan bultoso este en main)
    for i in range (0,lados):
        x1,y1 = puntos[i]
        if puntos[i] == puntos[lados-1]:
            x2, y2 = puntos[0]
        else:
            x2, y2 = puntos[i+1]

        Xrender1 = int(round(x1))
        Yrender1 = int(round(y1))
        Xrender2 = int(round(x2))
        Yrender2 = int(round(y2))
        print(Xrender1, Yrender1, Xrender2, Yrender2)
        Bresenham.dibujar_Bresenham(surface, Xrender1, Yrender1, Xrender2,Yrender2, color)


    return

