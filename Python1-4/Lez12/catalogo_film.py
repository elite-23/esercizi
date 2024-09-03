"""
Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. 
Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
    Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
    Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene 
    la parola cercata nel titolo.
"""
class MovieCatalog():
    def __init__(self) -> None:
        self.directors:dict[str,list] ={}

    def add_movie(self, director_name :str, movies :list):
        if director_name in self.directors.keys():
            self.directors[director_name].append(movies)
        else:
            self.directors[director_name]=movies

    def remove_movie(self, director_name :str, movie_name :str):
        if movie_name in self.directors[director_name]:
            self.directors[director_name].remove(movie_name)
            if len(self.directors[director_name])==0:
                self.directors.pop(director_name)


    def list_directors(self):
        print("The directors in the catalog are:")
        for i in self.directors.keys():
            print(f"\t{i}")


    def get_movies_by_directors(self, director_name :str):
        return self.directors[director_name]

    def search_movies_by_title(self, title :str):
        for i,j in self.directors.items():
            print(f"I film nel nostro catalogo con il titolo {title} sono:")
            if title in j:
                print(f"\tDel regista {i} sono:")
                for y in j:
                    if y == title:
                        print(f"\t\t{y}")
                    