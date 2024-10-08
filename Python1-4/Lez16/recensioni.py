"""
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. 
Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. 
Esempio di riassunto:

Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
"""

class Media:
    def __init__(self) -> None:
        pass

    def set_title(self, title): 
        #Imposta il titolo del media.
        pass

    def get_title(self):
        #Restituisce il titolo del media.
        pass

    def aggiungiValutazione(self, voto):
        #Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
        pass

    def getMedia(self):
        #Calcola e restituisce la media delle valutazioni.
        pass

    def getRate(self):
        #Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
        pass

    def ratePercentage(self, voto):
        #Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
        pass

    def recensione(self):
        #Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. 
        pass
    
class Film (Media):
    def __init__(self) -> None:
        super().__init__()
    
    def set_title(self, title):
        return super().set_title(title)
    
    def get_title(self):
        return super().get_title()
    
    def aggiungiValutazione(self, voto):
        return super().aggiungiValutazione(voto)
    
    def getMedia(self):
        return super().getMedia()
    
    def getRate(self):
        return super().getRate()
    
    def ratePercentage(self, voto):
        return super().ratePercentage(voto)
    
    def recensione(self):
        return super().recensione()
    
    