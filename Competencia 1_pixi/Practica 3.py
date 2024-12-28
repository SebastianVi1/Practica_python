class Nodo:
    def __init__(self,dato= None,sig= None):
        self.dato = dato
        self.sig = sig
class listaEnlazada:
    def __init__(self):
        self.inicio = None
    def agregarfrente(self,dato):
        self.inicio= Nodo(dato=dato,sig= self.inicio)
    def agregarfinal(self, dato):
        if not self.inicio:
            self.inicio = Nodo(dato = dato)
            return
        actual = self.inicio
        while (actual.sig):
            actual = actual.sig
        actual.sig = Nodo(dato = dato)
    def obtenerultimonodo(self):
        temp = self.inicio
        while (temp.sig is not None):
            temp = temp.sig
        return temp.dato
    def obtenerpimernodo(self):
        return self.inicio.dato
    def imprimirlista(self):
        Nodo = self.inicio
        while Nodo!= None:
            print(Nodo.dato, end=" =>")
            Nodo = Nodo.sig
    def esvacia(self):
        return self.inicio == None
s = listaEnlazada()
if s.esvacia():
    print("la lista esta vacia")
else:
    print("la lista no esta vacia")
s.agregarfrente(8)
s.agregarfrente(6)
s.agregarfinal(5)
if s.esvacia():
    print("la lista esta vacia")
else:
    print("la lista no esta vacia")
s.imprimirlista()
print("\n")
print("el ultimo elemento es:", s.obtenerultimonodo())
print("el primer elemento es:", s.obtenerpimernodo())