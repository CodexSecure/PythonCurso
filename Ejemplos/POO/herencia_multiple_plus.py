# ====================================================
# Mini RPG: Herencia múltiple + Inner Classes + Encapsulación
# Todo en un archivo
# ====================================================

# Clase base 1: Guerrero (ataque físico)
class Guerrero:
    def __init__(self, fuerza):
        self.fuerza = fuerza

    def ataque_fisico(self, objetivo):
        return f"💪 Ataca físicamente a {objetivo} con {self.fuerza} de fuerza"

# Clase base 2: Mago (magia)
class Mago:
    def __init__(self, mana):
        self.__mana = mana  # atributo privado

    # Getter y Setter para maná
    def get_mana(self):
        return self.__mana  # devuelve número

    def set_mana(self, nuevo_mana):
        self.__mana = max(nuevo_mana, 0)

    def lanzar_hechizo(self, hechizo, objetivo):
        if self.__mana <= 0:
            return f"❌ No hay maná suficiente para {hechizo}"
        self.__mana -= 10
        return f"✨ Lanza {hechizo} a {objetivo}. Mana restante: {self.__mana}"


# Clase hija: Paladin (hereda de Guerrero y Mago)
class Paladin(Guerrero, Mago):
    def __init__(self, nombre, fuerza, mana, salud):
        self.nombre = nombre
        self._salud = salud  # atributo protegido
        # Inicializamos clases base
        Guerrero.__init__(self, fuerza)
        Mago.__init__(self, mana)
        # Inner classes
        self.arma = self.Arma("Espada")
        self.armadura = self.Armadura("Placas")

    # Inner class Arma
    class Arma:
        def __init__(self, tipo):
            self.tipo = tipo
        def info(self):
            return f"🔹 Arma: {self.tipo}"

    # Inner class Armadura
    class Armadura:
        def __init__(self, tipo):
            self.tipo = tipo
        def info(self):
            return f"🛡 Armadura: {self.tipo}"

    # Ataque combinado
    def ataque_combinado(self, objetivo, hechizo=None):
        resultado = self.ataque_fisico(objetivo)
        if hechizo:
            resultado += "\n" + self.lanzar_hechizo(hechizo, objetivo)
        return resultado

    # Curación protegida
    def curar(self, cantidad):
        self._salud += cantidad
        return f"💖 {self.nombre} se cura {cantidad} puntos. Salud actual: {self._salud}"

    # Estado del Paladín
    def estado(self):
        return (f"{self.nombre} - Salud: {self._salud}, Mana: {self.get_mana()}, "
                f"Fuerza: {self.fuerza}, {self.arma.info()}, {self.armadura.info()}")


# ====================================================
# --- EJEMPLO DE USO ---
# ====================================================
if __name__ == "__main__":
    # Crear un Paladín
    paladin = Paladin("Sir Lancelot", fuerza=50, mana=30, salud=200)

    # Mostrar estado inicial
    print(paladin.estado())

    # Ataque físico
    print(paladin.ataque_fisico("Orco"))

    # Lanzar hechizo
    print(paladin.lanzar_hechizo("Fuego", "Troll"))

    # Ataque combinado
    print(paladin.ataque_combinado("Dragón", hechizo="Rayo"))

    # Curación
    print(paladin.curar(40))

    # Intentar gastar más maná del disponible
    print(paladin.lanzar_hechizo("Hielo", "Goblin"))

    # Estado final
    print(paladin.estado())

"""
Resumen de lo que hace este archivo:

1. Herencia múltiple:
   - Paladin hereda de Guerrero (ataque físico) y Mago (hechizos).
2. Encapsulación:
   - Maná (__mana) es privado, solo accesible mediante getter y setter.
   - Salud (_salud) es protegida, no se debe acceder directamente.
3. Inner Classes:
   - Arma y Armadura están dentro de Paladin para organizar objetos relacionados.
4. Ataques:
   - Puede atacar físicamente o lanzar hechizos.
   - Ataque combinado hace ambos.
5. Curación:
   - Puede curarse, modificando la salud protegida.
6. Manejo de maná:
   - No permite lanzar hechizos si maná <= 0.
"""
