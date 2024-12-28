class persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mensaje(self):
        print(f'hola soy {self.nombre}')

class estudiante(persona):
    def __init__(self,nombre,edad,matricula,horario):
        persona.__init__(self,nombre,edad)
        self.matricula = matricula
        self.horario = horario

    def estudiar(self):
        print(f'{self.nombre} está estudiando')

class Trabajador(persona):
    def __init__(self,nombre,edad,sueldo,empresa):
        persona.__init__(self,nombre,edad)
        self.sueldo = sueldo
        self.empresa = empresa

    def trabajar(self):
        print(f'{self.nombre} está trabajando')

class EstudianteTrabajador(estudiante,Trabajador):
    def __init__(self,nombre,edad,matricula,sueldo,empresa,horario):
        estudiante.__init__(self,nombre,edad,matricula,horario)
        Trabajador.__init__(self,nombre,edad,sueldo,empresa)

    def esforzarse(self):
        print(f'{self.nombre} está esforzandose para estudiar')

mi_estudiante_trabajador = EstudianteTrabajador("Andre",18,22010130,300000,"Tecnologico","Matricula")


print("Nombre:",mi_estudiante_trabajador.nombre)
print(mi_estudiante_trabajador.edad)
print(mi_estudiante_trabajador.matricula)
print(mi_estudiante_trabajador.sueldo)
print(mi_estudiante_trabajador.empresa)
print(mi_estudiante_trabajador.horario)