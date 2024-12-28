class CSigno:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes

    def signo(self):
        if self.mes == 3 and self.dia >= 21 or self.mes == 4 and self.dia <= 20:
            print("Su signo es Aries")
        if self.mes == 4 and self.dia >= 20 or self.mes == 5 and self.dia <= 20:
            print("Su signo es Tauro")
        if self.mes == 5 and self.dia >= 21 or self.mes == 6 and self.dia <= 20:
            print("Su signo es Geminis")
        if self.mes == 6 and self.dia >= 21 or self.mes == 7 and self.dia <= 22:
            print("Su signo es Cancer")
        if self.mes == 7 and self.dia >= 23 or self.mes == 8 and self.dia <= 22:
            print("Su signp es Leo")
        if self.mes == 8 and self.dia >= 23 or self.mes == 9 and self.dia <= 22:
            print("Su signo es Virgo")
        if self.mes == 9 and self.dia >= 23 or self.mes == 10 and self.dia <= 22:
            print("Su signo es Libra")
        if self.mes == 10 and self.dia >= 23 or self.mes == 11 and self.dia <= 21:
            print("Su signo es Escorpio")
        if self.mes == 11 and self.dia >= 22 or self.mes == 12 and self.dia <= 21:
            print("Su signo es Sagitario")
        if self.mes == 12 and self.dia >= 22 or self.mes == 1 and self.dia <= 19:
            print("Su signo es Capricornio")
        if self.mes == 1 and self.dia >= 20 or self.mes == 2 and self.dia <= 18:
            print("Su signo es Acuario")
        if self.mes == 2 and self.dia >= 19 or self.mes == 3 and self.dia <= 20:
            print("Su signo es Piscis")

    def mostrar(self):
        print(f"El nombre de la persona es: {self.nombre}")
        print(f"Su dia de nacimiento es: {self.dia}")
        print(f"Su mes de nacimiento es: {self.mes}")
        persona1.signo()

nombre = input("Introduzca su nombre:")
dia = int(input("Introduzca su dia de nacimiento[1-31]:"))
mes = int(input("Introduzca su mes de nacimiento[1-12]:"))
persona1 = CSigno(nombre, dia, mes)
persona1.mostrar()


