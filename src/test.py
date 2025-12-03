import colornames


def buscar_color_insensible(nombre_color):
    """Busca un color sin importar mayúsculas/minúsculas"""
    nombre_normalizado = nombre_color.strip().lower()

    for nombre, rgb in colornames._colors.items():
        if nombre.lower() == nombre_normalizado:
            return nombre, rgb  # Devuelve el nombre original y el RGB
    return None


# Uso
texto = input("Inserte color: ")
resultado = buscar_color_insensible(texto)
if resultado:
    nombre_original, rgb = resultado
    print(f"Nombre original: {nombre_original}")
    print(f"RGB: {rgb}")
else:
    print("Color no encontrado")