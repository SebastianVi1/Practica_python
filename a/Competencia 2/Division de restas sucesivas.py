contador = int(0)

dividendo = int(input("favor de ingresar dividendo:"))
divisor = int(input("favor de ingresar divisor:"))

dividendo = dividendo - divisor

while (dividendo >= 0):
    contador = contador + 1
    dividendo = dividendo - divisor
print("la division es igual a:" + str(contador))