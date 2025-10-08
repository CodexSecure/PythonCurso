# EJERCICIO
"""
El programa solicitará datos al usuario uno detrá de otro
crearemos una lista de coches iguales
al final mostramos la lista
"""

def introducir_vehiculo(id: int):
    vehiculo = {'id': id}

    for dato in  ["marca", "precio", "potencia", "color"]:
        vehiculo[dato] = input(f"{dato}:")

    return vehiculo

def validar_vehiculo(vehiculo):
    for llave in vehiculo:
        if vehiculo[llave] == '':
            return False

    return True

def introducir_vehiculos():
    vehiculos = []
    while True:
        print()
        v = introducir_vehiculo(len(vehiculos))
        if validar_vehiculo(v):
            vehiculos.append(v)
        else:
            break

    return vehiculos

def mostrar(vehiculo):
    print(f"==[{vehiculo["id"]}]")
    for llave in vehiculo:
        if llave != "id":
            print(f"{llave}: {vehiculo[llave]}")
    print("-" * 5)

for vehiculo in introducir_vehiculos():
    mostrar(vehiculo)
