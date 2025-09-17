import math

# ==========================
# Calcular la hipotenusa de un triángulo rectángulo
# ==========================

# Opción #1: Usando el operador **
def hipotenusa_op():
    a = 7
    b = 9
    c = (a**2 + b**2) ** 0.5   # raíz cuadrada con **0.5
    print("Opción 1 → La hipotenusa es:", c)

# Opción #2: Usando math.sqrt()
def hipotenusa_sqrt():
    a = 3
    b = 4
    c = math.sqrt(a**2 + b**2)  # función sqrt() de math
    print("Opción 2 → La hipotenusa es:", c)

# Opción #3: Usando math.hypot() con valores ingresados por el usuario
def hipotenusa_hypot():
    a = float(input("Introduce el cateto a: "))
    b = float(input("Introduce el cateto b: "))
    c = math.hypot(a, b)  # función especial para hipotenusa
    print("Opción 3 → La hipotenusa es:", c)

# =========================
# Ejecución de ejemplos
# =========================

hipotenusa_op()     # Calcula con a=3, b=4 usando **
hipotenusa_sqrt()   # Calcula con a=3, b=4 usando sqrt()
hipotenusa_hypot()  # Pide al usuario los valores y usa hypot()
