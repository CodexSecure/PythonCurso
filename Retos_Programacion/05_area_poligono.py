"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
 """
def calcular_area(poligono):
    match poligono["tipo"].lower():
        case "triangulo":
            return (poligono["base"] * poligono["altura"]) / 2
        case "cuadrado":
            return poligono["lado"] ** 2
        case "rectangulo":
            return poligono["base"] * poligono["altura"]
        case _:
            raise ValueError("Tipo de polígono no soportado")


# --- Programa principal ---
tipo = input("Introduce el tipo de polígono (triangulo, cuadrado, rectangulo): ").strip().lower()

if tipo == "triangulo":
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    poligono = {"tipo": tipo, "base": base, "altura": altura}

elif tipo == "cuadrado":
    lado = float(input("Introduce el lado del cuadrado: "))
    poligono = {"tipo": tipo, "lado": lado}

elif tipo == "rectangulo":
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    poligono = {"tipo": tipo, "base": base, "altura": altura}

else:
    print("Tipo de polígono no soportado.")
    exit()

# Cálculo e impresión del área
area = calcular_area(poligono)
print(f"El área del {tipo} es: {area}")

"""
Explicación rápida:

El usuario elige el tipo (triangulo, cuadrado o rectangulo).

Según la elección, se piden los valores necesarios.

Se construye un único diccionario (poligono) con los datos.

Se pasa ese diccionario a la única función calcular_area.

La función usa match para determinar la fórmula correcta y devuelve el resultado.

"""