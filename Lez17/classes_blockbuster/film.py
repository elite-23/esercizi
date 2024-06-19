"""
### CLASSE: Film
In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. 
In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
"""

class Film:
    def init(self, id :int, title :str): 
        #metodo costruttore.
        self.id=id
        self.title=title


    def setID(self, id :int): 
        #che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
        self.id=id

    def setTitle(self, title :str): 
        #che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
        self.title=title

    def getID(self): 
        #che consente di ritornare il valore del codice identificativo di un film.
        return self.id

    def getTitle(self): 
        #che consente di ritornare il valore del titolo di un film.
        return self.title

    def isEqual(self, otherFilm): 
        #che ritorna true se il codice identificativo di due film è uguale.  
        if self.id  == otherFilm.id:
            return True
        else:
            return False
