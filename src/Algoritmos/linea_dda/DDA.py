import pygame #libreria para crear
import os #poder interactuar con el sistema operativo
pygame.init()#iniciador de la libreria

#crear ventana
 #crear ventana con la resolucion seleccionada
#Esconder cursor en la pantalla para que esté el pixelado

# Esconder cursor del sistema
pygame.mouse.set_visible(False)
def dibujar_DDA(surface):
    print("--------------Algoritmo DDA-------------")
    x1 = int(input("x1:"))
    y1 = int(input("Y1:"))
    x2 = int(input("X2:"))
    y2 = int(input("Y2:"))#con esto aseguramos que debe escribir un valor a la variable seleccionada

    print("\nColor RGB:")
    r = int(input("Rojo (0-255):"))
    g = int(input("Verde (0-255):"))
    b = int(input("Azul (0-255):"))
    color = (r, g, b) #con esto podremos elegir el nivel de intensidad del color seleccionado segun su valor


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

