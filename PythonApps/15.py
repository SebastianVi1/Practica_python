nEmpleados = int(input(´Coloque numero de empleados´))
for i in range(nEmpleados):
    n =int(input('Numero de ventas: '))
    mayorMil = 0
    montototalMil = 0
    montototalQuin = 0
    montototal0 = 0
    mayorQuin = 0
    menorQuin = 0

    for i in range(n):
        precio = int(input('Coloque el precio'))
        if precio > 1000:
            mayorMil += 1
            montototalMil += precio
        elif precio > 500 and precio <=1000:
            mayorQuin += 1
            montototalQuin += precio
        elif precio > 500:
            menorQuin += 1
            montototal0 += precio

    print(montototalMil)
    print(montototalQuin)