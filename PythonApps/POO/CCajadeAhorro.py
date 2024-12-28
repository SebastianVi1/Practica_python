class CCajaAhorro():
    def __init__(self,nombre, dinero):
        self.nombre = nombre 
        self.dinero = dinero
        self.ahorro = 0 

    def ahorrar(self):
        self.ahorro += self.dinero
        return self.ahorro


    def retirar(self):
        cantidad = int(input("cantidad a retirar"))
        self.ahorro = self.ahorro - cantidad
        return self.ahorro

    def saldo(self):
        return f"su saldo es de {self.ahorro}"

    def mostrar(self):
        print("**************************************************")
        print(f"****{self.nombre} tiene ahorrado  {self.ahorro}***")
        print("**************************************************")
print("Socio 1")
caja1 = CCajaAhorro("sebastian",4500)
print(caja1.ahorrar())
print(caja1.retirar())
print(caja1.saldo())
print(caja1.mostrar())

print("Socio 2")
caja2 = CCajaAhorro("toño",4500)