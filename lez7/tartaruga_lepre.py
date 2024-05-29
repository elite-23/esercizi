'''
In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento.
 I contendenti iniziano la gara dal quadrato #1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa.
   Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara.
     Durante la corsa, i contendenti possono occasionalmente perdere terreno. 
     C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.

- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). 
Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. 
Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. 
Usate una tecnica simile per muovere la lepre seguendo le sue regole.

Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'

Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, 
la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. 
In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. 
Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. 
Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". 
Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". 
Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.
 
SFIDE AGGIUNTIVE:
X1. Variabilità Ambientale:
Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. 
Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
Modificatori mossa:
- La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
- La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
 
X 2. Energia o Stamina:
Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. 
Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. L'energia inziale per entrambi gli animali è 100.

Nuove regole di movimento:
- Tartaruga:
    - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, essa guadagna 10 di energia. 
    Non può superare l'energia iniziale.
    - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
    - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

- Lepre:
    - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energia iniziale.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
    - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.
 
3. Ostacoli e Bonus
Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse, che influenzano direttamente il movimento degli animali quando vengono calpestati. 
li ostacoli causano uno slittamento all'indietro, mentre i bonus offrono un avanzamento extra.

Dettagli Implementativi:
- Ostacoli:
Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), gli ostacoli riducono la posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7). 
Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli sul percorso (chiave) ed i relativi effetti (valore). 
Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.

- Bonus:
Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), i bonus aumentano la posizione dell'animale di un numero determinato di quadrati (es: 5, 3, 10). 
I bonus sono rappresentati da un dizionario che mappa le posizioni dei bonus sul percorso (chiave) ed i relativi effetti (valore). 
Consentire agli animali di beneficiare pienamente dei bonus, ma non oltrepassare il traguardo.
'''
import random

class Tartaruga:
    def __init__ (self) -> None:
        self.stamina=100
        self.pos=0


    def Passoveloce(self, pioggia :int =0):
        if self.stamina>=5:
            self.stamina-=5
            if self.pos+3+pioggia>69:
                self.pos=69
            else:
                self.pos+=3+pioggia
        else:
            self.stamina+=10
        

    def Scivolata (self, pioggia :int =0):
        if self.pos-6+pioggia>=0 and self.stamina>=10:
            self.pos-=6+pioggia
            self.stamina-=10
        elif self.pos-6+pioggia<0 and self.stamina>=10:
            self.pos=0
            self.stamina-=10
        else:
            self.stamina+=10
        
    
    def Passolento(self, pioggia :int =0):
        if self.stamina>=3:
            self.stamina-=3
            self.pos+=1+pioggia
        else:
            self.stamina+=10

    def round(self, p :int):
        x=random.randint(1,10)
        if (p//10)%2==0:
            #print("SOleeeeee")
            if x<=5:
                self.Passoveloce()
            elif x<=7:
                self.Scivolata()
            elif x<=10:
                self.Passolento()
        else:
            #print("PIOGGIAAAAAAA")
            if x<=5:
                self.Passoveloce(-1)
            elif x<=7:
                self.Scivolata(-1)
            elif x<=10:
                self.Passolento(-1)


class Lepre:
    def __init__(self) -> None:
        self.stamina=100
        self.pos=0


    def Riposo (self): 
        if self.stamina+5<= 100:
            self.stamina+=5
        else:
            self.stamina=100
        
    
    def Grandebalzo (self, pioggia :int=0): 
        if self.stamina>=15:
            self.stamina-=15
            if self.pos+9+pioggia>69:
                self.pos=69
            else:
                self.pos+=9+pioggia
        else:
            self.stamina+=10
    
    def Grandescivolata (self, pioggia :int=0): 
        if self.pos-12+pioggia>=1 and self.stamina>=20:
            self.pos-=12+pioggia
            self.stamina-=20
        elif self.pos-12+pioggia<0 and self.stamina>=20:
            self.pos=0
            self.stamina-=20
        else:
            self.stamina+=10
    
    def Piccolobalzo (self, pioggia :int=0):
        if self.stamina>=5 and self.pos+1+pioggia>=0:
            self.stamina-=5
            self.pos+=1+pioggia
        elif self.stamina>=5 and self.pos+1+pioggia<0:
            self.pos=0
        else:
            self.stamina+=10
        
    
    def Piccolascivolata (self, pioggia :int=0): 
        if self.pos-2+pioggia>=0 and self.stamina>=8:
            self.pos-=2+pioggia
            self.stamina-=8
        elif self.pos-2+pioggia<0 and self.stamina>=8:
            self.pos=0
            self.stamina-=8
        else:
            self.stamina+=10

    def round(self, p :int):
        x=random.randint(1,10)
        if (p//10)%2==0 :
            if x<=2:
                self.Riposo()
            elif x<=4:
                self.Grandebalzo()
            elif x==5:
                self.Grandescivolata()
            elif x<=8:
                self.Piccolobalzo()
            elif x<=10:
                self.Piccolascivolata()
        else:
            if x<=2:
                self.Riposo()
            elif x<=4:
                self.Grandebalzo(-2)
            elif x==5:
                self.Grandescivolata(-2)
            elif x<=8:
                self.Piccolobalzo(-2)
            elif x<=10:
                self.Piccolascivolata(-2)


class Gara:
    def __init__(self) -> None:
        self.pioggia=-1
        self.bonus={2:3,4:3,8:5,16:3,32:7,64:4}
        self.ostacolo={10:-4,20:-2,30:-3,40:-6,50:-1,60:-5}
        self.percorso=["+" if i in self.bonus.keys()  else "-" for i in range(70)]
        for i in self.ostacolo.keys():
            self.percorso[i]="/"

            
    def start(self, T :Tartaruga, L :Lepre):
        print("BANG !!!!! AND THEY'RE OFF !!!!!")
        while self.percorso[-1]=="-":
            self.pioggia+=1
            self.percorso[T.pos]="-"
            self.percorso[L.pos]="-"
            
            T.round(self.pioggia)
            if T.pos in self.bonus.keys():
                #print("BONUSSSS - Tortoise")
                T.pos+=self.bonus[T.pos]
            elif T.pos in self.ostacolo.keys():
                #print("Obstacleee - Tortoise")
                T.pos+=self.ostacolo[T.pos]
            self.percorso[T.pos]="T"
            
            L.round(self.pioggia)
            if self.percorso[L.pos]=="T":
                self.percorso[L.pos]="OUCH!!!"
            else:
                if L.pos in self.bonus.keys():
                    #print("BONUSSSS - Hare")
                    L.pos+=self.bonus[L.pos]
                elif L.pos in self.ostacolo.keys():
                    #print("Obstacleee - Hare")
                    L.pos+=self.ostacolo[L.pos]
                self.percorso[L.pos]="H"
            print("".join(self.percorso))

        if self.percorso[-1]=="T":
            print("TORTOISE WINS! || VAY!!!")
        elif self.percorso[-1]=="H":
            print("HARE WINS || YUCH!!!") 
        else:
            print("IT'S A TIE.") 

g=Gara()
g.start(Tartaruga(),Lepre())