"""
### CLASSI GENERE
Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. 
Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, che equivale al genere di film (genere="Azione", nella classe Azione) 
ed un attributo privato di tipo float chiamato penale. I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, 
i film drammatici hanno una penale di 2 euro al giorno.

- Per ognuna di queste classi si implementi un metodo chiamato:

    getGenere(), che ritorna il genere di film
    getPenale(), che ritorna il valore della penale
    calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.

Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py".
"""
from film import Film

class Azione(Film):
    def __init__(self, id :int, title :str) -> None:
        super().__init__(id, title)
        self.genere :str="Azione"
        self.penale :float=3.0

    def getGenere(self) -> str:
        #che ritorna il genere di film
        return self.genere
    
    def getPenale(self) ->float: 
        #che ritorna il valore della penale
        return self.penale
    
    def calcolaPenaleRitardo(self,ritardo :int) -> float: 
        #che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.
        return self.penale*ritardo

class Commedia(Film):
    def __init__(self, id :int, title:str) -> None:
        super().__init__(id, title)
        self.genere :str="Commedia"
        self.penale :float=2.50

    def getGenere(self) -> str:
        #che ritorna il genere di film
        return self.genere
    
    def getPenale(self) ->float: 
        #che ritorna il valore della penale
        return self.penale
    
    def calcolaPenaleRitardo(self,ritardo :int) -> float: 
        #che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.
        return self.penale*ritardo

class Drama(Film):
    def __init__(self, id :int, title :str) -> None:
        super().__init__(id, title)
        self.genere :str="Drama"
        self.penale :float=2.0

    def getGenere(self) -> str:
        #che ritorna il genere di film
        return self.genere
    
    def getPenale(self) ->float: 
        #che ritorna il valore della penale
        return self.penale
    
    def calcolaPenaleRitardo(self,ritardo :int) -> float: 
        #che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.
        return self.penale*ritardo
