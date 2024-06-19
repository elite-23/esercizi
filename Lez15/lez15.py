"""
Esercizio 1

Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')
"""

class FileManeger:
    def __init__(self, filePath, mode) -> None:
        self.open=open(filePath, mode)
        print("Resource acquired")

    
    def __enter__(self):
        return self.open

    def __exit__(self, exc_type, exc_value, traceback):
        
        print("Resource released")

        if exc_type is not None:
            print(f"Exception type is: {exc_type}")
            print(f"Exception value is: {exc_value}")
            print(f"Traceback is: {traceback}")
        
        return True



"""
Esercizio 2

Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1
"""
import time
class Timer():
    
    def __enter__(self):
        self.start = time.time()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.start=time.time()-self.start
        print(f"The code took {self.start} seconds to execute.")
        
        if exc_type is not None:
            print(f"Exception type is: {exc_type}")
            print(f"Exception value is: {exc_value}")
            print(f"Traceback is: {traceback}")
        
        return True


with Timer():

    time.sleep(1)
