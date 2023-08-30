# Archivo: animal_game.py
import animal_riddles as ar

def ask_question(riddle, score):
    user_answer = input(riddle["Pista"] + " ").lower()
    if user_answer == riddle["Respuesta"]:
        print(f"¡Respuesta correcta! Ganaste {score} puntos.\n")
        return score
    else:
        print("¡Respuesta incorrecta! Sigue intentando.\n")
        return 0

def start_game():
    print("¡Bienvenido al juego de adivinanzas de animales!")
    print("Debes responder correctamente las pistas para adivinar el animal oculto.")
    total_score = 0
    for index, riddle in enumerate(ar.riddles, start=1):
        score = len(ar.riddles) - index + 1  # Asignar más puntos a las pistas más difíciles
        total_score += ask_question(riddle, score)
    print(f"¡Felicidades! Has adivinado todos los animales y ganado el juego. Puntaje total: {total_score} puntos.")

if __name__ == "__main__":
    start_game()

