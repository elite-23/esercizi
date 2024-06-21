"""### Creazione di Test Case con UnitTest

Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi 
Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, 
i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.

Istruzioni
Creare un nuovo file Python denominato "test_persona.py".
Importare il modulo unittest e tutte le classi definite.

Test della Classe Persona
- Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi first_name, last_name e age.
  - Il funzionamento dei metodi setName, setLastName e setAge.

Test della Classe Dottore
- Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Dottore.
  - Il funzionamento del metodo isValidDoctor con diverse età.

Test della Classe Paziente
- Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Paziente.

Test della Classe Fattura
- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
- Scrivere test per verificare:
  - L'inizializzazione corretta della classe Fattura.
  - Il calcolo corretto del salario e del numero di fatture.
  - L'aggiunta e la rimozione di pazienti dalla lista.
"""

import unittest
from unittest import TestCase
from classes import persona,dottore,paziente,fattura

class TestStudiomedico(TestCase):
    def lol():
        pass
    

    
if __name__ == "__main__":
    unittest.main()