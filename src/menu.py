#Loop de menú principal en terminal, ajá

option = 0
def options():
    print("Que figura desea graficar?")
    print("1) Linea recta usando DDA")
    print("2) Linea recta usando Bresenham")
    print("3) Circulo usando DDA")
    print("4) Circulo Punto Medio")
    print("5) Elipse Punto Medio")
    print("6) Poligono Regular")
    option = int(input("Opción:"))
    if option == 1:
        return 1
    elif option == 2:
        return 2
    elif option == 3:
        return 3
    if option == 4:
        return 4
    if option == 5:
        return 5
    if option == 6:
        return 6


def datos_linea():
    print("--------------Línea-------------")
    x1 = int(input("x1:"))
    y1 = int(input("Y1:"))
    x2 = int(input("X2:"))
    y2 = int(input("Y2:"))#con esto aseguramos que debe escribir un valor a la variable seleccionada

    print("\nColor RGB:")
    r = int(input("Rojo (0-255):"))
    g = int(input("Verde (0-255):"))
    b = int(input("Azul (0-255):"))
    color = (r, g, b) #con esto podremos elegir el nivel de intensidad del color seleccionado segun su valor
    return x1,y1,x2,y2,color

def datos_circulo():
    print("--------------Circulo-------------")
    x1 = int(input("x:"))
    y1 = int(input("Y:"))
    radio = int(input("Radio:"))

    print("\nColor RGB:")
    r = int(input("Rojo (0-255):"))
    g = int(input("Verde (0-255):"))
    b = int(input("Azul (0-255):"))
    color = (r, g, b)
    return x1,y1,radio,color

def puntos_elipse():
    print("--------------Elipse-------------")
    x = int(input("x:"))
    y = int(input("y:"))
    rx = int(input("Radio X:"))
    ry = int(input("Radio Y:"))

    print("\nColor RGB:")
    r = int(input("Rojo (0-255):"))
    g = int(input("Verde (0-255):"))
    b = int(input("Azul (0-255):"))
    color = (r, g, b)
    return x, y, rx, ry, color

def datos_poligono():
    print("--------------Poligono-------------")
    x = int(input("x:"))
    y = int(input("Y:"))
    radio = int(input("Distancia:"))
    lados = int(input("Lados:"))
    print("\nColor RGB:")
    r = int(input("Rojo (0-255):"))
    g = int(input("Verde (0-255):"))
    b = int(input("Azul (0-255):"))
    color = (r, g, b)
    return x,y,radio,lados,color




