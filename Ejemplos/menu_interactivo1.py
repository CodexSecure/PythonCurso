import math  # Importamos el módulo math para usar funciones matemáticas

# ==========================
# Definición de funciones
# ==========================

def sumar(a, b):
    """Devuelve la suma de dos números"""
    return a + b

def restar(a, b):
    """Devuelve la resta de dos números"""
    return a - b

def multiplicar(a, b):
    """Devuelve el producto de dos números"""
    return a * b

def dividir(a, b):
    """Devuelve la división de dos números, manejando el caso de división por cero"""
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b

def hipotenusa(a, b):
    """Devuelve la hipotenusa de un triángulo rectángulo"""
    return math.hypot(a, b)

# ==========================
# Menú principal
# ==========================

def menu():
    """Muestra un menú para que el usuario elija una operación"""
    print("\n=== MENÚ DE OPERACIONES ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Calcular Hipotenusa")
    print("6. Salir")

# ==========================
# Programa principal
# ==========================

while True:
    menu()  # mostramos el menú en cada iteración
    opcion = input("Elige una opción (1-6): ")

    if opcion == "6":
        print("¡Hasta luego! 👋")
        break  # salimos del bucle

    # Si la opción es válida pedimos números
    if opcion in ["1", "2", "3", "4", "5"]:
        a = float(input("Introduce el primer número (o cateto a): "))
        b = float(input("Introduce el segundo número (o cateto b): "))

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", dividir(a, b))
        elif opcion == "5":
            print("La hipotenusa es:", hipotenusa(a, b))
    else:
        print("Opción no válida, intenta de nuevo.")
