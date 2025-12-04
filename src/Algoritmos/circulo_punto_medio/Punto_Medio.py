

def Circulo_Medio(surface,x,y,radio,color):

    xc = 0
    yc = radio
    p = 1- radio

    def dibujar_octante(surface,x,y,xc,yc,color):
        surface.set_at((x + xc,y + yc),color)
        surface.set_at((x - xc,y + yc), color)
        surface.set_at((x + xc,y - yc), color)
        surface.set_at((x - xc,y - yc), color)
        surface.set_at((x + yc,y + xc), color)
        surface.set_at((x - yc,y + xc), color)
        surface.set_at((x + yc,y - xc), color)
        surface.set_at((x - yc,y - xc), color)


    while xc <= yc:
        #dibujar
        dibujar_octante(surface,x,y,xc,yc,color)
        xc = xc + 1#actualizar x
            #Parametro de edicion
        if p < 0:
            p = p + 2 * xc + 1 #se avanza solo x, y se mantiene
        else:
            yc = yc -1
            p=p + 2 *(xc-yc)+1#avanzar y


