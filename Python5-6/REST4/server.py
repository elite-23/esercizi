from flask import Flask, json, request
from myjson import JsonSerialize, JsonDeserialize

FileA="anagrafe.json"
api=Flask(__name__)

@api.route("/add_cittadino", methods=["POST"])
def AddCittdino():
    content_type=request.headers.get("Content-Type")
    print("Ricevuta chiamata "+content_type)
    if content_type == "application/json":
        Anagrafe=JsonDeserialize(FileA)
        jRequest=request.json
        print(jRequest)

        CF=jRequest["CF"]
        if CF not in Anagrafe.keys():
            Anagrafe[CF]=jRequest
            JsonSerialize(Anagrafe,FileA)
            jResponse={"Error":"000", "Msg":"ok"}
            return json.dumps(jResponse),200
        else:
            jResponse={"Error":"001", "Msg":"COdice fiscale già presente nel database"}
            return json.dumps(jResponse),301
    else:
        return "Errore formato non riconosciuto",401

@api.route("/req_cittadino/<CF>", methods=["GET"])
def ReqCittadino(CF):
    content_type=request.headers.get("Content-Type")
    print("Ricevuta chiamata "+content_type)
    if content_type == "application/json":
        Anagrafe=JsonDeserialize(FileA)
        print(CF)
        if CF in Anagrafe.keys():
            return Anagrafe[CF]
        else:
            jResponse={"Error":"002", "Msg":"Codice fiscale non presente nel database"}
            return json.dumps(jResponse),302

@api.route("/mod_cittadino", methods=["PUT"])
def ModCittadino():
    content_type=request.headers.get("Content-Type")
    print("Ricevuta chiamata "+content_type)
    if content_type == "application/json":
        Anagrafe=JsonDeserialize(FileA)
        CF=request.json
        print(CF)
        if CF in Anagrafe.keys():
            mod=0
            print("I dati del cittadino selezionato:")
            print(f"Nome={Anagrafe[CF]["Nome"]}\nCognome={Anagrafe[CF]["Cognome"]}\nData di Nascita={Anagrafe[CF]["DN"]}\nCodice Fiscale={Anagrafe[CF]["CF"]}\n")
            while mod<5:
                mod=input("Selezionare cosa si vuole modificare:\n1-Nome\n2-Cognome\n3-Data di Nascita\n4-Codice Fiscale\n5-Exit\n")
                if mod==1:
                    Anagrafe[CF]["Nome"]=input("Inserisci il nuovo valore del nome:")
                elif mod==2:
                    Anagrafe[CF]["Cognome"]=input("Inserisci il nuovo valore del cognome:")
                elif mod==3:
                    Anagrafe[CF]["DN"]=input("Inserisci il nuovo valore della data di nascita:")
                elif mod==4:
                    n=input("Inserisci il nuovo valore del codice fiscale:")
                    if n in Anagrafe.keys():
                        jResponse={"Error":"002", "Msg":"Codice fiscale già presente nel database"}
                        return json.dumps(jResponse),302
                    else:
                        Anagrafe[n]={"Nome":Anagrafe[CF]["Nome"],"Cognome":Anagrafe[CF]["Cognome"],"DN":Anagrafe[CF]["DN"],"CF":n}
                        Anagrafe.pop(CF)
                        CF=n
            JsonSerialize(Anagrafe,FileA)
            jResponse={"Error":"003", "Msg":"Dati modificati con successo."}
            return json.dumps(jResponse),202
        else:
            jResponse={"Error":"002", "Msg":"Codice fiscale non presente nel database."}
            return json.dumps(jResponse),302

@api.route("/del_cittadino", methods=["DELETE"])
def DelCittadino():
    Anagrafe=JsonDeserialize(FileA)
    CF=request.json
    if CF in Anagrafe.keys():
        Anagrafe.pop(CF)
        jResponse={"Error":"003", "Msg":"Cittadino eliminato con successo."}
        return json.dumps(jResponse),202
    else:
        jResponse={"Error":"002", "Msg":"Codice fiscale non presente nel database."}
        return json.dumps(jResponse),302

api.run(host="127.0.0.1",port=8080)