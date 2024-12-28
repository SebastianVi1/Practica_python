class Person():
    def __init__(self,name, adress):
        self.__name = name
        self.__adress = adress

    def getName(self):
        return self.__name 
    
    def setName(self,name):
        self.__name = name
    
    def setAdress(self,adress):
        self.__adress = adress
    
    def getAdress(self):
        return self.__name
    
class CTeacher(Person):
    def __init__(self,subject,name, adress):
        super().__init__(name, adress)
        self.__subject = subject 
        

    def getSubjet(self):
        return self.__subject 
    
    def setSubject(self,subject):
        self.__subject = subject

class CStudent(Person):
    def __init__(self,school, name, adress):
        super().__init__(name, adress)
        self.__school = school 

    def getSchool(self):
        return self.__school
        
    def setSchool(self,school):
        self.__school = school

class CInternationalStudent(CStudent):
    def __init__(self,country, school, name, adress):
        super().__init__(school, name, adress)
        self.__country = country

    def getCountry(self):
        return self.__country
        
    def setCountry(self,country):
        self.__country = country
            

print("********Welcome**********")
print("Who are you?")
print("1. Person")
print("2. Teacher ")     
print("3. student")
print("4. International Student")

a = int(input())
if a == 1:
    person1 = Person(input("Name: ", input("Adress: ")))
if a == 2:
    teacher1 = CTeacher(input("Subject: "), input("Name: "), input("Adress: "))
                        
if a == 3:
    student1 = CStudent(input("School: "), input("Name: "), input("Adress: "))

if a == 4:
    istudent1 = CInternationalStudent(input("country:"),input("School: "), input("Name: "), input("Adress: "))