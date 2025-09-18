# Definimos una función que recibirá un número "n"
# y devolverá la distancia absoluta entre ese número y 50.
# La función abs() asegura que el resultado siempre sea positivo.
def myfunc(n):
    return abs(n - 50)


# Lista original
thislist = [100, 50, 65, 82, 23]


# Usamos sort() para ordenar la lista.
# El parámetro "key" indica una función que se usará como criterio de ordenación.
# En lugar de ordenar directamente por el valor del número,
# Python ordenará según el valor que devuelve myfunc(n),
# es decir, qué tan cerca está cada número del 50.
thislist.sort(key=myfunc)


# Imprimimos la lista resultante.
# Orden final: [50, 65, 23, 82, 100]
# Porque el orden está basado en la distancia a 50:
# 50 → 0 de distancia
# 65 → 15 de distancia
# 23 → 27 de distancia
# 82 → 32 de distancia
# 100 → 50 de distancia
print(thislist)
