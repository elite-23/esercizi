import json, requests

base_url="http://127.0.0.1:8080"

def CreaInterfaccia():
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino(es. atto di nascita)")
    print("2. Richiedi dati cittadino (es. cert. di residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")

def AddCittadino():
    print("\nInserisci i dati del cittadino:")
    nome=input("Nome= ")
    cognome=input("Cognome= ")
    dataNascita=input("Data di nascita= ")
    codFiscale=input("Codice fiscale= ")
    jRequest={"nome":nome, "cognome":cognome, "DN":dataNascita,"CF":codFiscale}
    return jRequest

def ActionCittadino(api_url):
    CF=input("Inserisci il Codice Fiscale del cittadino d'interesse: ")
    response= requests.post(api_url,CF)
    if response:
        return response
    


CreaInterfaccia()
ans=input("Seleziona operazione= ")
while (ans != "5"):
    if ans=="1":
        api_url = base_url +"/add_cittadino"
        datiCit = AddCittadino()
        try:
            response = requests.post(api_url,json=datiCit)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1=response.json()
            print(data1)
        except:
            print("\nProblemi di comunicazione con il server, riprova più tardi.\n")
    elif ans=="2":
        api_url = base_url +"/req_cittadino"
        datiCit=ActionCittadino(api_url)
        print(f"Nome={datiCit["Nome"]}\nCognome={datiCit["Cognome"]}\nData di Nascita={datiCit["DN"]}\nCodice Fiscale={datiCit["CF"]}\n")

    elif ans=="3":
        api_url = base_url +"/mod_cittadino"
        ActionCittadino(api_url)
    elif ans=="4":
        api_url = base_url +"/del_cittadino"
        ActionCittadino(api_url)
    CreaInterfaccia()
    ans=input("Seleziona operazione= ")