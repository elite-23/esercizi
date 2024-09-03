"""
Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.
"""

class Prodotto:
    def __init__(self, n :str, q :int) -> None:
        self.nome :str=n
        self.quantita :int=q


class Magazzino:
    def __init__(self) -> None:
        self.prodotti :list[Prodotto]=[]


    def aggiungi_prodotto(self, prodotto: Prodotto): 
        #aggiunge un prodotto al magazzino.
        self.prodotti.append(prodotto)

    def cerca_prodotto(self, nome: str) -> Prodotto: 
        #cerca un prodotto per nome e lo ritorna se esiste.
        for i in range(len(self.prodotti)):
            if nome==self.prodotti[i].nome:
                return self.prodotti[i]
        
    def verifica_disponibilità(self, nome: str) -> str: 
        p=self.cerca_prodotto(nome)
        if p:
            if p.quantita>0:
                return "Il prodotto è disponibile."
            elif p.quantita==0:
                return "Il prodotto è terminato"
        else:
            return "Il prodotto non è presente nel magazzino"
        
P1=Prodotto("Cesso",5)
P2=Prodotto("Bidet",0)
M1=Magazzino()
M1.aggiungi_prodotto(P1)
M1.aggiungi_prodotto(P2)
print(M1.verifica_disponibilità("Cesso"))
print(M1.verifica_disponibilità("Bide"))

