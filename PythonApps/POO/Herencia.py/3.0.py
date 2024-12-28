class Auto:
    def __init__(self, placas, marca, modelo, color):
        self.placas = placas 
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar(self):
        print(f"Sus placas son {self.placas}")
        print(f"La marca de su auto es {self.marca}")
        print(f"El modelo de su carro es. {self.modelo}")
        print(f"El color de su auto es {self.color}")


class Estacionamiento(Auto):
    def __init__(self, horas, minutos, placas, marca, modelo, color):
        super().__init__(placas, marca, modelo, color)
        self.horas = horas
        self.minutos = minutos
        self.cobro_estacionamiento = 18

    def mostrar_datos(self):
        super().mostrar
        print(f"Estuvo durnte {self.horas} horas con {self.minutos} minutos")


    def calular_pago(self):
        pago = self.horas*self.cobro_estacionamiento
        if self.minutos >=30:
            pago = pago + 18
        
        return f"La cantidad a pagar es de {pago}"
    

class Pension:
    def __init__(self,noches, placas, marca, modelo, color):
        super().__init__(placas, marca, modelo, color)
        self.noches = noches

    def mostrar_datos(self):
        super().mostrar
        print(f"Estuvo un total de {self.noches}")

    def calcular_pago(self):
        pago = self.noches *100
        return f"El pago por hacer es de {pago}"
    


print("Que servicio desea adquirir:")
print("1. Auto")
print("2. Estacionamiento")
print("3. Pension")
a = int(input())
if a == 1:
    auto1 = Auto(input("Placas: "),input("Marca: "),input("Modelo: "),input("color: "))
    auto1.mostrar()

if a == 2:
    estacionamiento1 = Estacionamiento(int(input("Horas: ")),int(input("Minutos: ")),input("Placas: "),input("Marca: "),input("Modelo: "),input("color: "))
    estacionamiento1.mostrar_datos()
    print(estacionamiento1.calular_pago())

if a == 3:
    pension1 = Pension(int(input("Noches: ")),input("Placas: "),input("Marca:"),input("Modelo: "),input("color: "))
    pension1.mostrar_datos()
    print(pension1.calcular_pago())