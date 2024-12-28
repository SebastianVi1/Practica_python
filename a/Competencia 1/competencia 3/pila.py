class Pila:
    def __init__(self):
        self.items=[]
    def estaVacia(self,dato):
        self.items.append(dato)

    def insertar(self,dato):
        self.items.append(dato)
    
    def tamaño(self):
        return len(self.items)

    def imprimir(self):
        print(self.items)
    
    def extraer(self):
        return self.items.pop()

"""""

p=Pila()
p.Insertar(34)
p.Insertar(41)
p.Insertar(5)
p.Imprimir()
p.Extraer()
print(p.Tamaño())
p.Imprimir()


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
"""
def prioridad(ch):
        if(ch=="*") or (ch=="/"):
            return 3
        elif (ch == "+") or (ch == "-"):
            return 2
        elif (ch == "(") or (ch == ")"):
            return 1
def convertir(exp):
    pila=Pila()
    salida=''
    for ch in exp:
        if ch=="(":
            pila.insertar(ch)
        elif ch==")":
            while(pila.inspeccionar!="("):
                salida+=pila.extraer()
            pila.extraer()
        elif ch.isdigit():
            salida+=ch
        else:
            while(True):
                if(pila.estaVacia()) or (prioridad(ch)>prioridad(pila.inspeccionar())):
                    pila.insertar(ch)
                    break
                else:
                    salida+=pila.extraer()
    while not pila.estaVacia():
        salida+=pila.extraer()
    return salida
e=input("escribe la exprecion infija:")
print( e,":", convertir(e))