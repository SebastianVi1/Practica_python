num = int(input("ingrese un numero:"))
resultado = 1

for i in range(1,num + 1):
    resultado=i*resultado
print(resultado)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n-1)
num = int(input("ingrese un numero:"))