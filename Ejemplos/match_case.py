# ===============================
# Ejemplos de uso de match-case en Python
# ===============================

# Ejemplo 1: valores simples
color = "rojo"

match color:
    case "rojo":
        print("Ejemplo 1 → El color es rojo 🔴")
    case "verde":
        print("Ejemplo 1 → El color es verde 🟢")
    case _:
        print("Ejemplo 1 → Color desconocido ❓")

# -------------------------------------------------

# Ejemplo 2: con condiciones
edad = 20

match edad:
    case n if n < 18:
        print("Ejemplo 2 → Menor de edad 🚸")
    case n if 18 <= n < 65:
        print("Ejemplo 2 → Adulto 👩")
    case _:
        print("Ejemplo 2 → Jubilado 👴")

# -------------------------------------------------

# Ejemplo 3: con listas
fruta = ["manzana", "verde"]

match fruta:
    case ["manzana", color]:
        print(f"Ejemplo 3 → Es una manzana de color {color} 🍏")
    case ["banana", _]:
        print("Ejemplo 3 → Es una banana 🍌")
    case _:
        print("Ejemplo 3 → Fruta desconocida ❓")

# -------------------------------------------------

# Ejemplo 4: con diccionarios
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

match car:
    case {"brand": "Ford", "model": "Mustang"}:
        print("Ejemplo 4 → Es un Ford Mustang 🐎")
    case {"brand": "Ford", "model": model}:
        print(f"Ejemplo 4 → Es un Ford {model} 🚗")
    case _:
        print("Ejemplo 4 → Coche desconocido ❓")

# -------------------------------------------------

# Ejemplo 5: diccionarios anidados
persona = {
    "nombre": "Ana",
    "direccion": {"ciudad": "Madrid", "cp": 28001}
}

match persona:
    case {"direccion": {"ciudad": "Madrid"}}:
        print("Ejemplo 5 → La persona vive en Madrid 🏙️")
    case {"direccion": {"ciudad": ciudad}}:
        print(f"Ejemplo 5 → La persona vive en {ciudad}")
    case _:
        print("Ejemplo 5 → Ciudad desconocida ❓")

# -------------------------------------------------

# Ejemplo 6: múltiples opciones
dia = "sábado"

match dia:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print("Ejemplo 6 → Es un día laboral 💼")
    case "sábado" | "domingo":
        print("Ejemplo 6 → Es fin de semana 🎉")
    case _:
        print("Ejemplo 6 → Día inválido ❓")
