class Pila:
    def __init__(self):
        self.items=[]
    def EstaVacia(self,dato):
        self.items.append(dato)

    def Insertar(self,dato):
        self.items.append(dato)
    
    def Tamaño(self):
        return self.items.pop()
    
    def Inspeccionar(self):
        return len(self.items)

    def Imprimir(self):
        print(self.items)
    
    def Extraer(self):
        return self.items.pop()

def evaluar_expresion(exp):
    pila = Pila()
    for ch in exp:
        if ch.isdigit():
            pila.Insertar(int(ch))
        else:
            op2= pila.Extraer()
            op1= pila.Extraer()
            if ch == "+":
                pila.Insertar(op1+op2)
            if ch == "-":
                pila.Insertar(op1-op2)
            if ch == "*":
                pila.Insertar(op1*op2)
            if ch == "/":
                pila.Insertar(op1//op2)
    return pila.Extraer()
e = input("Escribe la expresion postfija: ")
print(f"Exprecion {e} : {evaluar_expresion(e)}")



