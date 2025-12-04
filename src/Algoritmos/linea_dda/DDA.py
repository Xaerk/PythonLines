import os #poder interactuar con el sistema operativo


def dibujar_DDA(surface,x1,y1,x2,y2,color):

#Algoritmo DDA para dibujar
#Vamos a calcular las diferenciales entre los puntos
    dx = x2 - x1
    dy = y2 - y1

#determinar los pasoso necesarios para realizar la linea
#usamos el valor mayor para ver cual sera los pixeles continuos

    pasos = max(abs(dx), abs(dy))


    if pasos == 0:
        surface.set_at((int(x1), int(y1)), color)
        return

    #calcular cuando moverson en cada paso
    x_increment = dx / pasos #cuando avanza x por paso
    y_increment = dy / pasos # cuando avanza y por paso
    #punto inicial
    x = x1
    y = y1

    #bucle para avanzar utilizando for - dibujar cada punto de la linea
    for i in range(pasos + 1):
        #Dibujar pixel en el punto actual si es necesario redondearlo a un numero entero
        surface.set_at((int(round(x)), int(round(y))), color)
        #avanzar a la siguiente posicion
        x += x_increment
        y += y_increment

