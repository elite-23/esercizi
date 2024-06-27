from contextlib import contextmanager


class Analisi:

    @staticmethod
    def tempo(func):

        def wrapper(*args):
            import time

            start= time.time()

            value = func(*args)
            
            print(f"Time elapsed:{time.time()-start}")

            return value, time.time()- start
        
        return wrapper


@Analisi.tempo
def area_cerchio(raggio :float):

    return raggio *raggio * 3.14

area_cerchio(1)



def generator():
    yield "A"
    yield "B"
    yield "C"




