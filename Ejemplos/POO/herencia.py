# =====================================
# 🌟 HERENCIA EN PYTHON: PERSON, STUDENT, TEACHER
# =====================================

# Clase padre
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def full_name(self):
        """Devuelve el nombre completo."""
        return f"{self.firstname} {self.lastname}"

    def greet(self):
        """Saludo genérico, que será heredado."""
        print(f"👋 Hola, soy {self.full_name()}.")


# =====================================
# 👨‍🎓 Clase hija: Student
# =====================================
class Student(Person):
    def __init__(self, fname, lname, year, career):
        super().__init__(fname, lname)  # hereda el nombre
        self.graduationyear = year
        self.career = career

    def study(self):
        """Acción específica del estudiante."""
        print(f"📘 {self.firstname} está estudiando {self.career}.")

    def info(self):
        """Información del estudiante."""
        print(f"🎓 {self.full_name()} - Clase del {self.graduationyear} ({self.career})")


# =====================================
# 👩‍🏫 Clase hija: Teacher
# =====================================
class Teacher(Person):
    def __init__(self, fname, lname, subject, experience):
        super().__init__(fname, lname)
        self.subject = subject
        self.experience = experience  # años de experiencia

    def teach(self):
        """Acción específica del profesor."""
        print(f"🧮 {self.firstname} está dando clase de {self.subject}.")

    def info(self):
        """Información del profesor."""
        print(f"👩‍🏫 {self.full_name()} - {self.experience} años enseñando {self.subject}")


# =====================================
# 🧩 Uso de las clases
# =====================================

# Creamos una lista que mezcla distintos tipos de personas
people = [
    Student("Mike", "Olsen", 2024, "Ingeniería"),
    Student("Sara", "López", 2025, "Medicina"),
    Teacher("Anna", "Smith", "Matemáticas", 10),
    Teacher("Carlos", "Pérez", "Historia", 7)
]

# Recorremos la lista e identificamos qué tipo de objeto es
for person in people:
    person.greet()  # método heredado de la clase base
    person.info()   # método propio según la clase

    # Ejecutamos su acción particular
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

    print("-" * 50)
