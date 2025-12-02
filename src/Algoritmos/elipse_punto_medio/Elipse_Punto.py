import pygame
pygame.init()

def elipse_medio(surface, x, y, rx, ry, color):
    xc =0
    yc= ry

    #parametros de desicion
    rx2 = rx * rx
    ry2 = ry * ry
    dos_rx2 = 2 * rx2
    dos_ry2 = 2 * ry2

    #region1
    p1 = ry2-(rx2* ry)+ (0.25 * rx2) #parametro de desicion

    def dibujar_puntos(surface, xc, yc, x, y, color):
        surface.set_at((x + xc, y + yc),color)
        surface.set_at((x - xc, y + yc),color)
        surface.set_at((x + xc, y - yc),color)
        surface.set_at((x - xc, y - yc),color)

#recorrido region 1
    while dos_ry2 * xc< dos_rx2 * yc:

        dibujar_puntos(surface, xc, yc, x, y, color)
        xc = xc + 1

        if p1 < 0:
            p1 = p1 + dos_ry2 * xc + ry2
        else:
            yc = yc - 1
            p1 = p1 + dos_ry2 * xc - dos_rx2 * yc + ry2


    p2 = ry2 * (xc + 0.5) * (xc + 0.5) + rx2 * (yc - 1) * (yc - 1) - rx2 * ry2
    #recorrido region 2
    while yc >= 0:
        dibujar_puntos(surface, xc, yc, x, y, color)
        yc = yc- 1
        if p2 > 0:
            p2 = p2 - dos_rx2 * yc + rx2
        else:
            xc = xc+ 1
            p2=p2+ dos_ry2* xc - dos_rx2 * yc + rx2


