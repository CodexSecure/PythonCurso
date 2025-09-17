# ==========================
# Ejemplos del constructor list() en Python
# ==========================

# 1. Crear una lista a partir de una tupla
thislist = list(("apple", "banana", "cherry"))  # doble paréntesis: uno del constructor y otro de la tupla
print("Lista desde tupla:", thislist)

# 2. Convertir una cadena en lista de caracteres
word = "Python"
letters = list(word)
print("Lista desde cadena:", letters)

# 3. Convertir un conjunto en lista
myset = {"a", "b", "c"}
mylist = list(myset)
print("Lista desde conjunto:", mylist)  # El orden puede variar porque los sets no tienen orden

# 4. Convertir un diccionario en lista (solo claves)
mydict = {"id": 1, "name": "Ana", "age": 25}
keys_list = list(mydict)
print("Lista desde diccionario (claves):", keys_list)

# 5. Crear una lista vacía
emptylist = list()
print("Lista vacía:", emptylist)
