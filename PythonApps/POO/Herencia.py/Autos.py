class Autos:
    def __init__(self,placa, marca, modelo, mes):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo 
        self.mes = mes
        self.pago = 0

    def mes(self):
        if self.mes > 0 and self.mes<= 12:
            return True
        
    def getPago(self):
        if self.mes == 1:
            self.pago = 1500
        if self.mes == 2:
            self.pago = 1800
        if self.mes == 3:
            self.pago = 2000
        else:
            self.pago = 2800

        return self.pago
    
    def mostrar(self,pago):
        print(f"placa de auto: {self.placa}")
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo} ")
        print(f"cantidad a pagar {pago}")

    

auto = Autos(input("placa: "), input("marca: "),input("modelo"), int(input("mes:")))
auto.mostrar(auto.getPago())

