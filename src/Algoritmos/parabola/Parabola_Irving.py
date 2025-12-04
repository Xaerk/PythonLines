

def dibujar_parabola(surface, x1, y1, puntos, color):
    surface.set_at((x1, y1), color)
    cont = 1
    x=0 #vertice horizontal
    y=0 #vertice vertical
    p=1 #factor de apertura

    while cont < puntos:
        cont += 1  # Contamos esta iteración

        # Actualizar y siempre (parábola vertical)
        y += 1

        # Aplicar algoritmo de punto medio
        if p <= 0:
            p = p + 1
        else:
            x += 1
            p = p - 2 * x + 1
        # Dibujar puntos simétricos
        surface.set_at((x1 + x, y1 + y), color)  # Derecho abajo
        surface.set_at((x1 - x, y1 + y), color)  # Izquierdo abajo