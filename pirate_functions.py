# Archivo: pirate_functions.py

def find_treasure_map():
    return "X marks the spot! Follow the map to find the treasure."

def decode_map(map_data):
    # Aquí se implementaría una función que decodifique el mapa para obtener coordenadas.
    # Pero dado que no es el objetivo principal del ejercicio, simplemente retornaremos coordenadas ficticias.
    return (10, 15)

def dig_treasure(x, y):
    return f"¡Has encontrado el tesoro en las coordenadas ({x}, {y})!"

# Funciones lambda para encriptar y desencriptar mensajes
encrypt = lambda msg: ''.join([chr(ord(c) + 3) for c in msg])
decrypt = lambda msg: ''.join([chr(ord(c) - 3) for c in msg])

