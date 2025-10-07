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
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
"""

lista = []         # Guardará los números en el orden introducido
nuevalista = []    # Guardará los números en orden inverso

for x in range(5):
    lista.append(input(f"Introduce la cadena de caracteres # {x+1}: "))  
    # Con input() pedimos un número al usuario y lo añadimos a la lista con append()

# Creamos una nueva lista con los elementos de 'lista' pero en orden inverso
nuevalista = list(reversed(lista))  # reversed() devuelve un iterador, list() lo convierte en lista

print(lista)
print(nuevalista)

