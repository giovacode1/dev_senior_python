class Animal: 

    def __init__(self, name , age): 
                 self.name = name
                 self.age = age 
    
    def saludar(self):
            return f"Mi animalito se llama {self.name} y tiene {self.age} años"
    
animal1 = Animal("Ginebra", 3 )
#!el objeto va en minuscula siempre 

print(animal1.name)
print(animal1.age)

print(animal1.saludar())

#* metodos de clases en python 
