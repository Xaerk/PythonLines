import math


def parabola_medio(surface, vx, vy, p, orientation, length, color):


    def dibujar_simetria(surface, x, y, vx, vy, orientation, color):
            if orientation == 1:
                surface.set_at((int(vx + y), int(vy + x)), color)
                surface.set_at((int(vx + y), int(vy - x)), color)
            elif orientation == 2:
                surface.set_at((int(vx - y), int(vy + x)), color)
                surface.set_at((int(vx - y), int(vy - x)), color)
            elif orientation == 3:
                surface.set_at((int(vx + x), int(vy - y)), color)
                surface.set_at((int(vx - x), int(vy - y)), color)
            elif orientation == 4:
                surface.set_at((int(vx + x), int(vy + y)), color)
                surface.set_at((int(vx - x), int(vy + y)), color)

    # Initialize parameters based on orientation
    if orientation == 1:
        for y in range(length + 1):
            # x² = 4py, so x = sqrt(4py)
            x_squared = 4 * p * y
            if x_squared >= 0:
                x = int(math.sqrt(x_squared))
                dibujar_simetria(surface, x, y, vx, vy, orientation, color)


    elif orientation == 2:
        for y in range(length +1):
            # x² = 4py, so x = sqrt(4py)
            x_squared = 4 * p * y
            if x_squared >= 0:
                x = int(math.sqrt(x_squared))
                dibujar_simetria(surface, x, y, vx, vy, orientation, color)


    elif orientation == 3:
        # la parabola arriba inicia con este parametro de desicion: x² = 4py
        # se decide cuando incrementar y a su vez x
        for y in range(length + 1):
            # x² = 4py, so x = sqrt(4py)
            x_squared = 4 * p * y
            if x_squared >= 0:
                x = int(math.sqrt(x_squared))
                dibujar_simetria(surface, x, y, vx, vy, orientation, color)


    elif orientation == 4:
        # la parabola abajo inicia con este parametro de desicion: x² = 4py
        for y in range(length + 1):
            # x² = 4py, so x = sqrt(4py)
            x_squared = 4 * p * y
            if x_squared >= 0:
                x = int(math.sqrt(x_squared))
                dibujar_simetria(surface, x, y, vx, vy, orientation, color)

    else:
        return