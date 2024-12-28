class FigurasGeometricas:
    def __init__(self):
        self.__figuraGeometrica = ''
    
    def getfigu(self):
        return self.figuraGeometrica
    def setfigu(self,figurasGeometricas):
        self.__figuraGeometrica = figurasGeometricas
        
    def getRadio(self):
        return self.radio
    def setRadio(self, radio):
        self.radio = radio
class Circulo(FigurasGeometricas):  
    def __init__(self, radio,pi):
        self.radio = radio
        self.pi = 3.1416
    def area(self):
        print(f'yo soy '+ self.setRadio(2345))
        return "El area es de ", self.pi * self.radio**2

class Cuadrado:
    def __init__(self,lado1):
        self.lado1 = lado1

    def area(self):
        return 'Su area es de', self.lado1 * self.lado1
    
    def perimetro(self):
        return 'su perimetro es de ', self.lado1*4
    

class Rectangulo:
    def __init__(self,lado1, base) :
        self.lado1 = lado1
        self.base = base
    def area(self):
        return 'Su area es de', self.lado1 * self.base

    def perimetro(self):
        return 'su perimetro es de ', (self.lado1**2)+(self.base**2)
    
class Triangulo:
    def __init__(self,base, altura, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return 'su area es de : ', (self.base * self.altura) / 2
    def perimetro(self):
        return 'su perimetro es de: ', self.base + self.lado2 +self.lado3

class Trapecio:
    def __init__(self,altura, baseMenor, baseMayor,ladoIzquierdo) :
        self.altura = altura
        self.baseMenor = baseMenor
        self.baseMayor = baseMayor
        self.ladoIzquierdo = ladoIzquierdo

    def area(self):
        return 'el area de tu trapecio es de :', ((self.baseMenor + self.baseMayor) * self.altura)/2

    def perimetro(self):
        return 'el perimetro de tu trapecio es de: ', self.baseMayor + self.baseMenor + (self.ladoIzquierdo**2)

print("Bienvenido a la calcuadora de areas y perimetros. ")
print("Que figura desea analizar? ")
print("Cuadrado")
print("Circulo")
print("Rectangulo")
print("Trapecio")
resp = input("").lower()
if resp == "cuadrado":
    cuadrado = Cuadrado(int(input("lado: ")))
    print(cuadrado.area())
    print(cuadrado.perimetro())
if resp == "circulo":
    circulo = Circulo(input("Cual es e radio: "))
    
    print(circulo.area())
    print(circulo.perimetro())
if resp == "rectangulo":
    rectangulo = Rectangulo(input("lado:"),input("base: "))
    print(rectangulo.area())
    print(rectangulo.perimetro())
if resp == "trapecio":
    trapecio = Trapecio(input("Altura:"), input("Base menor: "),input("Base mayor: "), input("Lado: "))
    print(trapecio.area())
    print(trapecio.perimetro())
if resp == "triangulo":
    triangulo = Triangulo(input("Base: "), input("Altura"), input("Lado izquierdo: "), input("Lado derecho: "))
    print(triangulo.area())
    print(triangulo.perimetro())