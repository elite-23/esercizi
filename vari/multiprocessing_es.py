from multiprocessing import Process
import time

def bubble_sort_V2():
    from random import randint

    x=[randint(0,1000) for _ in range(10000)]

    swap :bool=True
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j]>x[j+1]:
                swap=False
                y=x[j]
                x[j]=x[j+1]
                x[j+1]=y
        if swap:
            break


def sleep():
    print("IN function")

    time.sleep(60)

    print("out function")

if __name__ =="__main__":
    tic :float= time.time()

    t1= Process(target=bubble_sort_V2)
    t2= Process(target=bubble_sort_V2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    toc :float=time.time()
    time_elapsed :float= toc-tic

    print(f"{time_elapsed}")