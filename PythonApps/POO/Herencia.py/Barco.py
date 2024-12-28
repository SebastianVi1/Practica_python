class Cbarco():
    def __init__(self,lenght, capacity, model, hours, people,prices=0):
        self.__lenght = lenght
        self.__capacity = capacity
        self.model = model
        self.hours = hours
        self.__people = people
        self.prices = prices
    
    def getLenght(self):
        return self.__lenght

    def setLenght(self,lenght):
        self.__lenght = lenght

    def getCapacity(self):
        return self.__capacity

    def setCapacity(self,capacity):
        self.__capacity = capacity

    def getPeople(self):
        return self.__people

    def setPeople(self,people):
        self.__people = people
        if self.__people > self.__capacity:
            print("Excedio el limite de capacidad")

    def rent(self):
        finalPrice = 0
        if self.__capacity == 100:
            self.prices = 1500
            finalPrice = self.prices * self.hours
            return f"El precio a pagar es de {finalPrice}"
        if self.__capacity == 10:
            self.prices = 800
            finalPrice = self.prices * self.hours
            return f"El precio a pagar es de {finalPrice}"

        if self.__capacity == 15:
            self.prices = 1000
            finalPrice = self.prices * self.hours
            return f"El precio a padar es de {finalPrice}"

        if self.__capacity == 7:
            self.prices = 1000
            finalPrice = self.prices * self.hours
            return f"El precio a padar es de {finalPrice}"

class Cvelero(Cbarco):
    def __init__(self, lenght, capacity, model, hours, people, prices=0):
        super().__init__(lenght, capacity, model, hours, people, prices)

        super().setCapacity(10)
        super().rent()

class Clancha(Cbarco):
    def __init__(self, lenght, capacity, model, hours, people, prices=0):
        super().__init__(lenght, capacity, model, hours, people, prices)

        super().setCapacity(7)
        super().rent()

class CYate(Cbarco):
    def __init__(self, lenght, capacity, model, hours, people, prices=0):
        super().__init__(lenght, capacity, model, hours, people, prices)

        super().setCapacity(15)          

print("Centro de embarcaciones El Velero")
print("Seleccionar una opcion")
print("1. Barco")
print("2. Yate ")
print("3. Velero")
print("4. Lancha")
print("5. Salir")

while True:
    opcion = int(input())
    if opcion == 1:
        barco1 = Cbarco(132,12,input("Modelo: "),int(input("Horas: ")),0)
        barco1.setCapacity(100)
        barco1.setPeople(int(input("cantidad de personas")))
            
        print(barco1.rent())
    if opcion == 2:
        yate1 = CYate(132,12,input("Modelo: "),int(input("Horas: ")),0)
        yate1.setPeople(int(input("cantidad de personas:")))
            
        print(yate1.rent())
    if opcion == 3:
        velero = Cvelero(132,12,input("Modelo: "),int(input("Horas: ")),0)
        velero.setPeople(int(input("cantidad de personas:")))
        print(velero.rent())
    if opcion == 4:
        lancha = Clancha(132,12,input("Modelo: "),int(input("Horas: ")),0)
        lancha.setPeople(int(input("cantidad de personas:")))
        print(lancha.rent())
    if opcion == 5:
        break