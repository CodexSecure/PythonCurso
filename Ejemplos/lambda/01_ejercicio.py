# Crea con una funcion lambda una calculadora de areas de circulo.
# El area del circulo se calcula con la siguiente formula: pi*radio*radio (pi = 3.14159262359)

radio = int(input("Introduce el radio del circulo en cm: "))
pi = 3.14159262359

calculo_area = lambda radio : pi * radio * radio
area = round(calculo_area(radio),2)

print(f" El area del circulo es de {area} cm.")


# devuelve el index del color dado
colores = ["rojo", "azul", "verde", "amarillo"]
(lambda color : print(f"El Color se encuetra en la posicion {colores.index(color)} de la lista {colores}."))("verde")