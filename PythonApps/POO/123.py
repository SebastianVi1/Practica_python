class Estudiante:
    def __init__(self,no_control, nombre, carrera, promedio):
        self.no_control = no_control
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio


    def datos(self):
        print(f"su numero de control es: {self.no_control}")
        print(f"su nombre es: {self.nombre}")
        print(f"su carrera es: {self.carrera}")
        if self.promedio <= 70:
            print("reprobado")
        elif self.promedio >=70 and self.promedio <80:
            print("pasable")
        elif self.promedio >= 80 and self.promedio <90:
            print("Muy bien")
        elif self.promedio >90 and self.promedio <101:
            print("excelente")

estudiante1 = Estudiante(22010131,"sebastian","sistemas computacionales",7.9)
print(estudiante1.datos())