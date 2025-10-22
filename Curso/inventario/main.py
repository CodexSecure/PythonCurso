# lista de piezas en el inventario
inventario = [
    {"nombre": "Filtro de Aire", "tipo": "Filtro", "cantidad": 10, "precio": 15.75},
    {"nombre": "Aceite de Motor", "tipo": "Aceite", "cantidad": 5, "precio": 25.50},
    {"nombre": "Bujias", "tipo": "Encendido", "cantidad": 20, "precio": 8.99},
    {"nombre": "Filtro de Combustible", "tipo": "Filtro", "cantidad": 15, "precio": 18.50},
    {"nombre": "Aceite Transmisión", "tipo": "Aceite", "cantidad": 8, "precio": 30.00},
    {"nombre": "Correa de Distribución", "tipo": "Correa", "cantidad": 5, "precio": 45.75},
    {"nombre": "Bobina", "tipo": "Encendido", "cantidad": 12, "precio": 50.00},
    {"nombre": "Cables", "tipo": "Encendido", "cantidad": 25, "precio": 12.75}
]

# listar piezas en el inventario
def mostrar_inventario(inventario):
    print("\nLista de todas las piezas en el inventario:")
    for idx, p in enumerate(inventario, start=1):
        print(f"{idx}. {p['nombre']} (Tipo {p['tipo']}): {p['cantidad']} unidades a ${p['precio']} cada una")

# añadir nueva pieza al inventario
def anyadir(inventario,pieza):
    inventario.append(pieza)
    print(f"Pieza '{pieza['nombre']}' añadida al inventario.")

# comprobar si una pieza ya existe en el inventario
def existe(inventario,pieza):
    nombre_pieza = pieza["nombre"]
    for item in inventario:
        if item["nombre"].lower() == nombre_pieza.lower():
            return True
    return False
    """
    nuevo_nombre = "Filtro de Aire"
    if any(item["nombre"] == nuevo_nombre for item in inventario):
        return True
    else:
        return False
    """

# modificar una pieza existente
def modificar(inventario, nuevo_nombre, pieza_a_actualizar):
    # Obtener el índice de la pieza actual
    indice = obtener_indice_por_nombre(inventario, pieza_a_actualizar["nombre"])

    # Verificar si el nuevo nombre ya existe en otra pieza
    nombres_existentes = [pieza["nombre"].lower() for i, pieza in enumerate(inventario) if i != indice]

    # Si el usuario no quiere cambiar el nombre, mantener el actual
    if not nuevo_nombre:
        nuevo_nombre = pieza_a_actualizar["nombre"]

    if nuevo_nombre.lower() in nombres_existentes:
        print(f"⚠️ El nombre '{nuevo_nombre}' ya existe en otra pieza. No se puede actualizar.")
        input("Presiona Enter para continuar...")
        return  # 👈 importante: salir de la función
    else:
        # Pedir los nuevos datos
        nuevo_tipo = input(f"Ingrese el nuevo tipo (actual: {pieza_a_actualizar['tipo']}): ").strip() # strip() para eliminar espacios
        nueva_cantidad = input(f"Ingrese la nueva cantidad (actual: {pieza_a_actualizar['cantidad']}): ").strip()
        nuevo_precio = input(f"Ingrese el nuevo precio (actual: {pieza_a_actualizar['precio']}): ").strip()

        # Actualizar solo si el usuario introdujo algo
        pieza_a_actualizar["nombre"] = nuevo_nombre or pieza_a_actualizar["nombre"]
        pieza_a_actualizar["tipo"] = nuevo_tipo or pieza_a_actualizar["tipo"]

        # Validar y convertir cantidad y precio si se proporcionan
        if nueva_cantidad:
            try:
                pieza_a_actualizar["cantidad"] = int(nueva_cantidad)
            except ValueError:
                print("⚠️ Cantidad inválida. No se actualizó la cantidad.")

        if nuevo_precio:
            try:
                pieza_a_actualizar["precio"] = float(nuevo_precio)
            except ValueError:
                print("⚠️ Precio inválido. No se actualizó el precio.")

        print(f"✅ Pieza '{pieza_a_actualizar['nombre']}' actualizada correctamente.")

# obtener el índice de una pieza por su nombre
def obtener_indice_por_nombre(inventario, nombre):
    for i, pieza in enumerate(inventario):
        if pieza["nombre"].lower() == nombre.lower():
            return i
    return None  # no encontrado

# eliminar una pieza del inventario
def eliminar(inventario, nombre_pieza):
    # Buscar el índice de la pieza
    indice = obtener_indice_por_nombre(inventario, nombre_pieza)

    if indice is None:
        print(f"⚠️ La pieza '{nombre_pieza}' no existe en el inventario.")
        input("Presiona Enter para continuar...")
        return

    # Mostrar confirmación antes de eliminar
    confirmacion = input(f"¿Seguro que deseas eliminar '{nombre_pieza}'? (s/n): ").lower().strip()
    if confirmacion == "s":
        pieza_eliminada = inventario.pop(indice)
        print(f"✅ Pieza '{pieza_eliminada['nombre']}' eliminada correctamente.")
    else:
        print("❎ Operación cancelada.")

