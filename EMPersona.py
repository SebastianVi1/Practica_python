class persona():
    def __init__(self,nombre, edad, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre = nombre

    def getEdad(self):
        if edad >= 0 and edad <= 100:
            print("Valido")
        else:
            print("Invalido")
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getGenero(self):
        if genero.lower == 'M' or 'Masculino':
            print("El genero es valido")
        elif genero.lower == 'F' or 'Femenino':
            print("El genero es valido")
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
genero = str(input("Ingrese su genero: "))
persona1 = persona(nombre,edad,genero)
print(persona1.getNombre())
print(persona1.getEdad())
print(persona1.getGenero())
