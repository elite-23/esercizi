import requests,json
import sys
import re

base_url = "http://127.0.0.1:8080"
cycle = True
contr=True


while cycle:    

    risp = input("Inserire il numero di ciò che desideri fare\n"
                "\t1) visualizzare e salvare su json il report di vendite per periodo di ogni filiale\n"
                "\t2) visualizzare e salvare su json il report di guadagno per periodo di ogni filiale\n"
                "\t3) uscire")
    
    if risp == "1":

        api_url = base_url + '/ReportVendite'

        print("Inserire la data di inizio con il seguente formato 'AAAA-MM-GG'")
        while contr:
            inizio = input()
            pattern_str = r'^\d{4}-\d{2}-\d{2}$'
            if re.match(pattern_str, inizio):
                contr = False
            else:
                print("Per favore inserisci una data nel formato corretto 'AAAA-MM-GG'")
        contr = True

        print("Inserire la data di fine con il seguente formato 'AAAA-MM-GG'")
        while contr:
            fine = input()
            pattern_str = r'^\d{4}-\d{2}-\d{2}$'
            if re.match(pattern_str, fine):
                contr = False
            else:
                print("Per favore inserisci una data nel formato corretto 'AAAA-MM-GG'")
        contr=True

        diz_risposta = {"inizio" : inizio, "fine" : fine}
        request_report_vendite = requests.post(api_url, json=diz_risposta, verify=False)

    elif risp == "2":

        api_url = base_url + '/ReportEntrate'

        print("Inserire la data di inizio con il seguente formato 'AAAA-MM-GG'")
        while contr:
            inizio = input()
            pattern_str = r'^\d{4}-\d{2}-\d{2}$'
            if re.match(pattern_str, inizio):
                contr = False
            else:
                print("Per favore inserisci una data nel formato corretto 'AAAA-MM-GG'")
        contr = True

        print("Inserire la data di fine con il seguente formato 'AAAA-MM-GG'")
        while contr:
            fine = input()
            pattern_str = r'^\d{4}-\d{2}-\d{2}$'
            if re.match(pattern_str, fine):
                contr = False
            else:
                print("Per favore inserisci una data nel formato corretto 'AAAA-MM-GG'")
        contr=True

        diz_risposta = {"inizio" : inizio, "fine" : fine}
        request_report_guadagni = requests.post(api_url, json=diz_risposta, verify=False)

    elif risp == "3":
        print ("arrivederci")
        cycle = False

    else:
        print("ERRORE dato non valido")

