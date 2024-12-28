from math import *
class Ecuacion:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = 0
        self.x2 = 0

    def validacion(self):
        if ((self.b ** 2) - 4 * self.a * self.c) < 0:
            return "La solucion de la ecuacion es con numeros complejos"
        else:
            x1 = (-self.b + sqrt(self.b ** 2 - (4 * self.a * self.c))) / (2 * self.a)
            x2 = (-self.b - sqrt(self.b ** 2 - (4 * self.a * self.c))) / (2 * self.a)

            return x1,x2



    def reales_iguales(self, x1, x2):
        if x1 > 0 and x2 > 0:
            print("Las dos raices son reales ")
        elif x1 < 0 and x2 < 0:
            print("Ninguna de sus raices es real")
        elif x1 > 0 and x2 < 0:
            print(f"La raiz {x1} es real y la raiz {x2} no lo es")
        elif x1 < 0 and x2 > 0:
            print(f"La raiz {x1} no es posible y la raiz {x2} es real")

    def comparacion(self, x1, x2):
        if x1 == x2:
            print("Las dos raices son iguales")
        else:
            print("no son iguales")


ecuacion1 = Ecuacion(1, 4, 4)

s, q = ecuacion1.validacion()
print(s, q)

ecuacion1.reales_iguales(s, q)
ecuacion1.comparacion(s, q)