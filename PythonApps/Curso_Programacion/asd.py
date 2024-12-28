lista =[]
n = input()
lista = n.split(" ")
n1,k = int(lista[0]),lista[1]

lista_inputs = []
lista_listas = []
lista2 =[]
a= []
for i in range(n1):
    entrada = input()
    lista_inputs.append(entrada)
    for splits in lista_inputs:
        lista_listas = splits.split(" ")
    lista2.append(lista_listas)


for h in lista2:
    print(h)
    for k in h:
        a.append(k[1]) 
    print(a)
    


print("Lista de inputs:", lista_inputs)