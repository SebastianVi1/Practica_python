class cola:
    def __init__(self):
        self.items=[]
    def insertar(self, dato):
        self.items.append(dato)
    def extraer(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("la cola esta vacia")
    def estaVacia(self):
        return self.items==[]
    def imprimir(self):
        print("elememtos en la cola")
        print(self.items)
c=cola()
while (True):
    op=int(input("escribe 1 para ingresar, 2 para extraer, 3 imprimir, otro numero para salir"))
    if(op==1):
        n=input("Escribe tu nombre: ")
        c.insertar(n)
    elif(op==2):
        print("Valor extraido: ",c.extraer())
    elif(op==3):
        c.imprimir()
    else:
        break

