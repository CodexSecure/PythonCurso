# ================================================================
# 🧠 CURSO PRÁCTICO: CLASES Y OBJETOS EN PYTHON
# ================================================================

# ---------------------------------------------------------------
# 1️⃣ Concepto básico: Clase y objeto
# ---------------------------------------------------------------
class Coche:
    # Constructor (se ejecuta al crear un objeto)
    def __init__(self, marca, modelo):
        self.marca = marca     # atributo de instancia
        self.modelo = modelo

    # Métodos (comportamientos)
    def arrancar(self):
        print(f"🚗 El {self.marca} {self.modelo} ha arrancado.")

    def frenar(self):
        print(f"🛑 El {self.marca} {self.modelo} se ha detenido.")


print("\n=== 1️⃣ Ejemplo básico de clase ===")
mi_coche = Coche("Toyota", "Corolla")
tu_coche = Coche("Ford", "Focus")

mi_coche.arrancar()
tu_coche.frenar()


# ---------------------------------------------------------------
# 2️⃣ Atributos de clase (comunes a todos los objetos)
# ---------------------------------------------------------------
class CocheConRuedas:
    ruedas = 4  # atributo compartido por todas las instancias

    def __init__(self, marca):
        self.marca = marca

print("\n=== 2️⃣ Atributos de clase ===")
c1 = CocheConRuedas("Mazda")
c2 = CocheConRuedas("Seat")
print(f"{c1.marca} tiene {c1.ruedas} ruedas.")
print(f"{c2.marca} tiene {c2.ruedas} ruedas.")


# ---------------------------------------------------------------
# 3️⃣ Métodos especiales (__init__, __str__)
# ---------------------------------------------------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

print("\n=== 3️⃣ Método __str__ ===")
p = Persona("Ana", 30)
print(p)  # muestra una versión legible del objeto


# ---------------------------------------------------------------
# 4️⃣ Herencia (una clase puede heredar de otra)
# ---------------------------------------------------------------
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido genérico.")

class Perro(Animal):  # Perro hereda de Animal
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

print("\n=== 4️⃣ Herencia ===")
perro = Perro("Firulais")
gato = Gato("Michi")
perro.hablar()
gato.hablar()


# ---------------------------------------------------------------
# 5️⃣ Encapsulación (controlar acceso a atributos)
# ---------------------------------------------------------------
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo   # atributo privado (por convención)

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("❌ Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"💰 Saldo actual de {self.titular}: {self.__saldo} €")

print("\n=== 5️⃣ Encapsulación ===")
cuenta = CuentaBancaria("Fidel", 100)
cuenta.depositar(50)
cuenta.retirar(120)
cuenta.mostrar_saldo()


# ---------------------------------------------------------------
# 6️⃣ Polimorfismo (mismo método, distinto comportamiento)
# ---------------------------------------------------------------
class Ave:
    def hablar(self):
        print("Pío pío")

class Loro(Ave):
    def hablar(self):
        print("¡Hola, soy un loro!")

class Pato(Ave):
    def hablar(self):
        print("Cuac cuac")

print("\n=== 6️⃣ Polimorfismo ===")
aves = [Loro(), Pato(), Ave()]
for ave in aves:
    ave.hablar()  # mismo método, distinto resultado


# ---------------------------------------------------------------
# 7️⃣ Ejemplo práctico: Gestor simple de cuentas bancarias
# ---------------------------------------------------------------
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_cuentas(self):
        print(f"\n🏦 Banco {self.nombre}:")
        for cuenta in self.cuentas:
            cuenta.mostrar_saldo()


print("\n=== 7️⃣ Programa completo con clases ===")
banco = Banco("PythonBank")

c1 = CuentaBancaria("Ana", 200)
c2 = CuentaBancaria("Luis", 500)

c1.depositar(100)
c2.retirar(150)

banco.agregar_cuenta(c1)
banco.agregar_cuenta(c2)
banco.mostrar_cuentas()


# ================================================================
print("\n✅ Fin del archivo de aprendizaje de Clases y Objetos en Python")
# ================================================================
