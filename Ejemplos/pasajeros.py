import math  # Importamos math para usar math.ceil (redondeo hacia arriba)

min_pasajeros=25
max_avion=150

def decidir_vuelo(pasajeros):
    """
    Función que decide si vale la pena despegar con un avión o más,
    dependiendo del número de pasajeros.
    
    Parámetros:
    - pasajeros (int): número total de pasajeros.
    - min_pasajeros (int): mínimo de pasajeros necesarios para que valga la pena (default=25).
    - max_avion (int): capacidad máxima de un avión (default=150).
    
    Retorna:
    - Un mensaje en texto con la decisión.
    """
    
    # Caso 1: muy pocos pasajeros
    if pasajeros < min_pasajeros:
        return f"{pasajeros} pasajeros → No vale la pena despegar"
    
    # Caso 2: demasiados pasajeros para un solo avión
    elif pasajeros > max_avion:
        # Calculamos cuántos aviones hacen falta
        # math.ceil redondea hacia arriba: ej. 200/150 = 1.33 → 2 aviones
        aviones_necesarios = math.ceil(pasajeros / max_avion)
        
        return (f"{pasajeros} pasajeros → ¡Demasiados para un avión!"
                f"Se necesitan {aviones_necesarios} aviones.")
    
    # Caso 3: cantidad suficiente y dentro de la capacidad de un avión
    else:
        return f"{pasajeros} pasajeros → Vale la pena despegar con un avión"


# -------------------------------
# Ejemplos de uso
# -------------------------------
print("\n--- Usando if-elif-else ---\n")

print(decidir_vuelo(10))     # Menos de 25 → No vale la pena
print(decidir_vuelo(100))    # Entre 25 y 150 → Un avión suficiente
print(decidir_vuelo(200))    # Más de 150 → Se necesitan 2 aviones
print(decidir_vuelo(375))    # Más de 150 → Se necesitan 3 aviones


def decidir_vuelo_match(pasajeros):
    """
    Decide si vale la pena volar usando match-case (Python 3.10+).
    """
    match pasajeros:
        # Caso 1: muy pocos pasajeros
        case n if n < min_pasajeros:
            return f"{pasajeros} pasajeros → No vale la pena despegar"
        
        # Caso 2: demasiados pasajeros (más que la capacidad máxima del avión)
        case n if n > max_avion:
            aviones_necesarios = math.ceil(n / max_avion)
            return (f"{pasajeros} pasajeros → ¡Demasiados para un avión!"
                    f"Se necesitan {aviones_necesarios} aviones.")
        
        # Caso 3: suficiente cantidad para un solo avión
        case _:
            return f"{pasajeros} pasajeros → Vale la pena despegar con un avión"


# -------------------------------
# Ejemplos de uso
# -------------------------------
print("\n--- Usando match-case ---\n")
print(decidir_vuelo_match(10))     # pocos pasajeros
print(decidir_vuelo_match(100))    # un avión suficiente
print(decidir_vuelo_match(200))    # dos aviones
print(decidir_vuelo_match(375))    # tres aviones
