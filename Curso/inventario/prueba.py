class Pieza:
    def __init__(self, nombre, tipo, cantidad, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio

    def mostrar_info(self):
        """Muestra los datos de la pieza."""
        print(f"{self.nombre} ({self.tipo}) - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}")

    def actualizar_cantidad(self, nueva_cantidad):
        """Cambia la cantidad disponible."""
        self.cantidad = nueva_cantidad
        print(f"✅ Cantidad de '{self.nombre}' actualizada a {self.cantidad} unidades.")

    def cambiar_precio(self, nuevo_precio):
        """Cambia el precio unitario."""
        self.precio = nuevo_precio
        print(f"💲 Nuevo precio de '{self.nombre}': ${self.precio:.2f}")

class Inventario:
    def __init__(self):
        self.piezas = []  # lista de objetos Pieza

    def agregar_pieza(self, pieza):
        """Añade una pieza al inventario."""
        self.piezas.append(pieza)
        print(f"🧩 Pieza '{pieza.nombre}' añadida al inventario.")

    def mostrar_todas(self):
        """Muestra todas las piezas registradas."""
        print("\n=== INVENTARIO COMPLETO ===")
        for i, pieza in enumerate(self.piezas, start=1):
            print(f"{i}. ", end="")
            pieza.mostrar_info()
        print("============================\n")

    def buscar_por_nombre(self, texto):
        """Busca piezas cuyo nombre contenga cierto texto."""
        resultados = [p for p in self.piezas if texto.lower() in p.nombre.lower()]
        return resultados

    def buscar_por_tipo(self, tipo):
        """Busca piezas por tipo (por ejemplo: 'Filtro', 'Aceite', 'Encendido')."""
        resultados = [p for p in self.piezas if tipo.lower() in p.tipo.lower()]
        return resultados

    # Crear el inventario
mi_inventario = Inventario()

# Crear varios objetos Pieza
p1 = Pieza("Filtro de Aire", "Filtro", 10, 15.75)
p2 = Pieza("Aceite de Motor", "Aceite", 5, 25.50)
p3 = Pieza("Bujías", "Encendido", 20, 8.99)
p4 = Pieza("Bobina", "Encendido", 12, 50.00)
p5 = Pieza("Correa de Distribución", "Correa", 5, 45.75)

# Agregar los objetos al inventario
mi_inventario.agregar_pieza(p1)
mi_inventario.agregar_pieza(p2)
mi_inventario.agregar_pieza(p3)
mi_inventario.agregar_pieza(p4)
mi_inventario.agregar_pieza(p5)

# Mostrar todas las piezas
mi_inventario.mostrar_todas()

# Buscar piezas por nombre
print("🔎 Buscando por nombre 'Aceite':")
for pieza in mi_inventario.buscar_por_nombre("Aceite"):
    pieza.mostrar_info()

# Buscar piezas por tipo
print("\n🔎 Buscando por tipo 'Encendido':")
for pieza in mi_inventario.buscar_por_tipo("Encendido"):
    pieza.mostrar_info()

# Modificar datos de una pieza
p3.actualizar_cantidad(25)
p3.cambiar_precio(9.49)


