"""
Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri 
sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
"""


class Book:
    def __init__(self, title :str, author :str):
        self.title :str =title
        self.author :str =author
        self.is_borrowed :bool =False

    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
    
    def return_book(self):
        self.is_borrowed=False
    

class Library:
    def __init__(self):
        self.books :dict[str,Book] ={}
        self.borrowed_books=[]
    
    
    def add_book(self, title: str, author: str):
        if title not in self.books.keys():
            book=Book( title, author)
            self.books[title]=book
        else:
            print("Book already present")
    
    def borrow_book(self, title: str):
        if title in self.books.keys():
            self.books[title].borrow(self.books[title])
            self.borrowed_books.append(self.books[title])
        else:
            print("Book not found")
        
    
    def return_book(self, title: str):
        if title in self.books.keys():
            self.books[title].return_book()
            self.borrowed_books.remove(self.books[title])

    def mostra_libri_disponibili(self):
        if len(self.books)-len(self.borrowed_books)!=0:
            print(list(self.books.values()).remove(i for i in self.borrowed_books))
        else:
            print("Sto cazzoooooooo niente libri disponibili.")
    