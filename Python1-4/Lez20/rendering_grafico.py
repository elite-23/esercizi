"""2. RENDERING GRAFICO
Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. 
Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le funzionalità base di ogni forma, 
come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.

Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel costruttore. 
Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del trinagolo 
(per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stamapre su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore. 
Il traingolo da stampare deve essere un traingolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni chiamata a print, 
e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

Esempi di output:
Ecco un Quadrato di lato 4!

* * * *
*     *
*     *
* * * *
L'area di questo quadrato vale: 16

Ecco un Rettangolo avente base 8 ed altezza 4!
* * * * * * * *
*             *
*             *
* * * * * * * *
L'area di questo rettangolo vale: 32

Ecco un Triangolo avente base 4 ed altezza 4!
*      
* *    
*   *  
* * * *
L'area di questo triangolo vale: 8.0
"""
from abc import ABC, abstractmethod

class Forma(ABC):
    
    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def render(self):
        pass


class Quadrato(Forma):
    def __init__(self, lato :int) -> None:
        self.lato :int=lato

    def getArea(self):
        return self.lato**2
    
    def render(self):
        print(f"Ecco un Quadrato di lato {self.lato}!")
        for i in range(self.lato):
            if i==0 or i==self.lato-1:
                s="* "*(self.lato-1)
                s+="*"
                print(s)
            else:
                s="* "
                s+="  "*(self.lato-2)
                s+="*"
                print(s)
        print(f"L'area di questo quadrato vale: {self.getArea()}")
        print("")


class Rettangolo(Forma):
    def __init__(self, base :int, altezza :int) -> None:
        self.base :int=base
        self.altezza :int=altezza


    def getArea(self):
        return self.base*self.altezza
    
    def render(self):
        print(f"Ecco un Rettangolo avente base {self.base} ed altezza {self.altezza}!")
        for i in range(self.altezza):
            if i==0 or i==self.altezza-1:
                s="* "*(self.base-1)
                s+="*"
                print(s)
            else:
                s="* "
                s+="  "*(self.base-2)
                s+="*"
                print(s)
        print(f"L'area di questo rettangolo vale: {self.getArea()}")
        print("")


class TriangoloRettangolo(Forma):
    def __init__(self, cateto :int) -> None:
        self.cateto :int=cateto
    
    
    def getArea(self):
        return self.cateto*self.cateto / 2
    
    def render(self):
        print(f"Ecco un Triangolo avente base {self.cateto} ed altezza {self.cateto}!")
        for i in range(self.cateto):
            if i==0:
                print("*")
            elif i==self.cateto-1:
                s="* "*(self.cateto-1)
                s+="*"
                print(s)
                
            else:
                s="* "
                s+="  "*(i-1)
                s+="*"
                print(s)
        print(f"L'area di questo triangolo vale: {self.getArea()}")
        print("")


t=TriangoloRettangolo(3)
t.render()

q=Quadrato(5)
q.render()

r=Rettangolo(5,3)
r.render()