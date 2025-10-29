"""
⚠️ Cuándo usar y cuándo no usar lambda

✅ Úsalo cuando:

La función sea muy corta (una sola línea).

La necesites solo una vez.

Quieras escribir código más compacto y legible.

❌ No lo uses cuando:

La función tenga varias líneas.

Sea compleja o se repita muchas veces → mejor usar def.
"""

# ==========================================
# 🔹 Ejemplos completos de funciones lambda
# ==========================================
# Autor: Fidel Oropesa (con explicación didáctica)
# ------------------------------------------

# 🧩 1️⃣ Función normal vs función lambda
# ------------------------------------------
# Ejemplo básico: multiplicar dos números

# ✅ Función normal
def multi(num1, num2):
    return num1 * num2

print(multi(3, 6))  # Salida: 18

# ✅ Función lambda equivalente
multiplicacion = lambda numero1, numero2: numero1 * numero2

# Podemos usarla directamente
resultado = multiplicacion(3, 6)
otro = multiplicacion(9, 2)

print(f"resultado es: {resultado} --- y otro es: {otro}")  # 18 y 18

# ✅ Lambda ejecutada en una sola línea
# (Se define y ejecuta inmediatamente)
(lambda numero1, numero2: print(numero1 * numero2))(5, 9)  # Imprime 45

# ------------------------------------------
# 🧠 2️⃣ Uso con una variable
# ------------------------------------------
# Calcular el cuadrado de un número
cuadrado = lambda x: x ** 2
print(f"El cuadrado de 5 es: {cuadrado(5)}")  # 25

# ------------------------------------------
# ⚙️ 3️⃣ Uso con varios parámetros
# ------------------------------------------
suma = lambda a, b: a + b
print(f"Suma de 3 + 7 = {suma(3, 7)}")  # 10

# ------------------------------------------
# 🗺️ 4️⃣ Uso con map() → aplica la función a cada elemento de una lista
# map()	Aplica una función a cada elemento de una lista
# lambda x: x**2	Función anónima que eleva cada número al cuadrado
# list()	Convierte el resultado en una lista visible
# ------------------------------------------
nums = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x ** 2, nums))
print(f"Cuadrados: {cuadrados}")  # [1, 4, 9, 16]
""" es el equivalente a este
nums = [1, 2, 3, 4]
cuadrados = []
for x in nums:
    cuadrados.append(x ** 2)
print(cuadrados)
"""

# ------------------------------------------
# 🔍 5️⃣ Uso con filter() → filtra según una condición
# ------------------------------------------
nums = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, nums))
print(f"Números pares: {pares}")  # [2, 4, 6]

# ------------------------------------------
# 🔢 6️⃣ Uso con sorted() → ordenar una lista de tuplas por el segundo valor
# ------------------------------------------
datos = [(1, 3), (2, 1), (5, 2)]
ordenado = sorted(datos, key=lambda x: x[1])
print(f"Ordenado por el segundo valor: {ordenado}")  # [(2, 1), (5, 2), (1, 3)]

# ------------------------------------------
# 🧮 7️⃣ Ejemplo práctico: ordenar nombres por su longitud
# ------------------------------------------
nombres = ["Ana", "Cristina", "Luis", "Bea"]
ordenados = sorted(nombres, key=lambda x: len(x))
print(f"Nombres ordenados por longitud: {ordenados}")
# ['Ana', 'Bea', 'Luis', 'Cristina']

# ------------------------------------------
# ✅ Cuándo usar lambda
# ------------------------------------------
# ✔ Cuando la función sea pequeña, de una línea.
# ✔ Cuando no necesites reutilizarla muchas veces.
# ✔ Cuando sea más legible dentro de otra función (map, filter, sorted).

# ❌ No usarla si:
# - La función tiene varias líneas.
# - Es compleja o se usará en muchas partes del código.

# ------------------------------------------
# 💬 Conclusión:
# ------------------------------------------
# Las funciones lambda son una herramienta útil
# para escribir código más compacto y expresivo.
# Son equivalentes a las funciones normales, pero anónimas y ligeras.
# ------------------------------------------
