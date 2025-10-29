# ==========================================
# Programa interactivo con clase Persona
# ==========================================

class Persona:
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
        return f"Persona: {self.color}, {self.edad} años, {self.sexo}, Ciudadano: {self.ciudadano}"

# Lista para almacenar personas
personas = []

# Función para crear una persona
def crear_persona():
    print("\nCreando nueva persona...")
    color = input("Color: ")
    altura = input("Altura en cm (dejar vacío para 180): ")
    edad = input("Edad (dejar vacío para 20): ")
    sexo = input("Sexo (M/F, dejar vacío para F): ")

    # Usar valores por defecto si no se ingresan
    persona = Persona(
        color=color if color else "blanco",
        altura_cm=int(altura) if altura else 180,
        edad=int(edad) if edad else 20,
        sexo=sexo.upper() if sexo else "F"
    )

    # Agregar atributos opcionales dinámicos
    while True:
        agregar = input("¿Agregar un atributo opcional? (s/n): ").lower()
        if agregar != "s":
            break
        nombre_attr = input("Nombre del atributo: ")
        valor_attr = input("Valor del atributo: ")
        setattr(persona, nombre_attr, valor_attr)  # Agrega el atributo dinámicamente

    personas.append(persona)
    print("Persona creada correctamente!")

# Función para mostrar atributos de una persona de manera segura
def mostrar_atributos():
    if not personas:
        print("No hay personas creadas.")
        return

    for i, p in enumerate(personas):
        print(f"\n[{i}] {p}")
        while True:
            ver_attr = input("¿Quieres ver un atributo opcional? (s/n): ").lower()
            if ver_attr != "s":
                break
            attr = input("Nombre del atributo: ")
            # Uso seguro de getattr
            valor = getattr(p, attr, "No tiene ese atributo")
            print(f"{attr}: {valor}")

# ==========================================
# Menú interactivo
# ==========================================
while True:
    print("\n--- MENÚ ---")
    print("1. Crear persona")
    print("2. Mostrar personas y atributos")
    print("3. Salir")

    opcion = input("Elige una opción: ")
    if opcion == "1":
        crear_persona()
    elif opcion == "2":
        mostrar_atributos()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
