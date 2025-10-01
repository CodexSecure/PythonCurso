# Diccionario con información de varias personas
personas = {
    "persona1": {
        "nombre": "Ana",
        "edad": 28,
        "ciudad": "Barcelona"
    },
    "persona2": {
        "nombre": "Luis",
        "edad": 35,
        "ciudad": "Madrid"
    },
    "persona3": {
        "nombre": "Marta",
        "edad": 22,
        "ciudad": "Valencia"
    }
}

# -------------------------------
# Acceder a datos en diccionarios anidados
# -------------------------------
print(personas["persona1"]["nombre"])  # Ana
print(personas["persona2"]["edad"])    # 35

# -------------------------------
# Modificar datos
# -------------------------------
personas["persona3"]["ciudad"] = "Sevilla"
print(personas["persona3"])

# -------------------------------
# Agregar una nueva persona
# -------------------------------
personas["persona4"] = {
    "nombre": "Carlos",
    "edad": 40,
    "ciudad": "Bilbao"
}

# -------------------------------
# Recorrer diccionario anidado
# -------------------------------
for key, info in personas.items():
    print(f"\n{key}:")
    for campo, valor in info.items():
        print(f"  {campo}: {valor}")

# -------------------------------
# Usar métodos en diccionarios anidados
# -------------------------------
# Obtener todas las edades
edades = [info.get("edad") for info in personas.values()]
print("\nEdades:", edades)

# Ver si alguien vive en Madrid
for info in personas.values():
    if info.get("ciudad") == "Madrid":
        print("Alguien vive en Madrid:", info["nombre"])
