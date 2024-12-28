import random
a=random.randint(1,50)
c=0
e=False
while c<5:
    c=c+1
    n=int(input("ADivina el numero aleatorio:"))
    if n==a:
        print("Felicidades, adivinaste el numero!!!")
        print("")
        print("Lo hiciste en",c,"oportunidades")
        e=True
        break
    elif(n<a):
        print("El numero aleatorio es mayor")
    else:
        print("El numero aleatorio es menor")
if not e:
    print("Se terminaron las oportunidades, el numero aleatorio era",a)