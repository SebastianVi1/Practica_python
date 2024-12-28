class Nodo:
    def __init__(self,dato, padre) -> None:
        self.dato = dato 
        self.padre = padre 
        self.izq=None
        self.der=None
    def getDato(self):
        return self.dato
    def setDato(self,dato):
        self.dato=dato
    def getIzq(self):
        self.izq
    def setIzq(self, dato):
        self.dato = dato 
    def getDer(self):
        return self.der
    def setDer(self,dato):
        self.dato = dato
    def getPadre(self):
        return self.padre
    def setPadre(self, padre):
        self.padre = padre



class Abo:
    def __init__(self) -> None:
        self.raiz = None
    def insertar (self, dato):
        nuevo = Nodo(dato,None)
        if self.empty():
            self.raiz = nuevo
        else :
            actual =self.raiz
            while actual  is not None:
                padre = actual
                if nuevo.getDato() < actual.getDato():
                    actual = actual.getIzq()
                else:
                    actual = actual.getDer()
            if nuevo.getDato()< padre.getDato():
                padre.setIzq(nuevo)
            else:
                padre.setDer(nuevo)
            nuevo.setPadre(padre)