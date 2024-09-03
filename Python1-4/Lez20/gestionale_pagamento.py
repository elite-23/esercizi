"""
1. GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano 
appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando 
il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, ad esempio: 
"Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il 
metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote 
da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 
0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. 
Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si 
invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321
"""

class Pagamento:
    def __init__(self) -> None:
        pass

    def setImporto(self, importo :float):
        self.importo :float=importo

    def getImporto(self):
        return self.importo

    def dettagliPagamento(self):
        #che visualizza una frase che descrive l'importo del pagamento, ad esempio: 
        #"Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali
        x="%.2f" % self.getImporto()
        print(f"Importo del pagamento: {x}")
        

class PagamentoContanti(Pagamento):
    def __init__(self, importo :float) -> None:
        super().__init__()
        self.setImporto(importo)
        self.banconote=[500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        

    def inPezziDa(self):
        x=self.importo
        i=0
        usati={}
        while x>0:

            if x>=self.banconote[i]:

                if self.banconote[i] in usati.keys():  
                    usati[self.banconote[i]]+=1
                    x=round(x-self.banconote[i],2)
                else:
                    usati[self.banconote[i]]=1
                    x=round(x-self.banconote[i],2)
            else:
                i+=1
        
        x="%.2f" % self.getImporto()
        print(f"{x} euro da pagare in contanti con:")

        for i,j in usati.items():
            print(f"{j} banconota da {i} euro")
        print("")
       
    def dettagliPagamento(self):
        x="%.2f" % self.getImporto()
        print(f"Importo in contanti di: {x}")
        self.inPezziDa()

    
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo: float, nome_titolare :str, data_scad :str, num_carta :int) -> None:
        super().__init__()
        self.setImporto(importo)
        self.nome_titolare=nome_titolare
        self.data_scad=data_scad
        self.num_carta=num_carta


    def dettagliPagamento(self):
        x="%.2f" % self.getImporto()
        print(f"Pagamento di: {x} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome_titolare}")
        print(f"Data di scadenza: {self.data_scad}")
        print(f"Numero della carta: {self.num_carta}")
        print("")

cont=PagamentoContanti(96.43)
cont.dettagliPagamento()

card=PagamentoCartaDiCredito(90, "Lillo", "09/24", 13323124242)
card.dettagliPagamento()
