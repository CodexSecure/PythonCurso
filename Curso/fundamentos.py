a = 3
b = -5
c = 0.2

print(type(a))
print(a)
print(type(b))
print(b+c)

import math

def calcular_hipotenusa():
    a = float(input("Introduce el cateto a: "))
    b = float(input("Introduce el cateto b: "))
    c = math.hypot(a, b)
    print(f"La hipotenusa es: {c}")

# Llamada a la función
calcular_hipotenusa()
