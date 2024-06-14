"""
### CLASSE: Fattura
Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:

    init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, 
        richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, 
        mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un 
        messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
    getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
    getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
    addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, 
        richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
    removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente 
        da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). 
        Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
"""
from paziente import Paziente
from dottore import Dottore
class Fattura:

    def init(self, patient :list[Paziente], doctor :Dottore): 
        #deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, 
        #richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, 
        #mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un 
        #messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
        if isinstance(patient, list[Paziente]):
            if isinstance(doctor, Dottore):
                if doctor.isAValidDoctor():
                    self.fatture :int=len(patient)
                    self.salary :int=0
                    self.doctor :Dottore=doctor
                    self.patient :list[Paziente]=patient
                else:
                    self.fatture=None
                    self.salary=None
                    self.doctor=None
                    self.patient=None
                    print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
            else:
                self.fatture=None
                self.salary=None
                self.doctor=None
                self.patient=None
                print("Il dottore deve essere di tipo Doctor.")
        else:
            self.fatture=None
            self.salary=None
            self.doctor=None
            self.patient=None
            print("Patient deve essere una lista di oggetti di tipo Pazienti.")
        
    
    def getSalary(self): 
        #deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
        self.salary=self.doctor.getParcel()*len(self.patient)
        return self.salary
    
    def getFatture(self):
        #deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
        self.fatture :int=len(self.patient)
        return self.fatture
    
    def addPatient(self, newPatient :Paziente): 
        #consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, 
        #richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
        if isinstance(newPatient, Paziente):
            self.patient.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor cognome è stato aggiunto il paziente {newPatient.idCode}")
        else:
            print("Il nuovo paziente deve essere di tipo Paziente")

    def removePatient(self, idCode :str): 
        #consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente 
        #da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). 
        #Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
        if isinstance(idCode,str):
            for i in self.patient:
                if i.getidCode() == idCode:
                    self.patient.remove(i)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor cognome è stato rimosso il paziente {idCode}")
                    break
        else:
            print("L'id del paziente da rimuovere deve essere una stringa.")
