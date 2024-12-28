from datetime import datetime, date
class Datos:
    def __init__(self,name, fecha, adress, phone) :
        self.name = name 
        self.fecha = fecha
        self.adress = adress
        self.phone = phone
        
    def calcular_edad(self):
        self.fecha = datetime.strptime(self.fecha, "%d-%m-%Y").date()
        hoy = date.today()
        self.edad = hoy.year - self.fecha.year - ((hoy.month, hoy.day) < (self.fecha.month,self.fecha.day))
        return self.edad
    
class Taxista(Datos):
    def __init__(self,name, fecha, adress, phone,no_licencia, no_placa):
        super().__init__(name, fecha, adress, phone)
        self.no_licencia = no_licencia
        self.no_placa = no_placa

    def tipoLicencia(self):
        super().calcular_edad
        if self.edad >= 18 and self.edad <= 30:
            print("Es tipo A")
        if self.edad >= 31 and self.edad <= 50:
            print("Es tipo B")
        


taxista1 = Taxista(input("Nmbre: "), input("Fecha de nacimiento: "), input("Direccion: "), input("Telefono"), input("Numero de licencia: "), input("No. placa"))
taxista1.calcular_edad()
print(taxista1.edad)
taxista1.tipoLicencia()
