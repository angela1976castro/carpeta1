# Archivo: pirate_adventure.py
import pirate_functions
import pirate_riddles 

def ask_question(preguntas, respuestas):
    user_answer = input(preguntas + " ").lower()
    return user_answer == respuestas

def start_adventure():
    print("¡Bienvenido a la aventura pirata!")
    print(pirate_functions.find_treasure_map())
    map_data = "T0G9P4B6W7K2"  # Coordenadas ficticias del tesoro encriptadas
    x, y = pirate_functions.decode_map(map_data)
    print(pirate_functions.dig_treasure(x, y))
    print("\n¡Felicidades, has encontrado el tesoro! Ahora, resuelve los siguientes acertijos para obtener más recompensas:")

    for preguntas, respuestas in pirate_riddles.riddles.items():
        if ask_question(preguntas, respuestas):
            print("¡Respuesta correcta! ¡Ganas una moneda de oro!\n")
        else:
            print("¡Respuesta incorrecta! ¡Sigue intentando!\n")
            break
    else:
        print("¡Has respondido correctamente a todos los acertijos y ganado el juego!")

if __name__ == "__main__":
    start_adventure()
