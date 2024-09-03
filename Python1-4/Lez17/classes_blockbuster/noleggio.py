"""
### CLASSE: Noleggio
In un file "noleggio.py", creare una classe Noleggio.
Questa classe deve avere come attributi una lista di film contenuti in negozio (film_list), 
un dizionario (rented_film) che ha come chiave un numero intero rappresentante l'id del cliente che ha affittato il film e per valore una lista contenente 
i film affittati dal cliente.
 
- Definire i seguenti metodi:

    init(film_list): tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.
    
    isAvaible(film): tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario. 
        Se il film è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!". 
        Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!".
    
    rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare 
        ed il codice id del cliente che lo noleggia. Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. 
        Pertanto, il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile, 
        rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
            la chiave sarà l'id del cliente che noleggia (id_client)
            il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
        Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere aggiunto 
        alla lista dei film noleggiati dal cliente dato.  Se il cliente ha potuto noleggiare il film richiesto, stampare: 
            "Il cliente {clientId} ha noleggiato {titolo_film}!". 
        Se, invece, il film richiesto non è disponibile pe il noleggio, stampare: 
            "Non è possibile nolegiare il film {titolo_film}!".
    
    giveBack(film, clientID, days): questo metodo consente di restituire un film noleggiato in negozio, 
        ed ha come argomenti il film da restituire, il codice ID del client che restituisce il film, 
        il numero dei giorni in cui il cliente ha tenuto il film per se.  Il film da restituire deve essere rimosso dalla 
        lista dei film noleggiati dal cliente con id clientID, e tale film, deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). 
        Successivamente, il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. 
        Stampare la penale che il cliente deve pagare: 
            "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".
    
    printMovies(): stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: 
        "{titolo_film} - {genere_film} -"
    
    printRentMovies(clientID): questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.
"""
from movie_genre import Azione,Commedia,Drama

class Noleggio:
    def __init__(self, film_list :list[:Azione|Commedia|Drama]): 
        #tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.
        self.film_list :list[:Azione|Commedia|Drama]=film_list
        self.rented_film :dict[int,list[:Azione|Commedia|Drama]]={}


    def isAvaible(self, film :Azione|Commedia|Drama): 
        #tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario. 
        #Se il film è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!". 
        #Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!".
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return False
    
    def rentAMovie(self, film :Azione|Commedia|Drama, clientID :int): 
        #tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. 
        #Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto, il metodo deve verificare la disponibilità. 
        #Nel caso in cui il film richiesto sia disponibile, rimuoverlo dalla lista dei film disponibili in negozio, 
        #poi riempire il dizionario rented_film in questo modo:
            #la chiave sarà l'id del cliente che noleggia (id_client)
            #il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
        #Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere 
        #aggiunto alla lista dei film noleggiati dal cliente dato.  Se il cliente ha potuto noleggiare il film richiesto, stampare: 
            #"Il cliente {clientId} ha noleggiato {titolo_film}!". 
        #Se, invece, il film richiesto non è disponibile pe il noleggio, stampare: 
            #"Non è possibile nolegiare il film {titolo_film}!".
        if self.isAvaible(film):
            self.film_list.remove(film)
    
            if clientID not in self.rented_film.keys():
                self.rented_film[clientID]=[]        
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")


    
    def giveBack(self, film :Azione|Commedia|Drama, clientID :int, days :int): 
        #questo metodo consente di restituire un film noleggiato in negozio, ed ha come argomenti il film da restituire, 
        #il codice ID del client che restituisce il film, il numero dei giorni in cui il cliente ha tenuto il film per se.  
        #Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, 
        #deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). Successivamente, 
        #il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. 
        #Stampare la penale che il cliente deve pagare: 
            #"Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".
        if film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            tot=film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} e' di {tot} euro!")
        else:
            print(f"Il cliente {clientID} non ha noleggiato quel film")
    
    def printMovies(self): 
        #stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: "{titolo_film} - {genere_film} -"
        print("I film disponibili sono:")
        for i in self.film_list:
            print(f"\t{i.title} - {i.genere} -")
    
    def printRentMovies(self, clientID :int): 
        #questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.
        
        if clientID in self.rented_film.keys() and len(self.rented_film[clientID])>0:
            print(f"I film noleggiati dal cliente {clientID} sono:")
            for i in self.rented_film[clientID]:
                print(f"\t{i.title} - {i.genere} -")
        else:
            print(f"Il cliente {clientID} non ha noleggiato nessun film.")
