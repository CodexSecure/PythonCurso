"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices.
Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

import os

if os.name == "nt":      # nt = Windows
    os.system("cls")
else:                    # posix = Linux, macOS, Unix
    os.system("clear")

import time

# =====================================================
# 🕒 Decorador para medir tiempo de ejecución
# =====================================================
def medir_tiempo(func):
    """Mide el tiempo que tarda en ejecutarse una función."""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱ {func.__name__} tardó: {fin - inicio:.6f} segundos")
        return resultado
    return wrapper


# =====================================================
# 🦖 Buscar dos números que sumen un objetivo
# =====================================================

nums = [1, 9, 4, 5, 6, 2] # lista grande para ver diferencias
goal = 8


# -----------------------------------------------------
# Versión básica
# -----------------------------------------------------
@medir_tiempo
def buscar_par_basico(nums, goal):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]


# -----------------------------------------------------
# Versión optimizada
# -----------------------------------------------------
@medir_tiempo
def buscar_par_optimizado(nums, goal):
    vistos = {}
    for i, num in enumerate(nums):
        complemento = goal - num
        if complemento in vistos:
            return [vistos[complemento], i]
        vistos[num] = i


# =====================================================
# 🔎 COMPARAR RESULTADOS
# =====================================================
print("Versión básica:", buscar_par_basico(nums, goal))
print("Versión optimizada:", buscar_par_optimizado(nums, goal))
