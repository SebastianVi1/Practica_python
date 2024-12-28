class Cuenta:
    def __init__(self,no_cuenta,nombre_cliente, saldo_anual):
        self.no_cuenta = no_cuenta
        self.nombre_cliente = nombre_cliente
        self.saldo_anual = saldo_anual
        self.interes = 1.68

    def mostrar(self):
        print(f"Su numero de cuenta es: {self.no_cuenta}")
        print(f"Nombre : {self.nombre_cliente}")
        print(f"Su saldo es de : {self.saldo_anual}")
        print(f"El porcentaje de sus intereses es de: {self.interes}")

    def intereses(self):
        interes = (self.saldo_anual /100)*self.interes
        saldo_interes = self.saldo_anual + interes
        return f"Su saldo ya con interes incluido es de: {interes}"

    def regalo(self):
        if self.saldo_anual > 10000:
            return "Usted a obtenido un regalo"
        else:
            return "No acredita a ningun regalo"
        
a1 = Cuenta(2352,"sebastian",4500)
a1.mostrar()
print(a1.intereses())
print(a1.regalo())