# buscar una pieza con filtro
def buscar(inventario, filtro):
    # Verifica si la opción de filtro ingresada es válida (solo "1" para nombre o "2" para tipo)
    if filtro not in ["1", "2"]:
        print("⚠️ Opción de filtro inválida.")
        return []  # Retorna una lista vacía si la opción no es válida

    # Si el usuario eligió buscar por nombre
    if filtro == "1":
        filtro = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
        # Crea una lista de piezas cuyo nombre contenga el texto ingresado (insensible a mayúsculas)
        resultados = [p for p in inventario if filtro.lower() in p["nombre"].lower()]

    # Si el usuario eligió buscar por tipo
    else:
        filtro = input("Ingrese el tipo o parte del tipo a buscar: ").strip()
        # Crea una lista de piezas cuyo tipo contenga el texto ingresado (insensible a mayúsculas)
        resultados = [p for p in inventario if filtro.lower() in p["tipo"].lower()]

    return resultados

#actualizar Cantidad de pieza existente
def actualizar_cantidad(inventario,nombre,cantidad):
    for pieza in inventario:
        if pieza["nombre"].lower() == nombre.lower():
            pieza["cantidad"] = cantidad
            print(f"Pieza '{pieza['nombre']}' actualizada con nueva cantidad.")
            return
    print(f"⚠️ La pieza '{nombre}' no existe en el inventario.")

# menú principal
def menu():
    while True:
        print("\n=== MENÚ INVENTARIO ===")
        print("1. Mostrar inventario")
        print("2. Agregar pieza")
        print("3. Modificar pieza")
        print("4. Eliminar pieza")
        print("5. Buscar pieza")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                mostrar_inventario(inventario)
                input("Presiona Enter para continuar...")

            case "2":
                nombre = input("\nIngrese el nombre de la pieza: ").strip()
                tipo = input("Ingrese el tipo de la pieza: ").strip()
                cantidad = int(input("Ingrese la cantidad disponible: "))
                precio = float(input("Ingrese el precio por unidad: "))

                if obtener_indice_por_nombre(inventario, nombre) is not None:
                    print(f"⚠️ La pieza '{nombre}' ya existe en el inventario. No se puede agregar duplicados.")

                    print("Desea actualizar su cantidad en su lugar?")
                    choice = input("Ingrese 's' para sí o cualquier otra tecla para cancelar: ")
                    if choice.lower() == 's':
                        actualizar_cantidad(inventario,nombre,cantidad)

                    input("Presiona Enter para continuar...")
                    continue  # Volver al inicio del bucle del menú

                nueva_pieza = {
                    "nombre": nombre,
                    "tipo": tipo,
                    "cantidad": cantidad,
                    "precio": precio
                }
                anyadir(inventario,nueva_pieza)

            case "3":
                mostrar_inventario(inventario)
                indice = int(input("Ingrese el número de la pieza a actualizar: ")) - 1
                if 0 <= indice < len(inventario):
                    pieza_a_actualizar = inventario[indice]
                    print(f"Actualizando pieza: {pieza_a_actualizar['nombre']}")

                    nuevo_nombre = input(f"Ingrese el nuevo nombre (actual: {pieza_a_actualizar['nombre']}): ")

                    modificar(inventario,nuevo_nombre,pieza_a_actualizar)
                else:
                    print("Índice inválido. Por favor, intente de nuevo.")

            case "4":
                mostrar_inventario(inventario)
                indice = int(input("Ingrese el número de la pieza a actualizar: ")) - 1
                if 0 <= indice < len(inventario):
                    nombre_pieza = inventario[indice]["nombre"]
                    eliminar(inventario,nombre_pieza)
                else:
                    print("Índice inválido. Por favor, intente de nuevo.")

            case "5":
                print("\n=== Búsqueda de piezas ===")
                print("1. Nombre")
                print("2. Tipo")
                filtro = input("Seleccione una opción: ").strip()
                resultados = buscar(inventario,filtro)
                if resultados:
                    print("\nResultados de la búsqueda:")
                    for p in resultados:
                        print(f"- {p['nombre']} (Tipo {p['tipo']}): {p['cantidad']} unidades a ${p['precio']} cada una")
                else:
                    print("No se encontraron piezas que coincidan con el filtro.")
                input("Presiona Enter para continuar...")

            case "6":
                print("Saliendo del programa...")
                break

            case _:
                print("⚠️ Opción inválida. Intente de nuevo.\n")

# Ejecutar menú
menu()