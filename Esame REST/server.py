from flask import Flask, json,jsonify, request, render_template
import psycopg2
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore di connessione al DB")
    sys.exit()

#Ricerca nel database delle case in vendita in base ai requisiti del cliente
@api.route('/CercaCasaVendita', methods=['POST'])
def CercaCaseVendita():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata" + content_type)

    if content_type == 'application/json':

        metri_m = request.json["metri_m"]
        metri_M = request.json["metri_M"]
        vani_m = request.json["vani_m"]
        vani_M = request.json["vani_M"] 
        prezzo_m = request.json["prezzo_m"]
        prezzo_M = request.json["prezzo_M"]
        piano = request.json["piano"]
        stato = request.json["stato"]

        query= f"""SELECT *
                FROM case_in_vendita
                WHERE metri BETWEEN {metri_m} AND {metri_M} 
                AND prezzo BETWEEN {prezzo_m} AND {prezzo_M} 
                AND vani BETWEEN {vani_m} AND {vani_M} 
                AND piano = {piano} AND stato = \'{stato}\';"""
        
        if  db.read_in_db(mydb, query) > 0:
            rows = mydb.fetchall()
            return rows, 200
        else:
            return {"Esito": "003", "Msg": "La query non ha restituito righe"}  
    else:
        return {"Esito": "002", "Msg": "Formato richiesta non valido"}

#Ricerca nel database delle case in affitto in base ai requisiti del cliente
@api.route('/CercaCasaAffitto', methods=['POST'])
def CercaCasaAffitto():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata" + content_type)

    if content_type == 'application/json':

        tipo_affitto = request.json["tipo_affitto"]
        bagno = request.json["bagno_personale"]
        prezzo_m = request.json["prezzo_m"]
        prezzo_M = request.json["prezzo_M"]

        query= f"""SELECT *
                FROM case_in_affitto
                WHERE prezzo_mensile BETWEEN {prezzo_m} AND {prezzo_M} 
                AND bagno_personale = {bagno} AND tipo_affitto = \'{tipo_affitto}\';"""
        print(query)
        if  db.read_in_db(mydb, query) > 0:
            rows = mydb.fetchall()
            return rows, 200
        else:
            return {"Esito": "003", "Msg": "La query non ha restituito righe"},300 
    else:
        return {"Esito": "002", "Msg": "Formato richiesta non valido"},300

#Aggiunta nel database di una casa in vendita con i dati forniti dal cliente
@api.route('/VendiCasa', methods=['POST'])
def VendiCasa():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)

    if content_type == 'application/json':

        catastale = request.json["catastale"]
        indirizzo = request.json["indirizzo"]
        civico = request.json["numero_civico"]
        piano = request.json["piano"]
        metri = request.json["metri"]
        vani = request.json["vani"]
        prezzo = request.json["prezzo"]
        stato = request.json["stato"]
        filiale = request.json["filiale_proponente"]
        
        query = f"""SELECT *
                FROM case_in_vendita
                WHERE catastale = {catastale};"""
        
        if  db.read_in_db(mydb, query)< 0:
            query = f"""INSERT INTO case_in_vendita (catastale, indirizzo, numero_civico, piano, metri,vani, prezzo,stato,filiale_proponente )
                    VALUES (\'{catastale}\', \'{indirizzo}\', \'{civico}\', {piano}, {metri}, {vani}, {prezzo}, \'{stato}\', \'{filiale}\'); """
            db.write_in_db(query)
            return {"Esito":"000", "Msg":"Casa aggiunta al database con successo"}, 200
        else:
            return {"Esito": "001", "Msg": "Una casa con questo catastale è già presente"},300
    else:
        return {"Esito": "002", "Msg": "Formato richiesta non valido"},300

#Aggiunta nel database di una casa in affitto con i dati forniti dal cliente         
@api.route('/AffittaCasa', methods=['POST'])
def AffittaCasa():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)

    if content_type == 'application/json':
        
        catastale = request.json["catastale"]
        indirizzo = request.json["indirizzo"]
        civico = request.json["numero_civico"]
        tipo_affitto = request.json["tipo_affitto"]
        bagno = request.json["bagno_personale"]
        prezzo = request.json["prezzo"]
        filiale = request.json["filiale_proponente"]

        query = f"""SELECT *
                FROM case_in_affitto
                WHERE catastale = {catastale};"""
        
        if db.read_in_db(mydb, query) == -1:
            query = f"""INSERT INTO case_in_vendita (catastale, indirizzo, numero_civico,tipo_affitto,bagno_personale, prezzo_mensile, filiale_proponente, )
                    VALUES (\'{catastale}\', \'{indirizzo}\', \'{civico}\',\'{tipo_affitto}\',{bagno}, {prezzo}, \'{filiale}\'); """
            db.write_in_db(query)
            return {"Esito":"000", "Msg":"Casa aggiunta al database con successo"}, 200
        else:
            return {"Esito": "001", "Msg": "Una casa con questo catastale è già presente"}
    else:
        return {"Esito": "002", "Msg": "Formato richiesta non valido"}

#Ricerca della sezione marketing per vedere in un lasso di tempo le vendite di ogni filiale
@api.route('/ReportVendite', methods=['POST'])
def ReportVendite():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)

    if content_type == 'application/json':

        inizio = request.json["inizio"]
        fine = request.json["fine"]

        query = f"""SELECT v.filiale_venditrice AS Filiale,
                    TO_CHAR(v.data_vendita, 'YYYY-MM') AS Mese,
                    COUNT(DISTINCT v.catastale) AS Numero_Case_Vendute,
                    COUNT(DISTINCT a.catastale) AS Numero_Case_Affittate
                FROM vendite_casa as v LEFT JOIN affitti_casa as a
                ON v.filiale_venditrice = a.filiale_venditrice 
                    AND TO_CHAR(v.data_vendita, 'YYYY-MM') = TO_CHAR(a.data_affitto, 'YYYY-MM')
                WHERE (v.data_vendita BETWEEN \'{inizio}\' AND \'{fine}\'
                    OR a.data_affitto BETWEEN \'{inizio}\' AND \'{fine}\')
                GROUP BY v.filiale_venditrice, TO_CHAR(v.data_vendita, 'YYYY-MM')
                ORDER BY Filiale, Mese;"""

        if  db.read_in_db(mydb, query) > 0:
            rows = mydb.fetchall()

            columns = [desc[0] for desc in mydb.description]
            print(columns)
            result = [dict(zip(columns, row)) for row in rows]
            file = 'report_vendite.json'

            with open(file, 'w') as json_file:
                json.dump(result, json_file, indent=4)

            return rows, 200
        else:
            return {"Esito": "003", "Msg": "La query non ha restituito righe"}  
    else:
        return {"Esito": "002", "Msg": "Formato richiesta non valido"}

#Ricerca della sezione marketing per vedere in un lasso di tempo il guadagno di ogni filiale
@api.route('/ReportEntrate', methods=['POST'])
def ReportEntrare():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)

    if content_type == 'application/json':

        inizio = request.json["inizio"]
        fine = request.json["fine"]

        query_vendite = f"""SELECT v.catastale as catastale, v.filiale_venditrice AS filialeV, TO_CHAR(v.data_vendita, 'YYYY-MM') AS mese, v.prezzo_vendita as prezzo
                        FROM vendite_casa as v
                        WHERE v.data_vendita BETWEEN {inizio} AND {fine}
                        ORDER BY filialeV;"""

        query_affitti=f"""SELECT a.catastale as catastale, a.filiale_venditrice AS filialeV, TO_CHAR(a.data_affitto, 'YYYY-MM') AS mese
                        FROM affitti_casa as a
                        WHERE a.data_affitto BETWEEN {inizio} AND {fine}
                        ORDER BY filialeV"""
        
        mydb.execute("SELECT partita_iva FROM filiali")
        rows_f=list(mydb.fetchall())
        guad=[]
        for i in rows_f:guad.append(0)

        if  db.read_in_db(mydb, query_vendite) > 0:
            rows_v = mydb.fetchall()
            if db.read_in_db(mydb, query_affitti) > 0:
                rows_a=mydb.fetchall()
            else:
                #niente affitti in quel periodo
                print()
            for i in range(0,len(rows_a)):
                for j in range(0,len(rows_f)):
                    if rows_f[j]==rows_a[i][1]:
                        guad[j]+=(float(rows_a[i][3])*0.01)


            columns = [desc[0] for desc in mydb.description]
            print(columns)
            result = [dict(zip(columns, row)) for row in rows]
            file = 'report_entrate.json'

            with open(file, 'w') as json_file:
                json.dump(result, json_file, indent=4)

            return rows, 200
        elif db.read_in_db(mydb, query_affitti) > 0:
            #niente vendite in quel periodo
            print()
        else:
            return jsonify({"Esito": "003", "Msg": "La query non ha restituito righe"})
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"})




if __name__ == "__main__":
    api.run(host="127.0.0.1", port = 8080)