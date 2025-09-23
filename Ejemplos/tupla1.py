# 📝 Ejercicio: separar primer, últimos e intermedios de una lista de alumnos
alumnos = ["Ana", "Luis", "María", "Carlos", "Elena", "Pedro"]


# =====================================================
# MÉTODO 1: Usando índices y slicing
# =====================================================
primero = alumnos[0]        # primer elemento con índice 0
ultimo = alumnos[-1]        # último elemento con índice negativo -1
intermedios = alumnos[1:-1] # todos los elementos menos el primero y el último

print("🔹 Con índices y slicing:")
print("Primero:", primero)
print("Último:", ultimo)
print("Intermedios:", intermedios)


# =====================================================
# MÉTODO 2: Usando desempaquetado con *
# =====================================================
(primero, *intermedios, ultimo) = alumnos
# - primero = primer elemento
# - *intermedios = todos los del medio en forma de lista
# - ultimo = último elemento

print("\n🔹 Con desempaquetado *:")
print("Primero:", primero)
print("Último:", ultimo)
print("Intermedios:", intermedios)
