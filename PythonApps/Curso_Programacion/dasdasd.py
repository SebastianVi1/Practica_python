def solution(n):
    lista = []
    lista_inputs = []
    n = input()
    lista = n.slplit(" ")
    n1, k = int(lista[0]), int(lista[1])
   

    lista_inputs = []
    for i in range(n1):
        entrada = input(i+1)
        lista_inputs.append(entrada)
    print(lista_inputs)