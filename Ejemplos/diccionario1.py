import os

if os.name == "nt":      # nt = Windows
    os.system("cls")
else:                    # posix = Linux, macOS, Unix
    os.system("clear")

# Diccionario
persona = {
    "nombre": "pepe",
    "edad": 25,
    "sexo": "H",
    "calificaciones":[7,8,9],
    "socials":{
        "twitter": "@pepe",
        "face": "pepito"
    }
}

# Aceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["face"])

# cambiar valores
persona["nombre"] = "Jose"
persona["calificaciones"][2] = 10

print("\n--- Nuevos Valores -----")
print(persona["nombre"])
print(persona["calificaciones"][2])

# Eliminar completamente una propiedad
del persona["edad"] # elimina la clave y valor

valor = persona.pop("sexo") # elimnina la clave pero devuelve el valor
print(persona)
print(valor)
print("edad" in persona) # False
print("socials" in persona) # True

# sobreescribir un diccionario con otro
a = {"name": "lolo", "edad": 88}
b = {"name": "ana", "pais": "cuba"}
a.update(b)
print(a)

# obtener todas las claves
print("\nClaves:")
print(persona.keys())

# obtener todos los valores
print("\nValores:")
print(persona.values())

# obtener tanto clave como valor
print("\nItems:")
print(persona.items()) # devuelve una tupla
for key, value in persona.items():
    print(f"{key}: {value}")