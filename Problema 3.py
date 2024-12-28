class auto():
    def __init__(self,placas,marca,modelo,color):
        self.placas = placas
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar(self):
        print(f'{self.placas}\n{self.marca}\n{self.modelo}\n{self.color}')

class estacionamiento(auto):
    def __init__(self,placas,marca,modelo,color,hora,minutos):
        super().__init__(placas,marca,modelo,color)
        self.hora = hora
        self.minutos = minutos

    def mostrar_datos(self):
        print(f'{self.placas}\n{self.marca}\n{self.modelo}\n{self.color}\n{self.hora}\n{self.minutos}')

    def calcular_pago(self):
        p = self.hora * 18
        if self.minutos >= 30 and self.minutos <= 60:
            self.minutos = (self.hora/self.hora)
        print("Total a pagar:",p+(self.minutos*18))

class pension(auto):
    def __init__(self,placas,marca,modelo,color,noches):
        super().__init__(placas,marca,modelo,color)
        self.noches = noches

    def mostrar_datos(self):
        print(f'{self.placas}\n{self.marca}\n{self.modelo}\n{self.color}\n{self.noches}')

    def calcular_pago(self):
        print("Total a pagar:",self.noches*100)


placas = input("Ingrese la nomenclatura de su placa: ")
marca = str(input("Ingrese su marca: "))
modelo = input("Ingrese el modelo: ")
color = str(input("Ingrese el color: "))
hora = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
noches = int(input("Ingrese las noches a hospedarse: "))
menu = str(input("Eliga la opcion de datos a imprimir: "))
estacionamiento1 = estacionamiento(placas,marca,modelo,color,hora,minutos)
pension1 = pension(placas,marca,modelo,color,noches)

if menu == 'E':
    estacionamiento1.mostrar()
    estacionamiento1.calcular_pago()

if menu == 'P':
    pension1.mostrar()
    pension1.calcular_pago()