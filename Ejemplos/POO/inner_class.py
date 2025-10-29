# ====================================================
# 🌟 CAR CON MÚLTIPLES INNER CLASSES
# ====================================================

class Car:
    """
    Clase Car con múltiples inner classes:
    - Engine: controla el motor
    - GPS: sistema de navegación
    """

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()  # Motor
        self.gps = self.GPS()        # GPS

    # -------------------------------
    # Inner Class: Engine
    # -------------------------------
    class Engine:
        """Motor del coche"""

        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    # -------------------------------
    # Inner Class: GPS
    # -------------------------------
    class GPS:
        """Sistema de navegación del coche"""

        def __init__(self):
            self.location = "Unknown"

        def set_location(self, location):
            self.location = location
            print(f"GPS location set to {self.location}")

        def get_location(self):
            print(f"Current GPS location: {self.location}")

    # -------------------------------
    # Método de Car
    # -------------------------------
    def drive(self):
        """Conducir solo si el motor está encendido"""
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model} from {self.gps.location}")
        else:
            print("Start the engine first!")


# ====================================================
# Uso de la clase con múltiples inner classes
# ====================================================

car = Car("Toyota", "Corolla")

# Intentar conducir con motor apagado
car.drive()  # Start the engine first!

# Encender motor
car.engine.start()

# Configurar GPS
car.gps.set_location("Madrid, Spain")

# Conducir con motor encendido y GPS configurado
car.drive()  # Driving the Toyota Corolla from Madrid, Spain

# Consultar ubicación actual
car.gps.get_location()

# Apagar motor
car.engine.stop()
car.drive()  # Start the engine first!

"""
=============================================
RESUMEN
=============================================

1️⃣ Inner Classes:
- Engine: controla el motor
- GPS: controla la ubicación del coche
- Ambas están definidas dentro de Car y son accesibles desde instancias de Car

2️⃣ Encapsulación:
- Los atributos internos (status, location) están protegidos por la convención de clase
- Se accede a ellos mediante métodos de cada inner class

3️⃣ Uso de drive():
- Verifica que el motor esté encendido
- Muestra ubicación usando GPS

4️⃣ Beneficios:
- Organiza funcionalidades relacionadas en inner classes
- Permite separar responsabilidades dentro de un mismo objeto
- Mantiene el código limpio y modular
"""
