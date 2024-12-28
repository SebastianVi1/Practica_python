class animal:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print("EL animal esta hablando")

class perro(animal):
    def __init__(self,nombre,edad,raza):
        super().__init__(nombre,edad)
        self.raza = raza

    def hablar(self):
        print("El perro esta ladrando")

class gato(animal):
    def __init__(self,nombre,edad,color):
        super().__init__(nombre,edad)
        self.color = color

    def hablar(self):
        print("El gato esta maullando")

mi_perro = perro("Fido", 5, "poodle")
mi_gato = gato("garfiield", 3, "naranja")
print(mi_perro.nombre)
print(mi_perro.edad)
print(mi_perro.raza)
print(mi_gato.nombre)
print(mi_gato.edad)
print(mi_gato.color)
mi_perro.hablar()
mi_gato.hablar()