"""
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
 """
# Versión clásica con if / elif / else
def fizz_buzz_if(n=100):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Versión moderna con match / case (Python 3.10+)
def fizz_buzz_match(n=100):
    for i in range(1, n + 1):
        match (i % 3 == 0, i % 5 == 0):
            case (True, True):
                print("FizzBuzz")
            case (True, False):
                print("Fizz")
            case (False, True):
                print("Buzz")
            case _:
                print(i)


# Bloque principal: solo se ejecuta si el archivo se ejecuta directamente
if __name__ == "__main__":
    print("=== Fizz Buzz con if/elif/else ===")
    fizz_buzz_if(20)

    print("\n=== Fizz Buzz con match/case ===")
    fizz_buzz_match(20)

