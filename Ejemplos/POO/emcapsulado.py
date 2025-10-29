# ====================================================
# 🌟 ENCPSULACIÓN AVANZADA EN PYTHON
# ====================================================

class BankAccount:
    """
    Clase que representa una cuenta bancaria.
    Demuestra encapsulación con atributos privados, protegidos y propiedades.
    """

    def __init__(self, owner, balance):
        self._owner = owner          # Atributo protegido (convención: solo para clase y subclases)
        self.__balance = balance     # Atributo privado

    # -------------------------------
    # Propiedad para acceder al owner
    # -------------------------------
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if isinstance(new_owner, str) and new_owner.strip():
            self._owner = new_owner
        else:
            print("Nombre inválido para el propietario.")

    # -------------------------------
    # Propiedad para obtener balance
    # -------------------------------
    @property
    def balance(self):
        """Getter: devuelve el saldo actual"""
        return self.__balance

    # -------------------------------
    # Métodos públicos
    # -------------------------------
    def deposit(self, amount):
        """Deposita dinero en la cuenta si el valor es positivo"""
        if amount > 0:
            self.__balance += amount
            self.__log_transaction(f"Depósito: {amount}€")
        else:
            print("Cantidad inválida para depositar.")

    def withdraw(self, amount):
        """Retira dinero si hay suficiente saldo"""
        if amount <= 0:
            print("Cantidad inválida para retirar.")
        elif amount > self.__balance:
            print(f"Fondos insuficientes. Saldo actual: {self.__balance}€")
        else:
            self.__balance -= amount
            self.__log_transaction(f"Retiro: {amount}€")

    # -------------------------------
    # Método privado
    # -------------------------------
    def __log_transaction(self, message):
        """Método privado para registrar transacciones (solo dentro de la clase)"""
        print(f"[{self._owner}] {message}. Saldo actual: {self.__balance}€")


# ====================================================
# USO DE LA CLASE
# ====================================================

# Crear cuenta
cuenta1 = BankAccount("Alice", 1000)

# Acceso a atributos protegidos y privados
print(cuenta1.owner)     # Acceso a propiedad protegida mediante getter
print(cuenta1.balance)   # Acceso al saldo mediante property

# Operaciones seguras
cuenta1.deposit(500)    # Depósito válido
cuenta1.withdraw(200)   # Retiro válido
cuenta1.withdraw(2000)  # Retiro inválido, fondos insuficientes

# Cambiar nombre del propietario usando setter
cuenta1.owner = "Alice Cooper"
print(f"Nuevo propietario: {cuenta1.owner}")

# Intento de acceso directo a saldo privado (no recomendado)
# print(cuenta1.__balance)  # Esto daría error

# Saldo final
print(f"Saldo final: {cuenta1.balance}€")


"""
=============================================
RESUMEN AVANZADO DE ENCPSULACIÓN
=============================================

1️⃣ Atributos privados y protegidos
- __balance → privado, solo accesible dentro de la clase
- _owner → protegido, convención de acceso restringido a la clase y subclases

2️⃣ Propiedades (@property)
- Permiten acceder y modificar atributos de forma controlada
- Ejemplo: balance es solo lectura, owner tiene getter y setter con validación

3️⃣ Métodos privados
- __log_transaction → solo puede llamarse dentro de la clase
- Permite encapsular la lógica interna (registro de transacciones)

4️⃣ Beneficios
- Control total sobre cómo se acceden o modifican los datos internos
- Posibilidad de validar entradas antes de cambiar atributos
- Mejora la seguridad y mantenibilidad del código

5️⃣ Ejemplo práctico
- BankAccount protege el saldo (__balance) y el propietario (_owner)
- Todas las operaciones sobre saldo usan métodos seguros y registran transacciones
"""
