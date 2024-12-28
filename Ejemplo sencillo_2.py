class persona():
    institucion = 'ITSSP'

    def __init__(self, apePat, apeMat, nom):
        self.apePat = apePat
        self.apeMat = apeMat
        self.nom = nom

    def mostrar(self):
        print(f'nombre completo: {self.nom} {self.apePat} {self.apeMat}')

class estudiante(persona):
    def __init__(self,apePat,apeMat,nom,nc,carrera):
        super().__init__(apePat,apeMat,nom)
        self.nc = nc
        self.carrera = carrera

    def mostrar(self):
        super().mostrar()
        print(f'numero de control: {self.nc}')
        print(f'carrera: {self.carrera}')

class secretaria(persona):
    def __init__(self,apePat,apeMat,nom,area):
        super().__init__(apePat,apeMat,nom)
        self.area = area

    def mostrar(self):
        super().mostrar()
        print(f'area: {self.area}')


class docente(persona):
    def __init__(self, apePat, apeMat, nom,grado, academia):
        super().__init__(apePat, apeMat,nom)
        self.academia = academia
        self.grado = grado

    def mostrar(self):
        super().mostrar()
        print(f'academia fue: {self.academia}')
        print(f'su grado es de: {self.grado}')


apePat = str(input("Ingrese su apellido paterno: "))
apeMat = str(input("Ingrese su apellido materno: "))
nom = str(input("Ingrese su nombre: "))
nc = int(input("Ingrese su numero de control: "))
carrera = str(input("Ingrese su carrera: "))
area = str(input("Ingrese su area: "))
grado = int(input("Ingrese su grado: "))
academia = str(input("Ingrese su academia: "))

print("Hola ¿cuales datos quieres?: ")
t = str(input())
if t == 'estudiante':
        estudiante1 = estudiante(apePat,apeMat,nom,nc,carrera)
        estudiante1.mostrar()

elif t == 'secretaria':
        secretaria1 = secretaria(apePat,apeMat,nom,area)
        secretaria1.mostrar()

elif t == 'docente':
        docente1 = docente(apePat, apeMat, nom,grado, academia)
        docente1.mostrar()



