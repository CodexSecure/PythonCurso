"""
Programa que solicita datos de varios coches al usuario.
Cada coche se guarda como un diccionario dentro de una lista.
Al final se muestran todos los coches introducidos.
"""

# Creamos una lista vacía para guardar los coches
coches = []

while True:
    print("\nIntroduce los datos del coche:")

    # Pedimos los datos al usuario
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = input("Año: ")

    # Creamos un diccionario para guardar los datos del coche
    coche = {
        "marca": marca,
        "modelo": modelo,
        "año": año
    }

    # Añadimos el coche a la lista de coches
    coches.append(coche)

    # Preguntamos si el usuario desea agregar otro coche
    continuar = input("¿Deseas añadir otro coche? (s/n): ").lower()
    if continuar != "s":
        break  # Si no escribe 's', salimos del bucle

# Mostramos los coches introducidos
print("\n--- LISTA DE COCHES ---")
for i, coche in enumerate(coches, start=1):
    print(f"Coche #{i}: Marca: {coche['marca']}, Modelo: {coche['modelo']}, Año: {coche['año']}")
