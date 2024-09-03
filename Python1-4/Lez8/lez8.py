class animal ():
    def __init__(self, specie: str, age :int) -> None:
        self.specie :str=specie
        self.age :int=age
    
    def __str__(self) -> str:
        return f"Animal (specie={self.specie}, age={self.age})"

class person(animal):
    def __init__(self, specie :str, age :int, name :str, surname :str, codice_fiscale :str) -> None:
        super().__init__(specie, age)
        self.name :str=name
        self.surname :str=surname
        self.codice_fiscale :str=codice_fiscale

    def __str__(self) -> str:
        return f"Person (specie={self.specie}, age={self.age}, name={self.name}, surname={self.surname}, codice_fiscale={self.codice_fiscale})"

class cat(animal):
    def __init__(self, specie :str, age :int, name :str) -> None:
        super().__init__(specie, age)
        self.name :str=name

    def __str__(self) -> str:
        return f"Cat (specie={self.specie}, age={self.age}, name={self.name})"

class rabbit(animal):
    def __init__(self, specie :str, age :int, name :str) -> None:
        super().__init__(specie, age)
        self.name :str=name

    def __str__(self) -> str:
        return f"Rabbit (specie={self.specie}, age={self.age}, name={self.name})"

class student(person):
    def __init__(self, specie:str, age :int, name:str, surname :str, codice_fiscale :str, matricola:str) -> None:
        super().__init__(specie, age, name, surname, codice_fiscale)
        self.matricola :str=matricola

    def __str__(self) -> str:
        return f"Student (specie={self.specie}, age={self.age}, name={self.name}, surname={self.surname}, codice_fiscale={self.codice_fiscale}, matricola={self.matricola})"