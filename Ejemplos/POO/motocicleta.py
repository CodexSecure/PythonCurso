import os

if os.name == "nt":      # nt = Windows
    os.system("cls")
else:                    # posix = Linux, macOS, Unix
    os.system("clear")

class Motocicleta():
   estado = "nueva"
   motor = False

   def __init__(self, color, matricula, combustible_litros, capacidad_litros, numero_ruedas, marca , modelo, fecha_fabricacion, velocidad_punta, peso):
      self.color = color
      self.matricula = matricula
      self.combustible_litros = combustible_litros
      self.capacidad_litros = capacidad_litros
      self.numero_ruedas = numero_ruedas
      self.marca = marca
      self.modelo =modelo
      self.fecha_fabricacion = fecha_fabricacion
      self.velocidad_punta = velocidad_punta
      self.peso = peso

   def arrancar(self):
      if self.motor:
         print("Ruido en el coche, ya estaba arrancado")
      else:
         print("Se ha arrancado el motor.")

   def detener(self):
      if self.motor:
          print("Se detiene el coche, estaba arrancado")
      else:
         print("No se puede detener, ya estaba apagado")

   def __str__(self):
      return f"Motocicleta: {self.marca}, estado: {self.estado}"

   def consultar_precio(self):
      try:
         self.precio
         print(f"El precio de la moto {self.marca} {self.modelo} es {self.precio}")
      except:
         print(f"La moto {self.marca} {self.modelo} no tiene precio aun")

      """
      x = getattr(self, "precio", "No tiene precio aun")
      if isinstance(x, int):
         print(f"El precio de la moto {self.marca} {self.modelo} es {self.precio}")
      else:
         print(x)
      """
   def reporte_combustible(self):
      """Muestra la cantidad actual de combustible y cuánto falta por llenar."""
      print("\n----- Reporte de Combustible ------")
      por_llenar = self.capacidad_litros - self.combustible_litros

      print(f"La motocicleta {self.marca} tiene {self.combustible_litros} L, "
         f"su capacidad máxima es {self.capacidad_litros} L. "
         f"Le faltan {por_llenar} L para llenar el depósito.")

      if por_llenar <= 0:
         print("✅ El tanque está lleno.")
      else:
         print("⛽ Aún puedes repostar combustible.")


   def repostar_combustible(self):
      """Permite al usuario añadir combustible al depósito, si no está lleno."""
      por_llenar = self.capacidad_litros - self.combustible_litros

      print(f"\nRepostaje de combustible de la Motocicleta {self.marca}")

      if por_llenar <= 0:
         print(f"El depósito de {self.marca} ya está lleno. No se puede repostar más.")
         return

      print(f"Le quedan por llenar {por_llenar} L")
      repostar = input("¿Deseas repostar combustible? (s/n): ").lower()
      if repostar != "s":
         print("Repostaje cancelado.")
         return

      while True:
         try:
            cantidad_repostar = int(input("¿Cuántos litros desea repostar? "))
         except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

         if cantidad_repostar > por_llenar:
            print(f"No puedes repostar tanto combustible. Solo caben {por_llenar} L más.")
            continue
         else:
            self.combustible_litros += cantidad_repostar
            print(f"✅ Repostaje correcto. La motocicleta {self.modelo} {self.marca} "
            f"ahora tiene {self.combustible_litros} L.")
            break


moto1 = Motocicleta("rojo", 1234, 40 , 40, 4, "toyota", "corola", 555555, 100, 3500)
moto2 = Motocicleta(
   matricula = 1234,
   numero_ruedas = 4,
   peso = 3500,
   color="verde",
   combustible_litros = 5,
   marca = "BMW",
   modelo = "Super",
   fecha_fabricacion = "20/20/20",
   velocidad_punta = 100,
   capacidad_litros = 50
   )

print(moto1)
print(moto2)
moto1.arrancar()
moto1.detener()

moto1.precio = 2700
moto1.consultar_precio()
moto2.consultar_precio()

moto1.reporte_combustible()
moto2.reporte_combustible()

moto1.repostar_combustible()
moto2.repostar_combustible()

print(moto1.combustible_litros)
print(moto2.combustible_litros)