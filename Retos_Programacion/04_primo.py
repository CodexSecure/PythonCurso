"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
# Función para verificar si un número es primo
def es_primo(n):
    # Los números menores o iguales a 1 no son primos
    if n <= 1:
        return False

    # Revisar divisores desde 2 hasta la raíz cuadrada de n (inclusive)
    for i in range(2, int(n**0.5) + 1):
        # Si n es divisible por i, no es primo
        if n % i == 0:
            return False

    # Si no encontró divisores, es primo
    return True

# Imprimir números primos entre 1 y 100
"""
for num in range(1, 101):
    if es_primo(num):
        print(num)
"""
primos = [num for num in range(1, 101) if es_primo(num)]
print(f"Números primos entre 1 y 100: {primos}")