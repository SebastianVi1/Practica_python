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

    def valMeses(self):
        if self.mes == 1:
            self.mes = "Enero"
        if self.mes == 2:
            self.mes = "Febrero"
        if self.mes == 3:
            self.mes = "Marzo"
        if self.mes == 4:
            self.mes = "Abril"
        if self.mes == 5:
            self.mes = "Mayo"
        if self.mes == 6:
            self.mes = "Junio"
        if self.mes == 7:
            self.mes = "Julio"
        if self.mes == 8:
            self.mes = "Agosto"
        if self.mes == 9:
            self.mes = "septiembre"
        if self.mes == 10:
            self.mes = "octubre"
        if self.mes == 11:
            self.mes = "Noviembre"
        if self.mes == 12:
            self.mes = "Diciembre"

auto = Autos(input("placa: "), input("marca: "),input("modelo"), int(input("mes:")))
auto.mostrar(auto.getPago())

