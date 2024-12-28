class Nodo:
    def __init__(self, dato=None, sig=None):
        self.dato = dato
        self.sig = sig

class ListasEnlazada:
    def __init__(self) -> None:
        self.inicio = None


    def agregarFrente(self, dato):
        self.inicio = Nodo(dato=dato, sig=self.inicio)

    def agregarFinal(self,dato):
        if not self.inicio:
            self.inicio = Nodo(dato=dato)
            return 
            actual = self.inicio
            while(actual.sig):
                actual.sig = Nodo(dato=dato)
    


    def imprimirLista(self):
        Nodo= self.inicio
        while Nodo!= None:
            print(Nodo.dato, end="->")
            Nodo= Nodo.sig  

    def esVacia(self):
        return self.inicio == None

s= ListasEnlazada()
s.agregarFinal(3)
s.agregarFinal(4)
s.agregarFinal(5)
if s.esVacia():
    print("la lista esta vacia")
else:
    print("la lista no esta vacia")
s.imprimirLista()

      
        