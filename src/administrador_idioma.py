import json

#Importar archivo Json del texto
with open('texts.json', 'r', encoding='utf-8') as file:
    texto = json.load(file)

idioma = 'es'

# Cambia el idioma actual
def set_idioma(lang):
    global idioma
    idioma = lang

# obtener clave
def txt(key):
    return texto[idioma][key]