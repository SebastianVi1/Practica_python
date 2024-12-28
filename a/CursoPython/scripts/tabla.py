import sys
print(sys.argv)
if len(sys.argv)== 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("El rango tiene que estar entre 1-9")
    else:
        for fila in range(filas):
            for columna in range(columnas):
                print("*", end=" ")
            print("")

else:
    print("error debe utilizar dos arugmentos ")
    print("ejemlo: tabla.py [1-10] [1-10]")

