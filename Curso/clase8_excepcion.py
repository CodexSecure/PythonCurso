"""
def dividir(a, b):
    if b == 0:
        raise ValueError("No puedes dividir entre cero.")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as error:
    print("Se detectó un error:", error)
"""

"""
# Ejemplo de manejo de excepciones

# Programa que se repite hasta que el usuario escribe "salir"

while True:  # Bucle infinito
    try:
        numero = int(input("\nIntroduce un número (o escribe '0' para salir): "))

        if numero == 0:  # Condición de salida
            print("Saliendo del programa...")
            break  # Rompe el bucle y termina el programa

        resultado = 10 / numero
        print(f"El resultado de 10 / {numero} es: {resultado:.2f}")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    except ValueError:
        print("Error: debes introducir un número válido.")
    except Exception as e:
        print("Error inesperado:", e)
    finally:
        print("Intento completado.")
# El bloque finally se ejecuta siempre, haya o no error9

"""

while True:  # Bucle infinito
    try:
        # Pedimos al usuario un número
        numero = input("Introduce un número entero: ")

        # Intentamos convertir a entero
        numero_int = int(numero)

        # Si no da error, es un número entero
        print(f"¡Correcto! {numero_int} es un número entero.")
        break  # Salimos del bucle

    except ValueError:
        # Se ejecuta si no se puede convertir a entero
        print(f"'{numero}' no es un número entero. Inténtalo de nuevo.")

