# Creacion de una clase
class Personaje: # clase Padre
    # Metodo de Inicializacion
    def __init__(self, nombre, clase, nivel, salud, mana):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.salud = salud
        self.__mana = mana # atrubito privado __ (Encapsulado getter y setter)

    # Metodo para atacar a un objetivo
    def atacar (self, objetivo):
        return f"{self.nombre} ataca a {objetivo}!"

    # Metodo para curarse a si mismo
    def curar(self, cantidad):
        self.salud += cantidad
        return f"{self.nombre} se cura {cantidad} puntos de vida"

    # Metodo para obtener un atriburo privado (Encapsulado getter)
    def get_mana(self): # puede ser "obtener_xxxxx"
        return self.__mana

    # Metodo para cambiar un atributo privado (Encapsulado setter)
    def set_mana(self, nuevo_mana):
        self.__mana = nuevo_mana
        return f"Nuevo mana: {self.__mana}"

    def __str__(self):
        return f"Personaje {self.nombre}, de clase {self.clase} y nivel {self.nivel}, tiene una salud de {self.salud} y {self.__mana} de mana"

class Mago(Personaje): # Clase hijo (Hereda de Personaje)
    def __init__(self, nombre, nivel, salud, mana, poder_magico):
        super().__init__(nombre, "Mago", nivel, salud, mana)
        self.poder_magico = poder_magico

    def lanzar_hechizo(self, hechizo, objetivo):
        mana_actual = self.get_mana() # Usamos getter
        if mana_actual > 10:
            self.set_mana(mana_actual - 10)
            self.salud += 1
            return f"{self.nombre} <{self.clase}> lanza {hechizo} a {objetivo} con poder de {self.poder_magico}. Le quedan {self.get_mana()} de mana y gana 1 de salud"
        else:
            return f"{self.nombre} no tiene suficiente mana para lanzar el hechizo."

class Geurrero(Personaje):
    def __init__(self, nombre, nivel, salud, mana, fuerza):
        super().__init__(nombre, "Guerrero", nivel, salud, mana)
        self.fuerza = fuerza

    # Sobreescritura del metodo atacar
    def atacar(self, objetivo):
        return f"{self.nombre} <{self.clase}> ataca ferozmente a {objetivo} con fuerza de {self.fuerza} !"


# para uzar el polimorfismo
def realizar_ataque(personaje, objetivo):
    print(f"Te lanzare mi mejor golpe. {personaje.atacar(objetivo)}")

# Instanciacion de un objeto de la clase Personaje
heroe = Personaje("Fide", "Caballero", 20, 500, 300)
print(heroe)
print(heroe.atacar("pepe"))
print(heroe.curar(50))
print(heroe.get_mana())
print(heroe.set_mana(500))

# Instanciacion de un objeto de la clase Mago que hereda de Personaje
mago = Mago("Gandalf", 20, 80, 100, 150)
print(mago.atacar("Muerto"))
print(f"El mana actual es de {mago.get_mana()} y la salud es {mago.salud}")
print(mago.lanzar_hechizo("Fuego", "Orco"))
print(f"Despues de lanzar el hechizo el mana actual es de {mago.get_mana()} y la salud es {mago.salud}")

# Instanciacion de un objeto de la clase Mago que hereda de Personaje
guerrero = Geurrero("Leonidas", 15, 150, 30, 200)
print(guerrero.atacar("Hercules"))

# Ejemplo de Polimorfismo
realizar_ataque(mago, "Orco")
realizar_ataque(guerrero, "Orco")

for x in (heroe, mago, guerrero):
    print("\n For")
    print(x.nombre)
    realizar_ataque(x, "Humano")
    print(x.atacar("hhhhhhhhhh"))

"""
1. *¿Qué es la Programación Orientada a Objetos?*

    La Programación Orientada a Objetos (POO) es un enfoque que organiza el software alrededor de objetos que representan entidades del mundo real. Estos objetos combinan datos y comportamiento, facilitando la modularidad, la reutilización del código y el mantenimiento del software.
    Compararemos la POO con la programación estructurada, que organiza el código en funciones separadas de los datos.


2. *Clases y Objetos*

    Una clase es una plantilla que define las características y comportamientos de un conjunto de objetos similares. Un objeto es una instancia de esa clase, con valores específicos para sus propiedades.
    Por ejemplo, si la clase es "Persona", los objetos serían personas individuales, cada una con su propio nombre, edad y altura.
    Veremos cómo crear una clase en Python y cómo instanciar objetos a partir de esa clase.


3. *Método de Inicialización (`__init__`)*

    El método de inicialización (`__init__`) es una función especial en una clase que se ejecuta cuando se crea un nuevo objeto. Se utiliza para establecer los valores iniciales de los atributos del objeto.
    Exploraremos cómo definir este método y cómo asignar valores iniciales a los atributos de un objeto al momento de su creación.


4. *Atributos y Métodos de Clase*

    Los atributos de la clase son las propiedades que describen el estado de los objetos creados a partir de esa clase, como nombre, nivel, salud, etc.
    Los métodos de clase son funciones definidas dentro de una clase que describen las acciones que los objetos de esa clase pueden realizar, como atacar o curar.
    Aprenderemos a definir y usar tanto atributos como métodos dentro de una clase en Python.


5. *Encapsulamiento*

    El encapsulamiento es un principio fundamental de la POO que consiste en restringir el acceso directo a ciertos componentes de un objeto, protegiendo así los datos y asegurando que se manipulen de manera controlada.
    Diferenciaremos entre atributos públicos (accesibles desde cualquier parte del programa) y atributos privados (solo accesibles desde dentro de la clase).
    Introduciremos los métodos getter y setter, que permiten acceder y modificar atributos privados de manera controlada.


6. *Herencia y Polimorfismo*

    La herencia permite crear una nueva clase a partir de una clase existente. La nueva clase, llamada subclase, hereda atributos y métodos de la clase base, y puede añadir o modificar funcionalidades adicionales.
    Veremos cómo usar el `super()` para reutilizar y extender la funcionalidad de la clase base en una subclase.
    El polimorfismo permite que objetos de diferentes clases sean tratados como objetos de una clase común, permitiendo usar una interfaz común para diferentes tipos de objetos. Exploraremos cómo implementar y usar polimorfismo en Python.


7. *Herencia Múltiple*

    La herencia múltiple es una característica en la POO que permite a una clase heredar atributos y métodos de más de una clase base. Esto puede ser útil para combinar funcionalidades de diferentes clases en una sola clase derivada.
    Aprenderemos cómo implementar herencia múltiple en Python y discutir las ventajas y desafíos de este enfoque.


8. *Métodos Mágicos*

    Los métodos mágicos, también conocidos como métodos especiales o dunder methods, son funciones predefinidas en Python que permiten a las clases definir su comportamiento en operaciones específicas, como la creación de instancias, la representación en cadena, la aritmética, y más.

"""