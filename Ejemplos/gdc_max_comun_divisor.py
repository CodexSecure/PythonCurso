def calcular_gcd(a, b):
    """
    Calcula el Máximo Común Divisor (GCD) de dos números enteros
    mostrando paso a paso cómo funciona el algoritmo de Euclides.

    Parámetros:
      a -- primer número entero
      b -- segundo número entero

    Retorna:
      El valor del GCD (máximo común divisor)
    """

    # Guardamos los valores iniciales (solo para mostrar en pantalla)
    x, y = a, b

    print(f"\nCalculando gcd({x}, {y}):")
    paso = 1  # Contador para mostrar el número de paso

    # Mientras el divisor (b) no sea cero, seguimos el proceso
    while b != 0:
        residuo = a % b  # Calculamos el residuo de la división
        print(f"Paso {paso}: {a} % {b} = {residuo}")
        
        # Intercambiamos valores: el divisor pasa a ser el nuevo 'a',
        # y el residuo pasa a ser el nuevo 'b'
        a, b = b, residuo
        paso += 1  # Aumentamos el contador

    # Cuando b llega a 0, el último valor de 'a' es el GCD
    print(f"\n✅ El GCD({x}, {y}) es {a}")
    return a  # Devolvemos el resultado


# --- Ejemplo de uso ---
# Tenemos dos dimensiones, por ejemplo, una imagen de 562x221 píxeles
dimension = [562, 221]

# Llamamos a la función con esos valores
resultado = calcular_gcd(dimension[0], dimension[1])

# Calculamos el aspect ratio simplificado usando el GCD obtenido
print(f"\nRelación de aspecto (ratio): {dimension[0] // resultado}:{dimension[1] // resultado}")
print(f"GCD encontrado: {resultado}")
