class Coche:
    cantidad_de_coches = 0  # Atributo de clase (común a todos los objetos)

    def __init__(self, marca, modelo):
        Coche.cantidad_de_coches += 1  # Aumenta el contador al crear un coche
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"🚗 El {self.marca} {self.modelo} ha arrancado.")

    def frenar(self):
        print(f"🛑 El {self.marca} {self.modelo} se ha detenido.")


print("\n=== 🚘 Creando coches ===")

# Lista para guardar todos los coches creados
coches = [
    Coche("Toyota", "Corolla"),
    Coche("Ford", "Focus"),
    Coche("Honda", "Civic"),
    Coche("Mazda", "3")
]

# 🔁 Recorremos la lista de coches e imprimimos sus datos
print("\n=== 🚗 Lista de coches creados ===")
for coche in coches:
    print(f"- {coche.marca} {coche.modelo}")

# También puedes mostrar cuántos hay
print(f"\nTotal de coches creados: {Coche.cantidad_de_coches}")

# 🔁 Recorremos todos los coches y llamamos al método arrancar()
print("\n=== Arrancando todos los coches ===")
for coche in [coches[0]]:
    coche.arrancar()

#mi_coche.arrancar()
#tu_coche.frenar()

