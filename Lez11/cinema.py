"""
Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""

class Film:
    def __init__(self, title :str, length :int) -> None:
        self.title :str =title
        self.length: int =length


class Sala:
    def __init__(self, num_sala :int, seats :int, film :Film) -> None:
        self.n :int =num_sala
        self.seats :int =seats
        self.taken :int =0
        self.film :Film =film
    

    def prenota_posti(self, num_posti :int): 
        #Prenota un certo numero di posti nella sala, se disponibili. 
        #Restituisce un messaggio di conferma o di errore.
        if num_posti<=self.seats-self.taken:
            self.taken+=num_posti
            print("I posti sono stati prenotati con successo!")
        else:
            print("Purtroppo non sono disponibili abbastanza posti per eseguire la prenotazione.")
        
    
    def posti_disponibili(self): 
        #Restituisce il numero di posti ancora disponibili nella sala.
        return self.seats-self.taken



class Cinema:
    def __init__(self) -> None:
        self.sale:list[Sala]=[]


    def aggiungi_sala(self, sala :Sala): 
        #Aggiunge una nuova sala al cinema.
        self.sale.append(sala)
    
    def prenota_film(self, titolo_film :str, num_posti :int): 
        #Trova il film desiderato e tenta di prenotare posti. 
        #Restituisce un messaggio di stato.
        for i in range(len(self.sale)):
            if titolo_film == self.sale[i].film.title:
                print("Il film è stato trovato, controllando disponibilità posti...")
                self.sale[i].prenota_posti(num_posti)
                return
        print("Il film non è presente in nessuna sala mi dispiace")

F1=Film("LOLLO",120)
S1=Sala(1,23,F1)
C=Cinema()
C.aggiungi_sala(S1)
C.prenota_film("LOLLO",24)
            

