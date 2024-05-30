import random

def tartaruga(pos,stamina,pioggia):
    x=random.randint(1,10)

    if (pioggia//10)%2==0:
        #print("SOleeeeee")
        pioggia=0
    else:
        #print("PIOGGIAAAAAAA")
        pioggia=-1

    if x<=5: #Passo veloce
        if stamina>=5:
            stamina-=5
            if pos+3+pioggia>69:
                pos=69
            else:
                pos+=3+pioggia
        else:
            stamina+=10

    elif x<=7:#Scivolata
        if pos-6+pioggia>=0 and stamina>=10:
            pos-=6+pioggia
            stamina-=10
        elif pos-6+pioggia<0 and stamina>=10:
            pos=0
            stamina-=10
        else:
            stamina+=10

    elif x<=10:#Passo lento
        if  stamina>=3:
             stamina-=3
             pos+=1+pioggia
        else:
             stamina+=10

    return [pos,stamina]
    

def Lepre(pos,stamina,pioggia):
    x=random.randint(1,10)
    
    if (pioggia//10)%2==0 :
        pioggia=0 
    else:
        pioggia=-2

    if x<=2:#Riposo
        if stamina+5<= 100:
            stamina+=5
        else:
            stamina=100
    elif x<=4:#Grande balzo
        if stamina>=15:
            stamina-=15
            if pos+9+pioggia>69:
                pos=69
            else:
                pos+=9+pioggia
        else:
            stamina+=10
    elif x==5:#Grande scivolata
        if pos-12+pioggia>=1 and stamina>=20:
            pos-=12+pioggia
            stamina-=20
        elif pos-12+pioggia<0 and stamina>=20:
            pos=0
            stamina-=20
        else:
            stamina+=10
    elif x<=8:#Piccolo balzo
        if stamina>=5 and pos+1+pioggia>=0:
            stamina-=5
            pos+=1+pioggia
        elif stamina>=5 and pos+1+pioggia<0:
            pos=0
        else:
            stamina+=10
    elif x<=10:#piccola scivolata
        if pos-2+pioggia>=0 and stamina>=8:
            pos-=2+pioggia
            stamina-=8
        elif pos-2+pioggia<0 and stamina>=8:
            pos=0
            stamina-=8
        else:
            stamina+=10

    return [pos,stamina]

def Gara():
    pioggia=-1
    bonus={2:3,4:3,8:5,16:3,32:7,64:4}
    ostacolo={10:-4,20:-2,30:-3,40:-6,50:-1,60:-5}
    percorso=["+" if i in bonus.keys()  else "-" for i in range(70)]
    T=[0,100]
    L=[0,100]
    for i in ostacolo.keys():
        percorso[i]="/"

    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while percorso[-1]=="-":
        pioggia+=1
        percorso[T[0]]="-"
        percorso[L[0]]="-"
        
        T=tartaruga(T[0],T[1],pioggia)
        if T[0] in bonus.keys():
            #print("BONUSSSS - Tortoise")
            T[0]+=bonus[T[0]]
        elif T[0] in ostacolo.keys():
            #print("Obstacleee - Tortoise")
            T[0]+=ostacolo[T[0]]
        percorso[T[0]]="T"
        
        L=Lepre(L[0],L[1],pioggia)
        if percorso[L[0]]=="T":
            percorso[L[0]]="OUCH!!!"
        else:
            if L[0] in bonus.keys():
                #print("BONUSSSS - Hare")
                L[0]+=bonus[L[0]]
            elif L[0] in ostacolo.keys():
                #print("Obstacleee - Hare")
                L[0]+=ostacolo[L[0]]
            percorso[L[0]]="H"
        print("".join(percorso))

    if percorso[-1]=="T":
        print("TORTOISE WINS! || VAY!!!")
    elif percorso[-1]=="H":
        print("HARE WINS || YUCH!!!") 
    else:
        print("IT'S A TIE.") 

Gara()