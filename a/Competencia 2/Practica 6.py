def positivo(n):
    if n > 0:
        return True
    else:
        return negativo(n)
def negativo (n):
    if n < 0:
        return False
    else:
        return positivo(n)
n = int(input("ingresar un numero:"))
if positivo(n):
    print("positivo")
else:
    print("negativo")