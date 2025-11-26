#Loop de menú principal en terminal, ajá

option = 0
def options():
    print("Que figura desea graficar?")
    print("1) Linea recta usando DDA")
    print("2) Linea recta usando Bresenham")
    option = int(input("Opción:"))
    if option == 1:
        return 1
    elif option == 2:
        return 2
def datos_linea():
    print("--------------Líneas-------------")
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
