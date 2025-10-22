"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
 """
def fibonacci(n):
    # Inicializamos los dos primeros números de la secuencia
    a, b = 0, 1

    # Creamos una lista vacía donde guardaremos los números de Fibonacci
    resultado = []

    # Repetimos n veces para obtener los primeros n números de Fibonacci
    for _ in range(n):
        resultado.append(a)  # Añadimos el número actual a la lista
        a, b = b, a + b     # Actualizamos los valores: 'a' toma el valor de 'b', y 'b' la suma de ambos

    return resultado  # Devolvemos la lista con la secuencia generada

# Ejemplo: obtener los primeros 15 números de Fibonacci
print(fibonacci(15))
