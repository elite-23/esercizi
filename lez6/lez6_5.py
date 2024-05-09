class Person:
    def __init__(self, name :str, surname :str, birth_date :str) -> None:
        self.name :str = name
        self.surname :str = surname
        self.birth_date :str = birth_date
    
    def age_calculator(self, date :str) -> int :
        age :int=0
        birth :list[str] = self.birth_date.split("/")
        date :list[str] = date.split("/")
        
        if int(date[1])-int(birth[1])>=0:
            age+= 1
        
        age+= int(date[2]) - int(birth[2])
        return age
    
class Dipendente(Person):
    def __init__(self, name: str, surname: str, birth_date: str, ore_lavorate:int) -> None:

        super().__init__(name, surname, birth_date)
        self.ore_lavorate :int = ore_lavorate


class Professore(Dipendente):
    def __init__(self, name: str, surname: str, birth_date: str, ore_lavorate: int, ore_lezione :int) -> None:
        super().__init__(name, surname, birth_date, ore_lavorate)
        self.ore_lezione :int = ore_lezione