from random import randint

vectorbs= []
for i in range(10):
    random = randint(1,100)
    vectorbs.append(random)

def bubllesort(vectorbs):
    print("El vector a ordenar es:", vectorbs)
    n=0
    for _ in vectorbs:
        n += 1 
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if vectorbs[j]   > vectorbs[j+i]:
                vectorbs[j], vectorbs[j+i] = vectorbs [j+1], vectorbs[j]
    print("El vector ordenado es:", vectorbs)
bubllesort(vectorbs)

S