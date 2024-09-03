"""Esercizio: Sistema di Gestione delle Prenotazioni Aeree
Completion requirements
Si vuole progettare un sistema in Python per la gestione delle prenotazioni aeree. 
Il sistema dovrà gestire diverse tipologie di voli, tra cui voli commerciali e voli charter.
 
Classe astratta Volo:
Tale classe sarà utilizzata per definire nel suo costruttore le funzionalità base di ogni tipo di volo, 
come il codice del volo (stringa) e la capacità massima di posti disponibili sul volo (numero intero) che sono attributi passati come argomenti in input. 
Inoltre, la classe deve avere un attributo chiamato prenotazioni, il quale non deve essere passato come argomento del costruttore; 
il costruttore, però, deve assegnare valore iniziale pari a 0 a tale attributo.
 
Metodi:

    si definisca il metodo astratto prenota_posto().
    si definisca il metodo astratto posti_disponibili().

Classe VoloCommerciale:
Estende la classe Volo e definisce gli attributi codice del volo e capacità massima di posti disponibili sul volo. 
Il costruttore deve inoltre gestire i seguenti attributi interi: posti_economica, posti_business, e posti_prima; 
i quali consentono di stabilire quanti posti sono stati riservati alla classe economica, quanti alla classe business e quanti alla prima classe su ogni volo. 
Il costruttore non deve ricevere in input questi argomenti, ma assegnare loro un valore iniziale tale 
che la somma di questi tre valori interi sia uguale al numero dei posti disponibili sul volo. 
Si può pensare di riservare il 70% dei posti alla classe economica, il 20% dei posti alla classe business ed i restanti posti alla prima classe. 
Inoltre, il costruttore deve creare tre valori interi pari a 0, chiamati prenotazioni_economica, prenotazioni_business, prenotazioni_prima.
 
Metodi:

    prenota_posto(posti, classe_servizio): che consente di prenotare un certo numero di posti sul volo in una determinata classe. 
    Tale metodo, prima di riservare un posto, deve controllare prima che ci siano posti disponibili sull'intero volo, 
    poi se ci sono posti disponibili nella classe richiesta. In caso affermativo, contare il numero dei posti prenotati in tale classe. 
    Inoltre, nel caso in cui sia possibile prenotare un posto, il metodo deve stampare a schermo un messaggio che notifichi all'utente 
    di aver riservato un tot di posti per una determinata classe su un dato volo (specificando il codice del volo). 
    In caso contrario, stampare a schermo un messaggio che notifichi all'utente che non ci sono più posti disponibili nella classe scelta. 
    Se sul volo non ci sono più posti disponibili, il metodo deve stampare a schermo un messaggio notificando all'utente che il volo è al completo. 
    Inoltre, se la classe passata come input del metodo non risulta essere una delle seguenti classi ("economica", "business", "prima"), 
    il metodo deve stamapre a schermo un messaggio di errore, notificando all'utente che la classe richiesta non è valida. 
    Infine, il metodo deve aggiornare l'attributo prenotazioni della classe estesa Volo, sommando il numero di prenotazioni ricevute per ogni classe di servizio, 
    poi aggiornare gli attributi prenotazioni_economica, prenotazioni_business, prenotazioni_prima con l'esatto numero delle prenotaioni ricevute 
    per ogni classe di servizio. Suggerimento: introdurre delle variabili locali d'appoggio per gestire le prenotazioni per ogni classe di servizio 
    da azzerare all'inizio di ogni fase di prenotazione.

    posti_disponibili(): che ritorna un dizionario in cui vengono salvati il numero di posti disponibili totali sul volo nel seguente modo: 
    il dizionario deve avere quattro chiavi, ovvero, 'posti disponibili', 'classe economica', 'classe business', 'prima classe'. 
    Alla chiave 'posti disponibili' associare come rispettivo valore il numero di posti disponibili rimasti sul volo, 
    alla chiave 'classe economica' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella classe economica, 
    alla chiave 'classe business' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella classe business, 
    alla chiave 'prima classe' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella prima classe. 
    Se i posti disponibili sia sul volo, sia su una specifica classe di servizio sono esauriti, il valore da associare alla corrispondete chiave è 0.

Classe VoloCharter:
Estende la classe Volo e e definisce gli attributi codice del volo e capacità massima di posti disponibili sul volo. 
Il costruttore deve inoltre gestire il costo del volo (numero float) per il charter. 
Un volo charter è un volo di cui tutti i posti disponibili vengono acquistati tutti insieme in una sola volta da un tour operator ad un certo prezzo.
 
Metodi:

    prenota_posto(): questo metodo verifica che se l'aereo è vuoto, ovvero i posti disponibili sono pari alla capacità massima di posti. 
    In quel caso, è possibile prenotare un numero di posti pari alla capacità massima di posti supportata dal volo. 
    Nel caso in cui la prenotazione charter andasse a buon fine, il metodo deve stampare a schermo un messaggio in cui avvisa il tour operator che i
    l volo charter (specificandone il codice del volo) è stato prenotato completamente, mostrando anche il prezzo pagato. 
    In caso contrario, il metodo deve mostrare un messaggio a schermo in cui avvisa l'utente che il volo charter è gia prenotato.

    posti_disponibili(): che ritorna il numero di posti disponibili totali sul volo.

Classe CompagniaAerea:
Questa classe deve avere un costruttore che richiede come argomento in input solo il nome della compagnia (stringa) 
ed il prezzo standard di un biglietto (numero float), e creare una lista vuota chiamata flotta. 
La classe CompagniaAerea deve gestire molteplici voli commerciali, attraverso i seguenti metodi:

    aggiungi_volo(volo_commericiale): il volo_commerciale deve essere aggiunto alla flotta della compagnia aerea.
    rimuovi_volo(volo_commericiale): il volo_commerciale deve essere rimosso dalla flotta della compagnia aerea.
    mostra_flotta(): tale metodo deve stampare a schermo tutti i voli che fanno parte della flotta della compagnia aerea, specificando il codice di ogni volo.
    guadagno(): questo metodo deve calcolare e ritornare (come float arrotondato alle prime due cifre decimali) 
        il gadagno ricavato dalla vendita dei biglietti aerei dei voli nella sua flotta. Su ogni aereo della flotta, il prezzo  
        per un posto in classe economica è pari a prezzo standard, il prezzo per un posto in classe business è pari al doppio del prezzo standard, 
        mentre il prezzo per un posto in prima classe vale tre volte il prezzo standard.
"""
from abc import ABC,abstractmethod

