class Person:
                                
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
print(bob.age)
if bob.age>alice.age:
    print(bob.name)
elif bob.age==alice.age:
    print(bob.name,"and", alice.name,"have the same age.")
else:
    print(alice.name)

People=[alice,bob]

alex=Person("Alex P.",77)
People.append(alex)

tizz=Person("Tiziano G.",21)
People.append(tizz)

gaia=Person("Gaia F.",23)
People.append(gaia)

min=None
for i in People:
    if min==None:
        min=i
    else:
        if i.age<min.age:
            min=i
print("The yungest is:",min.name)
