def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):        
        resultado *= i        
    return resultado

numero = 6
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

"""
import math

print("5! =", math.factorial(5))  # 120
"""