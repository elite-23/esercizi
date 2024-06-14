"""
### CLASSE: Persona

Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. Tale classe deve avere due attributi privati di tipo String, 
uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.
- La classe Persona deve avere i seguenti metodi:

    init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, impostare a None l'attributo 
        che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". Se first_name e last_name 
        sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; se first_name e last_name non sono due stringhe, allora assegnare None all'età.
    setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. Il valore viene modificato 
        se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
    setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. Il valore viene modificato 
        se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".
    setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se 
        viene passato al metodo un numero intero. In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
    getName(): consente di ritornare il nome di una persona.
    getLastname(): consente di ritornare il cognome di una persona.
    getAge(): consente di ritornare l'età di una persona.
    greet(): stampa il seguente saluto "Ciao, sono nome cognome! Ho età anni!"
"""

class Persona:

    def __init__(self, first_name:str , last_name:str):
        # Tale metodo, deve verificare che first_name, last_name siano stringhe; 
        # in caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, 
        # "Il nome inserito non è una stringa!". Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; 
        # se first_name e last_name non sono due stringhe, allora assegnare None all'età.
        if isinstance(first_name,str) and isinstance(last_name,str):
            self.first_name :str=first_name
            self.last_name :str=last_name
            self.age :int=0
        else:
            self.first_name :str=None
            self.last_name :str=None
            self.age :int=None
            print("Il nome inserito non è una stringa!")


    def setName(self, first_name): 
        #consente di impostare il nome di una persona, modificando il valore del relativo attributo. 
        # Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, 
        # ad esempio "Il nome inserito non è una stringa!".
        if isinstance(first_name,str):
            self.first_name :str=first_name
        else:
            print("Il nome inserito non è una stringa!")
    
    
    def setLastName(self, last_name): 
        #consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
        # Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, 
        # stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".
        if isinstance(last_name,str):
            self.last_name :str=last_name
        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self, age): 
        #consente di impostare l'età di una persona, modificando il valore del relativo attributo. 
        # Il valore viene modificato se e solo se viene passato al metodo un numero intero. 
        # In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
        if isinstance(age,str):
            self.age :str=age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self): 
        #consente di ritornare il nome di una persona.
        return self.first_name
    

    def getLastname(self): 
        #consente di ritornare il cognome di una persona.
        return self.last_name

    def getAge(self): 
        #consente di ritornare l'età di una persona.
        return self.age

    def greet(self): 
        #stampa il seguente saluto "Ciao, sono nome cognome! Ho età anni!"
        print(f"Ciao sono{self.first_name} {self.last_name}! Ho età {self.age}")

