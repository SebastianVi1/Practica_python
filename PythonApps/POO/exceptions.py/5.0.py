try:
    list = ["python", "java","c++","c#"]
    index = int(input("ccoloqeu el indice de la lista"))
    print("El lenguaje que estaba en el indice es ", list[index])
    

except IndexError:
    print("El indice que puso no funciona")
    index = input("coloque el indice de la lista")
    print("El lenguaje que estaba en el indice es ", list[index])
