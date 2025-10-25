# Argunmentos de longitud variable (*args)
def sumar_todos(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

print("=== Argumentos de longitud variable ===")
resultado = sumar_todos(1, 2, 3, 4, 5)
print(f"La suma es: {resultado}")

# Argumentos con nombre de longitud variable (**kwargs)
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print("\n=== Argumentos con nombre de longitud variable ===")
mostrar_info(nombre="Juan", edad=25, ciudad="Madrid")
mostrar_info(profesion="Ingeniero", empresa="TechCorp", pais="España", experiencia=5)
mostrar_info(nickname="coder123", nivel="avanzado", es_sub=True)

