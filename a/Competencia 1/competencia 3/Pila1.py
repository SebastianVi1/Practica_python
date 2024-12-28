class Pila:
    def __init__(self):
        self.items=[]
    def estaVacia(self):
        return self.items==[]
    def insertar(self,dato):
        self.items.append(dato)
    def extraer(self):
        self.items.pop()
    def inspeccionar(self):
        return self.items[len(self.items)-1]
    def tamaño(self):
        return len(self.items)
    def imprimir(self):
        print(self.items)

def evaluaexprecion(exp):
    pila=Pila()
    for ch in exp:
        if ch.isdigit():
            pila.insertar(int(ch))
        else:
            op2=pila.extraer()
            op1=pila.extraer()
            if ch=="+":
                pila.insertar(op1+op2)
            elif ch=="-":
                pila.insertar(op1-op2)
            elif ch=="*":
                pila.insertar(op1*op2)
            elif ch=="/":
                pila.insertar(op1//op2)
    return pila.extraer()
p= Pila()
p.insertar(13)
p.insertar(10)
p.insertar(8)  
p.imprimir()
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
                salida += pila.extraer()
            pila.extraer()
        elif ch.isdigit():
            salida+=ch
        else:
            while(True):
                if(pila.estaVacia()) or (prioridad(ch)>prioridad(pila.inspeccionar())):
                    pila.insertar(ch)
                    break
                else:
                    salida += pila.extraer()
    while not pila.estaVacia():
        salida+=pila.extraer()
    return salida
e=input("escribe la exprecion infija:")
print( e,":", convertir(e))



#841+*
#84*1+
#39*3+3/