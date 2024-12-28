vector = [45,67,23,12,98,6,54,36]
def busquedasecuencial(vector,vb):
    encontrado=-1
    pocision=0
    for i in vector:
        pocision=pocision+1
        if(vb==i):
            encontrado=pocision
    return encontrado

def busquedabinaria(vector,vb):
    izq=0
    der=len(vector)-1
    while izq<=der:
        medio=int((izq+der)/2)
        if vector[medio]==vb:
            return medio
        elif vector[medio]>vb:
            der=medio=1
        else:
            izq=medio+1
    return -1


vb=int(input("Escribe el valor a buscar: "))
p=busquedabinaria(vector,vb)
if(p!=-1):
    print("Valor encontrado en la pocision ",p)
else:
    print("Valor NO encontrado")



