# Definimos la clase
class Taza:
    # Atributo de clase:
    #    Compartido por todos los objetos
    cantidad_de_tazas = 0
    _SORBO = 50 # constante

    # Método: es una funcion asociada a un objeto
    def beber(self):
        if self.cantidad >= Taza._SORBO:
            self.cantidad -= Taza._SORBO
            print(f"Has bebido de la taza {self.color}")
        else:
            print(f"NO QUEDA BASTANTE LíQUIDO en {self}")

    # En el método init inicializamos los
    #     atributos de instancia obligatorios
    def __init__(self, color, cantidad):
        Taza.cantidad_de_tazas += 1
        self.color = color
        self.cantidad = cantidad
        print(f"SE HA CREADO UNA taza {self.color}")

    def __str__(self):
        return f"TAZA {self.color} CANTIDAD {self.cantidad}ml"


# Instanciamos objetos de la clase Taza
tazas = [
    Taza("rojo", 300),
    Taza("azul", 250),
    Taza("verde", 500),
    Taza("verde", 100),
    Taza("verde", 200),
    Taza("verde", 300)
]

print()
print("############################################")
print()

for taza in [tazas[0]]:
    print(type(taza))
    print(taza)
    print("El color de la taza (a) es", taza.color)
    taza.beber()
    print(taza)
    print(taza.cantidad_de_tazas)
    print("---")
    print()

for i in range(6):
    tazas[0].beber()
    print(tazas[0])