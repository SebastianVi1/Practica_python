class Cuenta():
    def __init__(self,propetario, saldo, moneda):
        self.__propetario = propetario
        self.saldo = saldo 
        self.moneda = moneda

    def getPropetario(self):
        return self.__propetario

    def getSaldo(self):
        return self.__saldo

    def getMoneda(self):
        return self.__moneda

    def setMoneda(self,moneda):
        self.__moneda= moneda


cuenta1 = Cuenta("sebas",120000,"dolares")
print(cuenta1.getPropetario())
print(cuenta1.getSaldo())
print(cuenta1.getMoneda())
cuenta1.setMoneda("pesos")
print(cuenta1.getMoneda)
