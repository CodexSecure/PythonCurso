import os

if os.name == "nt":      # nt = Windows
    os.system("cls")
else:                    # posix = Linux, macOS, Unix
    os.system("clear")

class Persona:

    pais = "España" # atributo compartido por todas las instancias

    def __init__(self, color="blanco", altura_cm=180, edad=20, sexo="F", ciudadano=True):
        self.color = color
        self.altura_cm = altura_cm
        self.edad = edad
        self.sexo = sexo
        self.ciudadano = ciudadano

    def comer(self):
        print(f"{self.color} está comiendo")

    def salir(self):
        print(f"{self.color} está saliendo")

    def __str__(self):
        return f"Persona: {self.color}, {self.altura_cm} cm, {self.edad} años, {self.sexo}"

# Crear objetos
persona1 = Persona(edad=50, color="moreno")
persona2 = Persona("rojo",100,99,"H")
persona3 = Persona()

print(persona1)
print(persona2)
print(persona3.pais)



persona2.salir()

# Agregamos un nuevo atributo 'nombre' a la instancia persona1
persona1.nombre = "pepe"

# Intentamos imprimir el atributo 'nombre' de persona2
# Si persona2 no tiene ese atributo, se captura la excepción AttributeError
try:
    print(persona2.nombre)  # Esto puede fallar si persona2 no tiene 'nombre'
except AttributeError as e:
    # Se ejecuta si ocurre un AttributeError
    # e contiene el mensaje del error
    print(f"Error: {e}")

# Usamos getattr para obtener el atributo 'nombre' de persona1
# Si no existiera, devolvería el valor por defecto "No tiene nombre"
nombre = getattr(persona2, "nombre", "No tiene nombre")
print(nombre)  # Imprime el nombre de persona1: "pepe"

# Imprimimos directamente el atributo 'nombre' de persona1
# Como ya existe, no genera error
print(persona1.nombre)  # Imprime: "pepe"


