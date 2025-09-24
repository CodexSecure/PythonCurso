"""Ejemplo de bucle while con break"""

cuenta = 10
while True:
    cuenta -= 1
    if cuenta == 0:
        print("¡Despegue!")
        break
    print(cuenta)
print("¡BOOM!")


"""
print("START")
counter = 0
while counter != 7:
    counter += 1    
    print(f"Valor de Counter es {counter}")
print("END")
"""

"""
i = 10
while i > 0:
    print(i)
    i -= 1
print("¡Despegue!")
print("¡BOOM!")
"""
