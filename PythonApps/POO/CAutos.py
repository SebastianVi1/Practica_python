class CAutos:
    def __init__(self,nombre, ventas_anuales):
        self.nombre = nombre
        self.ventas_anuales = ventas_anuales 
        self.comision_anual = 0

    def comision(self):
        if self.ventas_anuales >1000000 and self.ventas_anuales <= 3000000:
            self.comision_anual =(self.vetas_anuales /100) *3
            

        elif self.ventas_anuales >=3000000 and self.ventas_anuales <= 5000000:
            self.comision_anual = (self.vetas_anuales /100) *4
            

        elif self.ventas_anuales >=5000000 and self.ventas_anuales <= 5000000:
            self.comision_anual = (self.vetas_anuales /100) *5
            

    def mostrar(self):
        print(f"{self.nombre} Sus ventas anuales son: {self.ventas_anuales} su comision por sus ventas es de {self.comision_anual} ")

    def inicializar(self):
        self.ventas_anuales = 0
        self.comiison_anual = 0
        
    

cliente1 = CAutos("sebastian",6000000)
cliente1.mostrar()
cliente1.inicializar()
