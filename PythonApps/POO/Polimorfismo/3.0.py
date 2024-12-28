class Empleado:
    def __init__(self,__horasTrabajadas, __sueldoporHoras) :
        self.__horasTrabajadas = __horasTrabajadas
        self.__sueldoporHoras  = __sueldoporHoras
        self.base = 0
        self.total = 0
    def gethorasTrabajadas(self):
        return self.__horasTrabajadas
    def sethorasTrabajadas(self, horas):
        self.__horasTrabajadas = horas 

    def getsueldoporHoras(self):
        return self.__sueldoporHoras
    def setsueldoporHoras(self, sueldo):
        self.__sueldoporHoras= sueldo     


     
    def calcularsalario(self):
        
        if int(self.__horasTrabajadas) > 40 and int(self.__horasTrabajadas < 42):
                return (self.__sueldoporHoras * 40)+ self.__sueldoporHoras*2 
        

        elif int(self.__horasTrabajadas) > 41 and int(self.__horasTrabajadas) < 46:
            self.base= 40 * self.__sueldoporHoras
            a = (self.__horasTrabajadas - 40) * self.__sueldoporHoras*2
         
            return a+self.base
        
        elif self.__horasTrabajadas > 45:
            self.base= 40 * self.__sueldoporHoras
            a = (self.__horasTrabajadas - 40)* self.__sueldoporHoras*3
            
            return a + self.base
        else:
            return self.__horasTrabajadas * self.__sueldoporHoras
        
class EmpleadosSinHorasExtra(Empleado):
    def __init__(self, __horasTrabajadas, __sueldoporHoras):
        super().__init__(__horasTrabajadas, __sueldoporHoras)

efe = Empleado(0,0)
efe.sethorasTrabajadas(int(input('Horas Trabajadas: ')))
efe.setsueldoporHoras(float(input('Sueldo por hora: ')))
print(efe.calcularsalario()) 