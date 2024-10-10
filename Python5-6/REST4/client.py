import json, requests

base_url="http://127.0.0.1:8080"

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
    
    if api_url==base_url +"/req_cittadino":
        response= requests.get(api_url+"/" + CF)   
    elif api_url==base_url +"/mod_cittadino":
        response= requests.put(api_url,CF)   
    elif api_url==base_url +"/del_cittadino":
        response= requests.delete(api_url,CF)
    if response:
        return response
    
def EffettuaPrimoLogin():

    #inserisci username
    sUsername = input("Inserisci username: ")

    #inserisci password
    sPassword = input("Inserisci password: ")

    #componi jsonRequest
    jsonRequest = {"username": sUsername, "password":sPassword}

    try:
        #manda i dati al server
        api_url = base_url + "/login"
        response = requests.post(api_url,json=jsonRequest)
        
        #processa la risposta del server
        if response.status_code==200:
            jsonResponse = response.json
            if jsonResponse["Esito"]=="000":
                sPrivilegio = jsonResponse["Privilegio"]
                return sUsername,sPassword,sPrivilegio,1
    except:
        print("Attenzione, problemi di comunicazione con il server")



print("Benvenuti al Comune - sede locale")
sUsername=""
sPassword = ""
sPrivilegio = ""
iPrimoLoginEffettuato = 0 
while iPrimoLoginEffettuato == 0:
    sUsername, sPassword, sPrivlegio, iPrimoLoginEffettuato = EffettuaPrimoLogin()
ans=0
while ans != 5:
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino(es. atto di nascita)")
    print("2. Richiedi dati cittadino (es. cert. di residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")
    try:
        ans = int(input("Seleziona operazione= "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if ans==1:
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
    
    elif ans==2:
        api_url = base_url +"/req_cittadino"
        datiCit=ActionCittadino(api_url)
        print(f"Nome={datiCit["Nome"]}\nCognome={datiCit["Cognome"]}\nData di Nascita={datiCit["DN"]}\nCodice Fiscale={datiCit["CF"]}\n")

    elif ans==3:
        api_url = base_url +"/mod_cittadino"
        ActionCittadino(api_url)
    
    elif ans==4:
        api_url = base_url +"/del_cittadino"
        ActionCittadino(api_url)
        