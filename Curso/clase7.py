"""
def sum(a,b):
    return int (a + b)

a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))
print(sum(a,b))

def cuadrado(a):
    if a < 0:
        return None
    else:
        # return a * a
        # return pow(a,2)
        return a ** 2
    
a = float(input("Introduce el numero: "))
print(cuadrado(a))
"""
def hola(texto):
    return "Hola " + texto

nombre = input("Introduce tu nombre: ")
print(hola(nombre))


# ================================================
# Función que calcula el total de una factura con IVA
# ================================================
def calcular_factura(cantidad_sin_iva, iva = 21):    
    total = cantidad_sin_iva * (1 + iva / 100)
    return total

# Caso 1: usando el IVA por defecto (21%)
print("Factura con IVA 21%:", calcular_factura(100))   # 121.0

# Caso 2: usando un IVA distinto (10%)
print("Factura con IVA 10%:", calcular_factura(100, 10))  # 110.0