class CCantante:
    def __init__(self):
        self.__nombre = ""

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    def canta(self):
        print("procede a cantar")

class LuisMiguel(CCantante):
    def canta(self):
            print("yo soy "+ self.getNombre()+ "y cnto asi : adsfjadsfasdfadsfj")

LuisMiguel.canta()