class Volo(ABC):
    def __init__(self, codice_volo :int, max_posti :int) -> None:
        self.prenotazioni :int=0
        self.codice_volo :int=codice_volo
        self.max_posti :int=max_posti

    @abstractmethod
    def prenota_posto():
        pass

    @abstractmethod
    def posti_disponibili():
        pass


class VoloCommerciale(Volo):
    def __init__(self, codice_volo: int, max_posti: int) -> None:
        super().__init__(codice_volo, max_posti)
        self.posti_economica :int= round(max_posti*0.70,0)
        self.posti_business :int= round(max_posti*0.20,0)
        self.posti_prima :int=round(max_posti*0.10,0)
        self.prenotazioni_economica:int = 0
        self.prenotazioni_business:int = 0
        self.prenotazioni_prima:int = 0

    def posti_disponibili(self):
        posti={"posti disponibili":self.max_posti-self.prenotazioni, "economica":self.posti_economica-self.prenotazioni_economica, 
               "business":self.posti_business-self.prenotazioni_business, "prima":self.posti_prima-self.prenotazioni_prima}
        return posti

    def prenota_posto(self, posti:int,classe_servizio:int):
        p=self.posti_disponibili()
        if posti<=p["posti disponibili"]:
            if classe_servizio in p.keys():
                if posti<=p[classe_servizio]:
                    print(f"{posti} posti prenotati nella classe:{classe_servizio}\n per il volo:{self.codice_volo}")
                    self.prenotazioni+=posti
                    if classe_servizio=="business":self.prenotazioni_business+=posti
                    if classe_servizio=="econimca":self.prenotazioni_economica+=posti
                    if classe_servizio=="prima":self.prenotazioni_prima+=posti
                else:
                    print(f"Posti per la classe selezionata:{classe_servizio} sono finiti")
            else:
                print("ERROR la classe specificata non è valida")
        else:
            print("Posti sul volo terminati")

class VoloCharter(Volo):
    def __init__(self, codice_volo: int, max_posti: int, prezzo:int) -> None:
        super().__init__(codice_volo, max_posti)
        self.prezzo :int=prezzo

    def posti_disponibili(self): 
        return self.max_posti-self.prenotazioni

    def prenota_posto(self):
        p=self.posti_disponibili()
        if p == self.max_posti:
            print(f"Tutti i posti del volo charter:{self.codice_volo}\n prenotati per il prezzo di:{self.prezzo}")
            self.prenotazioni=self.max_posti
        else:
            print("Il volo è già stato prenotato")
        

class CompagniaAerea:
    def __init__(self,nome:str, prezzo:int) -> None:
        self.nome=nome
        self.prezzo=prezzo
        self.flotta :list[VoloCommerciale]=[]


    def  aggiungi_volo(self,volo_commericiale :VoloCommerciale): 
        self.flotta.append(volo_commericiale)

    def rimuovi_volo(self,volo_commericiale :VoloCommerciale): 
        #il volo_commerciale deve essere rimosso dalla flotta della compagnia aerea.
        self.flotta.remove(volo_commericiale)

    def mostra_flotta(self):
        #tale metodo deve stampare a schermo tutti i voli che fanno parte della flotta della compagnia aerea, specificando il codice di ogni volo.
        print(f"La flotta della compagnia {self.nome}:")
        for i in self.flotta:
            print(f"Volo:{i.codice_volo}")

    def guadagno(self): 
        #questo metodo deve calcolare e ritornare (come float arrotondato alle prime due cifre decimali) 
        #il gadagno ricavato dalla vendita dei biglietti aerei dei voli nella sua flotta. Su ogni aereo della flotta, 
        #il prezzo  per un posto in classe economica è pari a prezzo standard, il prezzo per un posto in classe business 
        #è pari al doppio del prezzo standard, mentre il prezzo per un posto in prima classe vale tre volte il prezzo standard.
        guad=0
        for i in self.flotta:
            guad+=self.prezzo*i.posti_economica
            guad+=2*self.prezzo*i.posti_business
            guad+=3*self.prezzo*i.posti_prima
            