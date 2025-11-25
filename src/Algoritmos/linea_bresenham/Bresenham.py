#copypaste de DDA xD
import pygame
pygame.init()


def dibujar_Bresenham(surface):
    print("--------------Algoritmo Bresenham--------------")
    x0 = int(input("x1:"))
    y0 = int(input("Y1:"))
    x1 = int(input("X2:"))
    y1 = int(input("Y2:"))

    print("\nColor RGB:")
    r = int(input("Rojo (0-255):"))
    g = int(input("Verde (0-255):"))
    b = int(input("Azul (0-255):"))
    color = (r, g, b)

    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        surface.set_at((int(x0 + x*xx), int(y0+x*xy+y*yy)), color)
        if D >= 0:
            y += 1
            D -= 2 * dx
        D += 2 * dy

#TODO support lines going to the left