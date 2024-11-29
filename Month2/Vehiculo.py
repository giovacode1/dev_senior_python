class Vehiculo:
    def __init__(self , tipo):
        self.tipo = tipo 

    def descripcion(self):
        return f"Este vehiculo es de tipo{self.tipo}"
    
class  Moto(Vehiculo):

    def __init__(self, tipo ,marca):
        super().__init__(tipo)#atributo de la clase madre 
        self.marca = marca 

moto1 = Moto("Motocicleta", "Honda")
print(moto1.descripcion())