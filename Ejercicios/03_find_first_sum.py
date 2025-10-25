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

# ============================================
# 🦖 Buscar dos números que sumen un objetivo
# ============================================

nums = [4, 5, 6, 2]   # Lista de números
goal = 8              # Suma objetivo


# ------------------------------------------------------------
# 🧩 VERSIÓN 1: BÁSICA (con dos bucles)
# Complejidad: O(n²)
# ------------------------------------------------------------
def buscar_par_basico(nums, goal):
    """Busca el primer par de números cuya suma sea igual a goal."""
    for i in range(len(nums)):              # Primer índice
        for j in range(i + 1, len(nums)):   # Segundo índice
            if nums[i] + nums[j] == goal:   # Comprobamos si suman el objetivo
                return [i, j]               # Devolvemos los índices del par
    return None # No se encontro ninguna combinacion

# ------------------------------------------------------------
# ⚡ VERSIÓN 2: OPTIMIZADA (con diccionario)
# Complejidad: O(n)
# ------------------------------------------------------------
def buscar_par_optimizado(nums, goal):
    """Busca el primer par usando un diccionario para más eficiencia."""
    vistos = {}  # Guardará los números vistos con su índice

    for i, num in enumerate(nums):          # Recorremos con índice y valor
        complemento = goal - num            # Calculamos el número que falta

        if complemento in vistos:           # Si ya vimos ese complemento...
            return [vistos[complemento], i] # Devolvemos ambos índices

        vistos[num] = i                     # Guardamos el número actual


# ------------------------------------------------------------
# 🔎 COMPROBACIÓN DE RESULTADOS
# ------------------------------------------------------------

print("Versión básica:", buscar_par_basico(nums, goal))        # → [2, 3]
print("Versión optimizada:", buscar_par_optimizado(nums, goal))  # → [2, 3]
