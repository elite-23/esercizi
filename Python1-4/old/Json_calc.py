# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# X1) contare quanti calciatori hanno giocato per l'Italia
# X2) contare quanti calciatori hanno giocato per il Brasile
# X3) contare quanti calciatori hanno giocato per l'Argentina
# X4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# X5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# X6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# X7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# X8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# X9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...
import json

# Apro il file, lo leggo e chiudo
fin = open("all-world-cup-players.json", "r")
calciatori = json.load(fin)
fin.close()

#Es. 1, 2, 3
Ita=0
Bra=0
Arg=0

#Es. 4, 5
Italiani=[]
Brasiliani=[]
Argentini=[]

#Es. 6, 7
age=0
ageM=["",0]
agem=["",100]

#Es. 8, 9
CalcNed={}
SquaNed=[['ALG','Algeria'], 'Angola', ['ARG','Argentina'], ['AUS','Australia'],['AUT', 'Austria'],['BEL', 'Belgium'], 'Bolivia', 'Bolivia ', 'Bosnia and Herzegovina',['BRA', 'Brazil'], ['BUL','Bulgaria'], 'Cameroon',['CAN'] ['CHI','Chile','Chile '], 'China PR', ['COL','Colombia'], 'Costa Rica', 'Croatia', 'Cuba', 'Czech Republic', 'Czechoslovakia', "CÃƒÂ´te d'Ivoire", ['DEN','Denmark'], 'Dutch East Indies', 'Ecuador', 'Egypt', 'El Salvador', ['ENG','England','England '], 'FR Yugoslavia', 'France', 'Germany', 'Ghana', 'Greece', 'Honduras', 'Hungary', 'Iran', 'Italy', 'Italy ', 'Ivory Coast', 'Jamaica', 'Japan', 'Korea DPR', 'Korea Republic', 'Kuwait', 'Mexico', 'Mexico ', 'Morocco', 'Netherlands', 'New Zealand', 'Nigeria', 'Northern Ireland', 'Norway', 'Paraguay', 'Paraguay ', 'Peru', 'Poland', 'Portugal', 'Republic of Ireland', 'Romania', 'Russia', 'SFR Yugoslavia', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Serbia and Montenegro', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Soviet Union', 'Spain', 'Spain ', 'Sweden', 'Switzerland', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'USSR', 'Ukraine', 'United Arab Emirates', 'United States', 'United States ', 'Uruguay', 'West Germany', 'Yugoslavia', 'Yugoslavia ']

for e in calciatori:
    
    #Es. 1, 2, 3
    if e["FullName"]!="":
        
        if e["Team"] in ["ITA", "Italy"]:
            Ita+=1
            Italiani.append(e["FullName"])
            
        if e["Team"] in ["BRA","Brazil"]:
            Bra+=1
            Brasiliani.append(e["FullName"])
            
        if e["Team"] in ["ARG","Argentina"]:
            Arg+=1
            Argentini.append(e["FullName"])
    
    #Es. 6, 7
    if e["DateOfBirth"]!="" and e["FullName"]!="":
        
        age= e["Year"]-int(e["DateOfBirth"].split("-")[0])
        if age<agem[1]:
            agem[1]=age
            agem[0]=e["FullName"]
        
        if age>ageM[1]: 
            ageM[1]=age
            ageM[0]=e["FullName"]
    
    #Es. 8, 9
    if e["FullName"]!="":
        
        if e["FullName"] in CalcNed:
            CalcNed[e["FullName"]]+=1
        else:
            CalcNed[e["FullName"]]=1
        
    if e["Team"] in SquaNed:
        SquaNed[e["Team"]]+=1
    else:
        SquaNed[e["Team"]]=1

#Es 4, 5
BraIta=[]
ArgIta=[]
for i in Italiani:
    
    if i in Brasiliani:
        BraIta.append(i)
        
    if i in Argentini:
        ArgIta.append(i)
    

print("Es. 1, 2, 3")
print("ITA:",Ita,"\nBRA:",Bra,"\nARG:",Arg)

print("\nEs. 4, 5")
print("Ecco i giocatori che hanno giocato sia per l'Italia che il Brasile",BraIta)
print("Ecco i giocatori che hanno giocato sia per l'Italia che l'Argentina",ArgIta)

print("\nEs. 6, 7")
print("Il giocatore più anziano ad aver giocato nel mondiale è: ",ageM[0]," all'età di: ",ageM[1])
print("Il giocatore più giovane ad aver giocato nel mondiale è: ",agem[0]," all'età di: ",agem[1])

print("\nEs.8, 9")
SortedCalcNed = dict(sorted(CalcNed.items(),key=lambda x:x[1],reverse = True))
SortedSquaNed = dict(sorted(SquaNed.items(),key=lambda x:x[1],reverse = True))
print("Il giocatore con più partecipazioni è ",list(SortedCalcNed.keys())[0]," con ",SortedCalcNed[list(SortedCalcNed.keys())[0]]," partecipazioni.")
print("Il team con più giocatori partecipanti è ",list(SortedSquaNed.keys())[0]," con ",SortedSquaNed[list(SortedSquaNed.keys())[0]]," giocatori.")





