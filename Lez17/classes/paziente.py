"""
### CLASSE: Paziente
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
    getidCode(): consente di ritornare il codice identificativo del paziente.
    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
"""
from persona import Persona

class Paziente (Persona):
    
    def __init__(self, first_name: str, last_name: str, idCode :str):
        super().__init__(first_name, last_name)
        
        if isinstance(id,str):
            self.idCode :str=idCode
        else:
            self.idCode=None
            print("L'id inserito non è una stringa!")

    def setIdCode(self, idCode :str): 
        #consente di impostare il codice identificativo del paziente.
        if isinstance(id,str):
            self.idCode :str=idCode
        else:
            self.idCode=None
            print("L'id inserito non è una stringa!")
    
    def getidCode(self): 
        #consente di ritornare il codice identificativo del paziente.
        return self.idCode
    
    def patientInfo(self): 
        #stampa in output le informazioni del paziente in questo modo:
            #"Paziente: {nome} {cognome}
            #ID: {codice identificativo}"
        print(f"Paziente: {self.first_name} {self.last_name}\nID: {self.idCode}")
