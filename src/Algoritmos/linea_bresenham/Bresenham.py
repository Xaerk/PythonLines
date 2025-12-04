#copypaste de DDA xD


# formula de bresenham en horizontal
def dibujar_BresenhamH(surface,x1,y1,x2,y2,color):
    if x1 > x2:
        x1,x2 = x2,x1
        y1,y2 = y2,y1

    dx = x2 - x1
    dy = y2 - y1

    if dy < 0:
        dir = -1
    else:
        dir = 1

    dy = dy * dir

    if dx != 0:
        y = y1
        p = 2*dy - dx
        for i in range(dx+1):
            surface.set_at((x1 + i, y),color)
            num = x1 + i
            #print("(" + str(num) + "," + str(y) + ")") #testing code (Uncomment if needed)
            if p >=0:
                y += dir
                p = p - 2*dx
            p = p + 2*dy

#Formula de bresenham en vertical
def dibujar_BresenhamV(surface,x1,y1,x2,y2,color):
    if y1 > y2:
        x1,x2 = x2,x1
        y1,y2 = y2,y1

    dx = x2 - x1
    dy = y2 - y1

    if dx < 0:
        dir = -1
    else:
        dir = 1

    dx = dx * dir

    if dy != 0:
        x = x1
        p = 2*dx - dy
        for i in range(dy+1):
            surface.set_at((x, y1 + i),color)
            num = y1 + i
            #print("(" + str(x) + "," + str(num)+")") #testing code (uncomment if needed)
            if p >=0:
                x = x + dir
                p = p - 2*dy
            p = p + 2*dx


def dibujar_Bresenham(surface,x1,y1,x2,y2,color):
    if abs(x2 - x1) > abs(y2 - y1):
        dibujar_BresenhamH(surface,x1,y1,x2,y2,color)
    else:
        dibujar_BresenhamV(surface,x1,y1,x2,y2,color)