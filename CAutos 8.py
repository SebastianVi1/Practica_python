class autos():
    def __init__(self,placa,marca,modelo,mes,pago):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__mes = mes
        self.__pago = pago

    def getPlaca(self):
        return self.__placa

    def setPlaca(self,placa):
        self.__placa = placa

    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__placa = marca

    def getModelo(self):
        return self.__modelo

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getMes(self):
        if mes.lower == 'enero' or 'febrero' or 'marzo' or 'abril' or 'mayo' or 'junio' or 'julio' or 'agosto' or 'septeimbre' or 'octubre' or 'noviembre' or 'diciembre':
            print("Mes Valido")
        return self.__mes

    def setMes(self, mes):
        self.__mes = mes

    def getPago(self):
        if mes == 'enero':
            print("su pago es de: 1500")
        elif mes == 'febrero':
            print("su pago es de 1800")
        elif mes == 'marzo':
            print ("su pago es de 2000")
        elif mes == 'abril':
            print("su pago es de 2800")
        elif mes == 'mayo':
            print("su pago es de 2800")
        elif mes == 'junio':
            print("su pago es de 2800")
        elif mes == 'julio':
            print("su pago es de 2800")
        elif mes == 'agosto':
            print("su pago es de 2800")
        elif mes == 'septeimbre':
            print("su pago es de 2800")
        elif mes == 'octubre':
            print("su pago es de 2800")
        elif mes == 'noviembre':
            print("su pago es de 2800")
        elif mes == 'diciembre':
            print("su pago es de 2800")
        return self.__pago

    def setPago(self, pago):
        self.__pago = pago

placa = input("Ingrese la nomenclatura de su placa: ")
marca = str(input("Ingrese su marca: "))
modelo = str(input("Ingrese el modelo: "))
mes = str(input("Ingrese el mes: "))
pago = int(input("Ingrese el pago: "))
autos1 = autos(placa,marca,modelo,mes,pago)
print(autos1.getPlaca())
print(autos1.getMarca())
print(autos1.getModelo())
print(autos1.getMes())
print(autos1.getPago())

