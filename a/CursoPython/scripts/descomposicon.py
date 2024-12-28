import sys
if len(sys.argv) == 2:
    numero = str(int(sys.argv[1]))
    lenght = len(numero)

    for i in range(lenght):
        print("{:04d}".format(int(numero[lenght-1-i]) * 10 ** i))
    
else:
    print("error tiene que poner solo un argumento entero")