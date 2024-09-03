'''
Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal
'''

class Animal:
    def __init__(self, name :str, specie :str, legs :int) -> None:
        self.name=name
        self.specie=specie
        self.legs=legs        
    
    def Set_legs(self,legs :int):
        self.legs=legs
    
    def Get_legs(self):
        return self.legs

    def printInfo(self):
        print("Name:",self.name)
        print("Specie:",self.specie)
        print("Number of legs:",self.legs,"\n")

giraffe=Animal("Giraffe","Mammal",4)
crow=Animal("Crow","Oviparous",2)

print("Giraffe's legs:",giraffe.legs)
print("\nCrow's legs:",crow.legs)

crow.legs=3
print("\nCrow's modified legs:",crow.legs)

giraffe.Set_legs(1)
print("Giraffe's modified legs:",giraffe.legs)

giraffe.printInfo()
crow.printInfo()
