class cuenta():
    def __init__(self,propietario,saldo,moneda):
        self.__propietario = propietario
        self.__saldo = saldo
        self.__moneda = moneda

    def getSaldo(self):
        return self.__saldo

    def getPropietario(self):
        return self.__propietario

    def getMoneda(self):
        return self.__moneda

    def setMoneda(self,moneda):
        self.__moneda= moneda

cuenta1 = cuenta("Andre",15000,"dolares")
print(cuenta1.getSaldo())
print(cuenta1.getMoneda())
cuenta1.setMoneda("pesos")
print(cuenta1.getMoneda())