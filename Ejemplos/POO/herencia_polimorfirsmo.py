# ====================================================
# 🌟 HERENCIA Y POLIMORFISMO EN PYTHON - VEHÍCULOS
# ====================================================

# --------------------------------------------
# Clase base: Vehicle
# --------------------------------------------
class Vehicle:
    # Atributo de clase: se comparte entre todos los objetos de Vehicle
    total_vehicles = 0

    def __init__(self, brand, model):
        """
        Constructor de Vehicle: se ejecuta al crear un objeto.
        Inicializa los atributos de instancia: marca y modelo.
        También incrementa el contador total de vehículos.
        """
        self.brand = brand
        self.model = model
        Vehicle.total_vehicles += 1  # Incrementamos el contador global de vehículos

    def move(self):
        """
        Método genérico de movimiento.
        Puede ser sobrescrito (overridden) en las clases hijas.
        """
        print("Move!")  # Mensaje genérico para cualquier vehículo

    @classmethod
    def show_total(cls):
        """Método de clase para mostrar el total de vehículos creados"""
        print(f"Total de vehículos creados: {cls.total_vehicles}")


# --------------------------------------------
# Clase hija: Car
# --------------------------------------------
class Car(Vehicle):
    # Contador específico de coches
    total_cars = 0

    def __init__(self, brand, model, doors):
        """
        Constructor de Car: llama al constructor de Vehicle para inicializar
        brand y model, y añade un atributo propio: doors (número de puertas).
        """
        super().__init__(brand, model)  # Llama al __init__ de Vehicle
        self.doors = doors
        Car.total_cars += 1  # Incrementa el contador de coches

    def move(self):
        """Sobrescribe el método move() de Vehicle"""
        print("Drive on road!")

    def honk(self):
        """Método propio de Car"""
        print(f"{self.brand} {self.model} hace: ¡BEEP BEEP!")

    @classmethod
    def show_total_cars(cls):
        """Mostrar total de coches"""
        print(f"Total de coches: {cls.total_cars}")


# --------------------------------------------
# Clase hija: Boat
# --------------------------------------------
class Boat(Vehicle):
    total_boats = 0

    def __init__(self, brand, model, length):
        """Constructor de Boat: añade atributo length (largo del barco)"""
        super().__init__(brand, model)
        self.length = length
        Boat.total_boats += 1

    def move(self):
        """Sobrescribe move() para barcos"""
        print("Sail on water!")

    def anchor(self):
        """Método propio de Boat"""
        print(f"{self.brand} {self.model} está anclando.")

    @classmethod
    def show_total_boats(cls):
        print(f"Total de barcos: {cls.total_boats}")


# --------------------------------------------
# Clase hija: Plane
# --------------------------------------------
class Plane(Vehicle):
    total_planes = 0

    def __init__(self, brand, model, capacity):
        """Constructor de Plane: añade atributo capacity (capacidad de pasajeros)"""
        super().__init__(brand, model)
        self.capacity = capacity
        Plane.total_planes += 1

    def move(self):
        """Sobrescribe move() para aviones"""
        print("Fly in the sky!")

    def land(self):
        """Método propio de Plane"""
        print(f"{self.brand} {self.model} está aterrizando.")

    @classmethod
    def show_total_planes(cls):
        print(f"Total de aviones: {cls.total_planes}")


# --------------------------------------------
# Crear objetos de cada tipo
# --------------------------------------------
vehicles = [
    Car("Ford", "Mustang", 2),
    Car("Tesla", "Model S", 4),
    Boat("Ibiza", "Touring 20", 20),
    Plane("Boeing", "747", 416),
    Plane("Airbus", "A320", 180)
]

# --------------------------------------------
# Recorrer lista de vehículos
# --------------------------------------------
for v in vehicles:
    print(f"Marca: {v.brand}, Modelo: {v.model}")

    # Polimorfismo: cada clase tiene su propia implementación de move()
    v.move()

    # Llamar a métodos específicos según el tipo de objeto
    if isinstance(v, Car):
        v.honk()  # Solo los coches pueden hacer "honk"
        print(f"Puertas: {v.doors}")
    elif isinstance(v, Boat):
        v.anchor()  # Solo los barcos pueden anclar
        print(f"Largo: {v.length} pies")
    elif isinstance(v, Plane):
        v.land()  # Solo los aviones pueden aterrizar
        print(f"Capacidad: {v.capacity} pasajeros")

    print("-" * 40)

# --------------------------------------------
# Mostrar contadores
# --------------------------------------------
Vehicle.show_total()
Car.show_total_cars()
Boat.show_total_boats()
Plane.show_total_planes()


"""
=============================================
RESUMEN EXPLICADO DEL CÓDIGO
=============================================

1️⃣ Herencia
- Las clases hijas (Car, Boat, Plane) heredan de Vehicle.
- Por eso todas tienen los atributos brand y model, y el método move() que puede sobrescribirse.

2️⃣ Polimorfismo
- El método move() se comporta distinto según la clase del objeto.
    - Car.move() → "Drive on road!"
    - Boat.move() → "Sail on water!"
    - Plane.move() → "Fly in the sky!"

3️⃣ Atributos propios de cada clase hija
- Car → doors (número de puertas)
- Boat → length (largo del barco)
- Plane → capacity (capacidad de pasajeros)

4️⃣ Métodos propios
- Car.honk() → sonido del coche
- Boat.anchor() → anclar barco
- Plane.land() → aterrizar avión

5️⃣ Contadores de objetos
- Vehicle.total_vehicles → total de vehículos creados
- Car.total_cars → total de coches
- Boat.total_boats → total de barcos
- Plane.total_planes → total de aviones

6️⃣ Uso de isinstance()
- Permite ejecutar métodos que solo existen en ciertos tipos de objetos dentro del bucle.

7️⃣ Lista de objetos
- vehicles = [Car(...), Boat(...), Plane(...)]
- Recorremos la lista y cada objeto responde a sus métodos propios y heredados correctamente.

📌 Con esto tienes un ejemplo completo de:
- Herencia
- Polimorfismo
- Métodos propios y heredados
- Contadores de objetos
- Uso de isinstance() y listas de objetos
"""
