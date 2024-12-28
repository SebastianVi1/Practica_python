def solucion(input):
    lista = []
    lista2 = []
    lista = input.split(" ")
    n,k =int(lista[0]), int(lista[1])
    suma = 0
    total = 0
    for i in range(1,n):
        print(i)
        suma = i**k
        total += suma
        print(total)
    return print(total)
solucion("5 10")

