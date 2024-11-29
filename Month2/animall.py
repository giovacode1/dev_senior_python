class animall: 
    cantidadAnimales = 0

    def __init__(self, name):
        self.name = name 
        animall.cantidadAnimales += 1

#!investigar sobre los decoradores 
    @classmethod
    def totalAnimales(cls):
        return f"tengo {cls.cantidadAnimales} animalitos"


animalito1 = animall("Ron")
animalito2 = animall("Rayo")
animalito3 = animall("Sexo")
print(animall.cantidadAnimales)
print(animalito3.name)
print(animall.totalAnimales( ))