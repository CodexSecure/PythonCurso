# 📝 Ejercicio: Reemplazar "banana" por "orange" en una lista de frutas  

# Lista original de frutas
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


# =========================================
# MÉTODO 1: Usando un bucle for clásico
# =========================================
# Paso 1: Creamos una lista vacía
# Paso 2: Recorremos la lista "fruits"
# Paso 3: Si el elemento NO es "banana", lo guardamos igual
# Paso 4: Si el elemento es "banana", lo reemplazamos por "orange"
# Paso 5: Mostramos la nueva lista
newlist1 = []  

for x in fruits:
    if x != "banana":       
        newlist1.append(x)
    else:                   
        newlist1.append("orange")

print("Con bucle for clásico:", newlist1)


# ========================================
# MÉTODO 2: Usando list comprehension
# ========================================
# La misma lógica que el bucle, pero resumida en una sola línea:
# - "x if x != 'banana' else 'orange'" -> expresión condicional
# - "for x in fruits" -> recorre la lista original
newlist2 = [x if x != "banana" else "orange" for x in fruits]

print("Con list comprehension:", newlist2)
