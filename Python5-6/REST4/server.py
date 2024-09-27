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

@api.route("/req_cittadino", methods=["POST"])
def ReqCittadino():
    content_type=request.headers.get("Content-Type")
    print("Ricevuta chiamata "+content_type)
    if content_type == "application/json":
        Anagrafe=JsonDeserialize(FileA)
        CF=request.json
        print(CF)
        if Anagrafe[CF]:
            return Anagrafe[CF]
        
        else:
            jResponse={"Error":"002", "Msg":"Codice fiscale non presente nel database"}
            return json.dumps(jResponse),302

@api.route("/mod_cittadino", methods=["POST"])
def ModCittadino():
    return 0

@api.route("/del_cittadino", methods=["POST"])
def DelCittadino():
    return 0








api.run(host="127.0.0.1",port=8080)