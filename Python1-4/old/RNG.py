"""
Scrivere una funzione che dati due numeri interi, N e M,
genera una sequenza di M cifre, casuali, comprese tra 1 e N
"""
#from random import randint

#m=int(input("Numero di numeri da generare randomicamente: "))
#n=int(input("Numero massimo generabile randomicamente: "))

#def RNGmxn(n,m):
#    Rng=[]
#    for i in range(m):
#        Rng.append(randint(0, n))
        
#    return Rng

#print(RNGmxn(n,m))

"""
 Funzione che date due liste <ls> e <lsCheck> di pari lunghezza,
 conta
 1) quante volte nella stessa posizione delle due
    liste appare lo stesso valore
 2) quante volte ci sono due valori uguali, uno per lista, ma non
    nella stessa posizione
 Esempio
 ls      [1,8,4,4,3,1]
 lsCheck [2,1,4,1,1,1]
 ci sono due elementi uguali nella stessa posizione delle due liste 4 e 1
 ci sono 1 elemento uguale ma in posizioni differenti
"""
ls=[1,8,4,4,3,1]
lsCheck=[2,1,4,1,1,1]
posug=0
posdv=0
for i in range(len(ls)):
    if ls[i]==lsCheck[i]:
        posug+=1
    for j in range(len(lsCheck)):
        if i!=j and ls[i]==lsCheck[j]:
            posdv+=1
print("1) = ",posug,"\n2) = ",posdv)
        
        
        
        
        
        
        
        
        