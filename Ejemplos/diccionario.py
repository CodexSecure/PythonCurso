# Creamos un diccionario inicial
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Barcelona"
}

# -------------------------------
# 1️⃣ Acceder a un valor
# -------------------------------
print(persona["nombre"])          # -> Ana
print(persona.get("edad"))        # -> 28
print(persona.get("pais", "No especificado"))  # Si no existe, devuelve valor por defecto

# -------------------------------
# 2️⃣ Modificar valores
# -------------------------------
persona["edad"] = 29               # cambia edad a 29
print(persona)

# -------------------------------
# 3️⃣ Agregar nuevos pares
# -------------------------------
persona["profesion"] = "Ingeniera"
print(persona)

# -------------------------------
# 4️⃣ Eliminar elementos
# -------------------------------
persona.pop("ciudad")              # elimina la clave "ciudad"
print(persona)

persona.popitem()                  # elimina el último par agregado
print(persona)

# -------------------------------
# 5️⃣ Recorrer diccionarios
# -------------------------------
# Solo claves
for clave in persona.keys():
    print(clave)

# Solo valores
for valor in persona.values():
    print(valor)

# Clave y valor
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# -------------------------------
# 6️⃣ Copiar diccionarios
# -------------------------------
persona2 = persona.copy()
print("Copia:", persona2)

# -------------------------------
# 7️⃣ Limpiar diccionario
# -------------------------------
persona2.clear()
print("Limpiado:", persona2)  # -> {}

# -------------------------------
# 8️⃣ Actualizar diccionario
# -------------------------------
datos_nuevos = {"edad": 35, "pais": "España"}
persona.update(datos_nuevos)
persona.update({"nombre": "María"})  # Cambia nombre a María
print("Actualizado:", persona)

# -------------------------------
# 9️⃣ Comprobar existencia de claves
# -------------------------------
print("nombre" in persona)  # True
print("ciudad" in persona)  # False

