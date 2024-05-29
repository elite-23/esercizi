from abc import ABC, abstractmethod

class abcAnimal (ABC):

    @abstractmethod
    def verso(self):
        pass

class Cane (abcAnimal):
    def __init__(self, name :str) -> None:
        super().__init__()
        self.name=name


    def verso (self):
        return print("BAU")
    

class Gatto(abcAnimal):
    def __init__(self,name :str) -> None:
        super().__init__()
        self.name=name
        

    def verso (self):
        return print("MIAO")
        
Cane("pippo").verso()
Gatto("Fulmine").verso()