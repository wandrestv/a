def multiplicar(valor1,*args,**kwargs):
    print(valor1)
    print(args)
    print(kwargs)
    #for ele in args:
    #    print(ele)
#multiplicar(50,2, 5, 6, "ok", nombre = "Ana", sueldo = 500)

class Empleado:
    nombre = "Vacante"
    def __init__(self, cargo):
        self.cargo = cargo
    def mostrar (self):
        print(self.nombre, self.cargo)

class Obrero(Empleado):
    nombre = "Jose"
    def __init__(self, car, sueldo):
        super().__init__(car)
        self.sueldo = sueldo
    def mostrar (self):
        #print(self.nombre, self.cargo,self.sueldo)
        super().mostrar()
        print(self.sueldo)

obr = Obrero("amatista", 500)
obr.mostrar()        


        