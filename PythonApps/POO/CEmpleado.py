class CEmpleado:
    def __init__(self,rfc, nombre, edad, antiguedad):
        self.rfc = rfc
        self.nombre = nombre
        self.edad = edad
        self.antiguedad = antiguedad


    def mostrar(self):
        print(f"su rfc es: {self.rfc}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad : {self.edad}")
        print(f"Su antiguedad es de: {self.antiguedad}")

    def jubilacion(self):
        if self.edad >= 60 and self.antiguedad >=25:
            return print("Usted acredita a la jubilacion por edad") 
        elif self.edad < 60 and self.antiguedad >24:
            return print("Usted acredita a la jubilacion por antiguedad")
        elif self.edad <60 and self.antiguedad >25:
            return print("Usted no acredita a la jubilacion")
            
empleado1 = CEmpleado("a56gj8fsdy","sebastian",60,25)
empleado1.mostrar()
empleado1.jubilacion()
