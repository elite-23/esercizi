class Room():
    def __init__(self, id :str, floor:str, seats:str) -> None:
        self.id=id
        self.floor=floor
        self.seats=seats
    
    def get_id(self):
        return self.id

    def get_floor(self):
        return self.floor
    
    def get_seats (self):
        return self.seats

    def __str__(self) -> str:
        return f"Room(id={self.id}, floor={self.floor}, seats={self.seats})"

class Building():
    def __init__(self, name :str, address :str, floors :tuple{int}) -> None:
        self.name :str=name
        self.address :str=address 
        self.floors :int=floors
        self.rooms :list[Room]=[] 

    def get_floors(self):
        return self.floors

    def add_room(self,room:Room):
        floors=self.floors
        if room and isinstance(room,Room) and room not in self.rooms and floors[1]>=room.get_floor()<=floors[0]:
            self.rooms.append(room)
    
    def __str__(self) -> str:
        s= f"{self.name} @ {self.address}\n"
        s+= "With rooms:\n"
        for i in self.rooms:
            s+=i.__str__()+"\n"


class Person:

    def __init__(self, cf, name, surname, age) -> None:
        self.cf=cf
        self.name=name
        self.surname=surname
        self.age=age

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (cf={self.cf}, name={self.name}, surname={self.surname}, age={self.age})"

class Student(Person):
    def __init__(self, cf, name, surname, age, matricola) -> None:
        super().__init__(cf, name, surname, age)
        self.matricola=matricola

    def __str__(self) -> str:
        return super().__str__()

class Group:
    def __init__(self, name, limit) -> None:
        self.name=name
        self.limit=limit
        self.limit_lecturer=len(self.students)//10
        self.students: list[Student]=[]
        self.lecturers :list[Lecturer]=[]
        
    def get_name(self):
        return self.name

    def get_limit(self):
        return self.limit
        
    def get_students(self):
        return self.students
    
    def get_limit_lecturer(self):
        return min(len(self.students) //10,1)

    def add_student(self,student:Student):
        if student and isinstance(student,Student) and student not in self.students and  self.limit>0:
            self.students.append(student)
            student.set_group(self)
            self.limit-=1
    
    def add_lecturer(self, lecturer:Lecturer):
        if lecturer and lecturer not in self.lecturers and self.get_limit_lecturer()>0:
