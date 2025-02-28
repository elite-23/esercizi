import psycopg2
from flask import Flask, json,jsonify, request, render_template
import flask_cors as CORS
#Dettagli connession
host="localhost"
port="5432"
dbname="accademia"
user="postgres"
password="postgres"

#Connection al databvase
try:
    connection=psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password)
    print("Connessione al database avvenuta con successo")
except Exception as e:
    print(f"Errore durante la connessione al database:{e}")

cursor=connection.cursor()
cycle=True
risp=input("Scegli:\n\t1:Tabella persone\n\t2:Tabella progetti\n\t3:Tabella wp\n\t4:Scrivi la tua query\n")
if risp=="1":
    cursor.execute("SELECT * FROM persona")
    rows = cursor.fetchall()
    for i in rows:
        print(i)

elif risp=="2":
    cursor.execute("SELECT * FROM progetto")
    rows = cursor.fetchall()
    for i in rows:
        print(i)

elif risp=="3":
    cursor.execute("SELECT * FROM wp")
    rows = cursor.fetchall()
    for i in rows:
        print(i)

elif risp=="4":
    print("Di quale tabella vuoi vedere i valori?\nInserisci il nome come riportato.")
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
    rows = cursor.fetchall()
    Query="FROM "
    l=[]
    x=0
    for i in rows:
        i=str(i)
        x+=1
        i=i.replace("(","")
        i=i.replace(")","")
        i=i.replace("'","")
        i=i.replace(",","")
        print("\t"+str(x)+"."+i)
        l.append(i)

    while cycle:
        ans=input("")
        if ans in l:
            Query+=ans
            print("Quale valore vuoi prendere dalla tabella?\nInserisci il nome come riportato.")
            print("\t1. * (Inserisci l'asterisco per visualizzare tutte le colonne)")
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name   = '"+ans+"'")
            rows = cursor.fetchall()
            l=["*"]
            x=1
            for i in rows:
                i=str(i)
                x+=1
                i=i.replace("(","")
                i=i.replace(")","")
                i=i.replace("'","")
                i=i.replace(",","")
                print("\t"+str(x)+"."+i)
                l.append(i)

            while cycle:
                ans=input("")
                if ans in l:
                    Query="SELECT "+ans+" "+Query

                    while cycle:
                        ans=input("Vuoi aggiungere un WHERE?(y/n)")
                        if ans=="y":

                            while cycle:
                                ans=input("Scrivi la condizione del WHERE: ")
                                try:
                                    cursor.execute(Query+" WHERE "+ans)
                                    rows = cursor.fetchall()
                                    for i in rows:
                                        print(i)
                                    cycle=False
                                except Exception as e:
                                    print(e)
                                    print("Condizione WHERE errata per favore riprovare ad inserirla")
                                    connection.reset()
                        
                        elif ans=="n":
                            cursor.execute(Query)
                            rows = cursor.fetchall()
                            for i in rows:
                                print(i)
                            cycle=False
                        else:
                            print("Inserisci o 'y' o 'n'")
                
                else:
                    print("Nome della colonna errato, riprova.")
        
        else:
            print("Nome della tabella errato")

cursor.close()
connection.close()