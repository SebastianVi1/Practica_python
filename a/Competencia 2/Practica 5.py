def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
num = int(input("ingrese un numero:"))
print("el factorial de",num, "es:", factorial(num))