# Lista original de frutas
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# ==========================
# MÉTODO 1: Usando un bucle for clásico
# ==========================
newlist1 = []  # lista vacía donde guardaremos las frutas filtradas

for x in fruits:                # recorremos cada fruta de la lista
    if "a" in x:                 # comprobamos si la fruta contiene la letra "a"
        newlist1.append(x)       # si la contiene, la añadimos a la nueva lista

print("Con bucle for clásico:", newlist1)


# ==========================
# MÉTODO 2: Usando list comprehension
# ==========================
# Esto hace lo mismo que el bucle anterior, pero en una sola línea
newlist2 = [x for x in fruits if "a" in x]

print("Con list comprehension:", newlist2)


# ==========================
# Función para filtrar palabras que contengan una letra específica (usando bucle clásico)
def filtrar_por_letra(lista, letra):
    """
    Devuelve una nueva lista con las palabras de 'lista' 
    que contienen la letra indicada.
    """
    
    # Opción 1: con bucle for clásico
    resultado = []
    for palabra in lista:
        if letra in palabra:   # verificamos si la letra está en la palabra
            resultado.append(palabra)
    
    # También podríamos hacerlo en una sola línea con list comprehension:
    # resultado = [palabra for palabra in lista if letra in palabra]
    
    return resultado


# Función para filtrar palabras que contengan una letra específica  (usando list comprehension)
def filtrar_por_letra_lc(lista, letra):
    """
    Devuelve una nueva lista con las palabras de 'lista' 
    que contienen la letra indicada.
    """
    # Aquí usamos list comprehension en lugar del bucle clásico
    return [palabra for palabra in lista if letra in palabra]


# ==========================
# Uso de la función
# ==========================

frutas = ["apple", "banana", "cherry", "kiwi", "mango"]

# Filtramos las frutas que contienen la letra "a"
resultado = filtrar_por_letra(frutas, "a")
print("Frutas con 'a':", resultado)

# Filtramos las frutas que contienen la letra "i"
resultado = filtrar_por_letra_lc(frutas, "e")
print("Frutas con 'i':", resultado)
