vector = [55,8,2,44,95,65,32,45]
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

print("Lista",vector)
vb=int(input("Escribe el valor a buscar: "))
p=busquedasecuencial(vector,vb)

if(p!=-1):
    print("Valor encontrado en la pocision ",p+1)
else:
    print("Valor NO encontrado")

