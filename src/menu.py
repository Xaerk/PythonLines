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
