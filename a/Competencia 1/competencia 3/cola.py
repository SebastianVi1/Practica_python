class Cola:
    def __init__(self):
        self.items=[]

    def insertar(self,dato):
        self.items.append(dato)

    def extraer(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")
        
    def estaVacia(self):

        return self.items==[]
    
    def imprimir(self):
        print("Elementos en la cola")
        print(self.items)

c = Cola()
c.insertar(56)
c.insertar(32)
c.insertar(67)
c.imprimir()
print("Valor extraido :",c.extraer())
c.insertar(45)
c.imprimir()

while True:
    num = int(input("Coloque 1 para ingresar, 2 para extraer y 3 para imprimir, otro numero para salir "))
    
    if num == 1:
        nom = input("coloca tu nombre")
        c.insertar(nom)
    elif num == 2:
        print(f"valor extraido {c.extraer()}")
    elif num == 3:
        c.imprimir()
    else:
        break