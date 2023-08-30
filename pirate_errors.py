# Archivo: pirate_errors.py

def divide_numbers(a, b):
    try:
        result = a / b
        return f"El resultado de la división es: {result}"
    except ZeroDivisionError:
        return "¡No puedes dividir entre cero, eso está prohibido en el mundo pirata!"
    except Exception as e:
        return f"Ocurrió un error desconocido: {str(e)}"
