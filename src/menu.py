import administrador_idioma as admin
import colornames
from color import colornames_es

#Loop de menú principal en terminal, ajá

def seleccion_idioma():
    print("Select language / Seleccione idioma:")
    print("1. English")
    print("2. Español")
    choice = input("Choice / Opción: ")
    if choice == "1":
        admin.set_idioma('en')
        print("Language set to English")
    else:
        admin.set_idioma('es')
        print("Idioma establecido a Español")


def options():
    print(admin.txt("figure"))
    print(f"1) {admin.txt("option_1")}")
    print(f"2) {admin.txt("option_2")}")
    print(f"3) {admin.txt("option_3")}")
    print(f"4) {admin.txt("option_4")}")
    print(f"5) {admin.txt("option_5")}")
    print(f"6) {admin.txt("option_6")}")
    print(f"7) {admin.txt("option_7")}")
    print(f"8) {admin.txt("option_8")}")
    option = int(input(f"{admin.txt('option')}"))
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
    if option == 7:
        return 7
    if option == 8:
        return 8

def buscar_color_insensible(nombre_color):
    # Convierte el input en un string en minusculas sin espacios
    nombre_normalizado = nombre_color.strip().lower()

    if admin.idioma =="es":
        dict_actual = colornames_es.colors_es
    else:
        dict_actual = colornames._colors

    for nombre, rgb in dict_actual.items():
        if nombre.lower() == nombre_normalizado:
            return rgb  # Devuelve el RGB
    return None


def color_set():
    color_elegido = input(f"{admin.txt('color')}")
    if color_elegido == "1":
        print(f"\n{admin.txt('color_rgb')}")
        r = int(input(f"{admin.txt("red")}"))
        g = int(input(f"{admin.txt("green")}"))
        b = int(input(f"{admin.txt("blue")}"))
        return r, g, b
    else:
        color = buscar_color_insensible(color_elegido)
        if color == None:
            print(f"{admin.txt("color_failsafe")}")
            return 255,255,255
        else:
            return color



def datos_linea():
    print(f"--------------{admin.txt('line')}-------------")
    x1 = int(input(f"{admin.txt("x1")}"))
    y1 = int(input(f"{admin.txt("y1")}"))
    x2 = int(input(f"{admin.txt("x2")}"))
    y2 = int(input(f"{admin.txt("y2")}"))


    color = color_set()
    return x1,y1,x2,y2,color

def datos_circulo():
    print(f"--------------{admin.txt('circle')}-------------")
    x = int(input(f"{admin.txt("x")}"))
    y = int(input(f"{admin.txt("y")}"))
    radio = int(input(f"{admin.txt('radius')}"))

    #llamar funcion para obtener el color desde texto
    color = color_set()
    return x,y,radio,color

def puntos_elipse():
    print(f"--------------{admin.txt('ellipse')}-------------")
    x = int(input(f"{admin.txt('x')}"))
    y = int(input(f"{admin.txt('y')}"))
    rx = int(input(f"{admin.txt('rx')}"))
    ry = int(input(f"{admin.txt('ry')}"))

    color = color_set()
    return x, y, rx, ry, color

def datos_poligono():
    print(f"--------------{admin.txt('polygon')}-------------")
    x = int(input(f"{admin.txt('x')}"))
    y = int(input(f"{admin.txt('y')}"))
    radio = int(input(f"{admin.txt('distance')}"))
    lados = int(input(f"{admin.txt('sides')}"))
    color = color_set()
    return x,y,radio,lados,color

def datos_parabola_Irving():
    print(f"--------------{admin.txt('parabola')}-------------")
    x = int(input(f"{admin.txt('x_p')}"))
    y = int(input(f"{admin.txt('y_p')}"))
    puntos = int(input(f"{admin.txt('puntos')}"))
    color = color_set()
    return x,y, puntos,color

def datos_parabola():
    print(f"--------------{admin.txt('parabola')}-------------")
    x = int(input(f"{admin.txt('x_p')}"))
    y = int(input(f"{admin.txt('y_p')}"))
    p = int(input(f"{admin.txt('p')}"))
    orientation = int(input(f"{admin.txt('orientation')}").lower())
    puntos = int(input(f"{admin.txt('puntos')}"))
    color = color_set()
    return x,y,p, orientation, puntos, color







