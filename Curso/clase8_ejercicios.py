"""
# Pedimos al usuario que introduzca una frase
frase = "Este es un  ejemplo de frase"

palabra = ""  # Variable para ir guardando cada palabra

for caracter in frase:  # Recorremos cada carácter de la frase
    if caracter != " ":
        # Si no es un espacio, lo agregamos a la palabra
        palabra += caracter
    else:
        # Si es un espacio, imprimimos la palabra y reiniciamos
        if palabra != "":
            print(palabra)
            palabra = ""

# Imprimir la última palabra si la hay
if palabra != "":
    print(palabra)

# Otra forma de hacerlo usando split()
print("\nUsando split():")
for palabra in frase.split():
    print(palabra) 
"""


"""
Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, 
y muestra sus elementos por pantalla.
"""

# Lista donde guardaremos las cadenas en el orden en que las introduce el usuario
lista = []

# Lista donde guardaremos las cadenas en orden inverso
nuevalista = []

# --- Lectura de datos ---
for x in range(5):  # Repetimos 5 veces para pedir 5 cadenas
    valores = input(f"Introduce la cadena de caracteres #{x + 1}: ")    
    lista.append(valores)  # Agregamos cada cadena a la lista original

# --- Inversión de las cadenas y creación de la nueva lista ---
for y in lista:
    if len(y) > 1:  
        # Si la cadena tiene más de un carácter, la invertimos
        # y[::-1] → uso de slicing: recorre la cadena al revés (paso -1)
        y = y[::-1]
    # Agregamos la cadena (invertida o no) a la nueva lista
    nuevalista.append(y)

# --- Invertimos el orden de los elementos en la nueva lista ---
# reversed() devuelve un iterador que recorre la lista al revés
# list() lo convierte en una lista normal
nuevalista = list(reversed(nuevalista))

# --- Mostramos los resultados ---
print("\nLista original:")
print(lista)

print("\nNueva lista (cadenas invertidas y en orden inverso):")
print(nuevalista)


