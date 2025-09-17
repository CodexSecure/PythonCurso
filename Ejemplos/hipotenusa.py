import math

#Calcular la hipotenusa de un triángulo rectángulo
"""
Opcion #1: Usando el operador
a = 3
b = 4

c = (a**2 + b**2) ** 0.5   # raíz cuadrada
print("La hipotenusa es:", c)
"""

#opcion #2: Usando la función sqrt() del módulo math
"""
a = 3
b = 4

c = math.sqrt(a**2 + b**2)
print("La hipotenusa es:", c)
"""

def calcular_hipotenusa():
    a = float(input("Introduce el cateto a: "))
    b = float(input("Introduce el cateto b: "))
    c = math.hypot(a, b)
    print(f"La hipotenusa es: {c}")

# Llamada a la función
calcular_hipotenusa(