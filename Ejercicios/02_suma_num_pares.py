"""
Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""
import os

if os.name == "nt":      # nt = Windows
    os.system("cls")
else:                    # posix = Linux, macOS, Unix
    os.system("clear")

# Ejercicio 2: Sumar los números pares en una lista que representan huevos de dinosaurios carnívoros (T-Rex)
def count_eggs_par(egg_list) -> int:
    """funcion para calcular la suma de los huevos pares"""
    total = 0
    for eggs in egg_list:
        if eggs % 2 == 0:
            total += eggs
    return total

egg_list = [1,4,2,5,6,4,6,8,5,3,2,3,4]
print(count_eggs_par(egg_list))