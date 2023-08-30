# Archivo: mechanical_diagnosis.py
import mechanical_problems as mp

def preguntar_problema(problemas, puntaje):
    print(problemas["Problema"])
    # aquí nos imprime desde problemas el problema que se presenta 
    solucion_usuario = input("¿Cuál crees que es la solución? ").lower()
    if solucion_usuario == problemas["Solución"].lower():
        print(f"¡Respuesta correcta! Ganaste {puntaje} puntos.\n")
        return puntaje
    else:
        print("¡Respuesta incorrecta! Sigue intentando.\n")
        return 0

def comenzar_diagnostico():
    print("¡Bienvenido al simulador de diagnóstico de problemas en vehículos!")
    print("Debes resolver problemas mecánicos y proporcionar las soluciones adecuadas.")
    total_puntaje = 0
    for index, problemas in enumerate(mp.problems, start=1):
        puntaje = len(mp.problems) - index + 1  # Asignar más puntos a los problemas más difíciles
        total_puntaje += preguntar_problema(problemas, puntaje)
    print(f"¡Diagnóstico completado! Puntaje total: {total_puntaje} puntos.")

"""for index, problem in enumerate(mp.problems, start=1):: Este es un bucle forque 
itera sobre la lista de problemas mecanicos mp.problems. 
La función enumerate()se utiliza para obtener tanto el índice como el problema
en cada iteración. La opción start=1 se utiliza para comenzar el índice en 1 en lugar de 0.
score = len(mp.problems) - index + 1: Aquí se calcula el puntaje asignado al problema actual.
El puntaje se determina restando el índice actual (empezando en 1) del total de problemas 
en la listalen(mp.problems)) y sumando 1 al resultado. Esta fórmula asigna puntajes más 
altos a los problemas más difíciles, ya que los problemas al final de la lista
tienen índices más bajos.
total_score += ask_problem(problem, score): En cada iteración del bucle,
 llamamos a la función ask_problem()para presentar el problema actual altotal_score.
 En resumen, esta línea de código recorre la lista de problemas mecánicos,
calcula el puntaje asignado a cada problema según su dificultad, 
y luego llama a la función ask_problem()para presentartotal_score. 
Al final del bucle, `totaltotal_score
contendrá la suma de los puntajes obtenidos por el estudiante en 
función de las respuestas correctas a los problemas.
"""






if __name__ == "__main__":
    comenzar_diagnostico()
