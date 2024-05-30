"""
Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
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
    
    
    def add_book(self,book_id: str, title: str, author: str):
        if book_id not in self.books.keys():
            book=Book(book_id, title, author)
            self.books[book_id]=book
        else:
            print("Book already present")
    
    def borrow_book(self, book_id: str):
        if book_id in self.books.keys():
            self.books[book_id].borrow_book(self.books[book_id])
        else:
            print("Book not found")
        
    
    def return_book(self,member_id: str, book_id: str):
        if member_id in self.members.keys():
            self.members[member_id].return_book(self.books[book_id])
    
    def get_borrowed_books(self,member_id):
        list=[]
        for i in self.members[member_id].borrowed_books:
            list.append(i.title)
        return list
    
    
    