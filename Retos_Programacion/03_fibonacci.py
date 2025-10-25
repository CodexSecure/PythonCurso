"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */

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
"""
# ================================================================
# FIBONACCI: 10 primeros números empezando en 0
# Distintas formas de generar e imprimir la serie en Python
# ================================================================

print("\n=== 1️⃣ Versión con bucle for (simple y eficiente) ===")
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b


# ---------------------------------------------------------------
print("\n=== 2️⃣ Versión con lista (almacenando todos los valores) ===")
fibonacci = [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for num in fibonacci:
    print(num)


# ---------------------------------------------------------------
print("\n=== 3️⃣ Versión con función generadora (yield) ===")
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i, num in enumerate(fibonacci_generator()):
    if i == 10:
        break
    print(num)


# ---------------------------------------------------------------
print("\n=== 4️ Versión recursiva (básica, no eficiente) ===")
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

for i in range(10):
    print(fib_recursive(i))

# ---------------------------------------------------------------
print("\n=== 4️.1 Versión con generador infinito ===")
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 10 Fibonacci numbers
gen = fibonacci()
for _ in range(10):
  print(next(gen))


# ---------------------------------------------------------------
print("\n=== 5️⃣ Versión recursiva con memoización (lru_cache) ===")
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

for i in range(10):
    print(fib_memo(i))


# ---------------------------------------------------------------
print("\n=== 6️⃣ Versión compacta con comprensión de listas ===")
fibo = [0, 1]
[fibo.append(fibo[-1] + fibo[-2]) for _ in range(8)]
print(*fibo, sep="\n")


# ---------------------------------------------------------------
print("\n=== 7️⃣ Versión con itertools.islice (generador infinito limitado) ===")
from itertools import islice

def fibonacci_infinite():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for num in islice(fibonacci_infinite(), 10):
    print(num)


# ================================================================
print("\n✅ Fin de demostración de métodos Fibonacci (10 primeros números)")
# ================================================================
