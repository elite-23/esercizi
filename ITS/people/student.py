from people.person import Person
class Student(Person):
    
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.group: Group = None
        
    def set_group(self, group):
        self.group = group
           