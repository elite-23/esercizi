'''
1. Write a class called Student with the attributes name (str) and
studyProgram (str)

2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.

3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!

4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.
'''
class Student:
    def __init__(self, name :str, studyProgram :str):
        self.name=name
        self.studyProgram=studyProgram
        self.age=None
        self.gender=None
    
    def add_age(self, age :int):
        self.age=age
    
    def add_gender(self, gender :str):
        self.gender=gender

    def printInfo(self):
        
        print("Name:",self.name)
        print("Study program:",self.studyProgram)
        if self.age!=None:
            print("Age:",self.age)
        if self.gender!=None:
            print("Gender:",self.gender)
        print()
            
Gaia=Student("Gaia","Full-Stack")
Me=Student("Luca","Full-Stack")
Gimmi=Student("Gianmarco","Full-Stack")

Gaia.printInfo()
Me.printInfo()
Gimmi.printInfo()

Gaia.add_age(23)
Gaia.add_gender("Female")
Gaia.printInfo()

Me.add_age(21)
Me.add_gender("Male")
Me.printInfo()

Gimmi.add_age(25)
Gimmi.add_gender("Male")
Gimmi.printInfo()