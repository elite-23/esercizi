from flask import Flask, render_template, request

api=Flask(__name__)

utenti: list[list[str]]=[["Mario","Password1","1","1"],["Luigi","Password2","1","0"],["Francesca","Password3","2","0"]]


@api.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@api.route('/regko', methods=['GET'])
def regKo():
    return render_template("reg_ko.html")

@api.route('/regok', methods=['GET'])
def regOk(Uname: str,Usex: str):
    if Usex=="1":
        Usex="un maschio"
    else:
        Usex="una femmina"
    context={"Usex":Usex,"Uname":Uname}
    return render_template("reg_ok.html", **context)

@api.route("/ordinipas",methods=["GET"])
def ordinipas():
    context={"Uname":request.args.get("Nome")}
    return render_template("ordinipas.html", **context)

@api.route("/ordinicor",methods=["GET"])
def ordinicor():
    context={"Uname":request.args.get("Nome")}
    return render_template("ordinicor.html", **context)


@api.route('/registrati', methods=['GET'])
def registrati():
    utente: list[str]=[str(request.args.get("fnome")),str(request.args.get("fpassword")),str(request.args.get("fsesso")),"0"]
    print(utente)
    if utente in utenti:
        utenti[utenti.index(utente)][3]="1"
        return regOk(utente[0],utente[2])
    return regKo()

@api.route("/accedi",methods=["GET"])
def accedi():
    utente: list[str]=[str(request.args.get("fnome")),str(request.args.get("fpassword")),"1"]
    print(utente)
    for u in utenti:
        i=u
        i.pop(2)
        print(i)
        if utente == i:
            return regOk(u[0],u[2])
    return regKo()



api.run(host="0.0.0.0",port=8085)