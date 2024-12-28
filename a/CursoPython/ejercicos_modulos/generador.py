import random 
import math

def leer_numero(ini, fin, mensaje = None):
    print(mensaje)
    numero = int(input("coloca un numero: "))
    
    while True:
        if numero >= ini and numero <= fin:
            break
        else:
            numero = int(input("Que sea entre {} y {} -coloca un numero: ".format(ini, fin)))
    return numero

def generador():
    numeros = leer_numero(1,20,"Cuantos numero quieres generar? [1-20]")
    modo = leer_numero(1,3,"Como quieres redondear los numeros?\n1. Al alza\n2. A la baja\n3. Normal")
    lista_numeros = []
    for i in range(1,numeros):
        numero_aleatorio = random.uniform(0,101)
        if modo == 1:
            print(numero_aleatorio)
            lista_numeros.append(math.ceil(numero_aleatorio))
        if modo == 2:
            print(numero_aleatorio)
            lista_numeros.append(math.floor(numero_aleatorio))
        else:
            print(numero_aleatorio)
            lista_numeros.append(round(numero_aleatorio))
    return lista_numeros


print(generador())