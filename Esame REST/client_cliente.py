import requests,json
import sys

base_url = "http://127.0.0.1:8080"
cycle = True
contr=True


while cycle:

    risp = input("1) Ceraca case in vendita\n"
                "2) Ceraca case in affitto\n"
                "3) metti una casa in vendia\n"
                "4) metti una casa in affitto\n"
                "5) esci\n")

    if risp == "1":

        api_url = base_url + '/CercaCasaVendita'

        print("Mettere quanti metri quadri minimi si vogliono")
        risposta_metri_min = input()
        print("Mettere quanti metri quadri massimi si vogliono")
        risposta_metri_max = input()

        print("Mettere quanti vani minimi si vogliono")
        rispsota_vani_min = input()
        print("Mettere quanti vani massimi si vogliono")
        rispsota_vani_max = input()

        print("Mettere il prezzo minimo con il quale vuole cercare la casa")
        risposta_prezzo_min = input()
        print("Mettere il prezzo massimo con il quale vuole cercare la casa")
        risposta_prezzo_max = input()

        print("Mettere a quale piano si preferisce la casa")
        risposta_piano = input()

        while contr:
            print("casa libera o ancora occupata? l/o")
            risoposta_stato = input()
            if risoposta_stato == "l":
                risoposta_stato = 'LIBERO'
                contr=False

            elif risoposta_stato == "o":
                risoposta_stato = 'OCCUPATO'
                contr=False
            
            else:
                print("ERROE dato non valido")
        
        contr = True

        diz_risposta = {"metri_m" : risposta_metri_min, "metri_M" : risposta_metri_max, 
                        "vani_m" : rispsota_vani_min, "vani_M" : rispsota_vani_max, 
                        "prezzo_m" : risposta_prezzo_min, "prezzo_M" : risposta_prezzo_max,
                        "piano" : risposta_piano, "stato" : risoposta_stato}
        
        request_vendita = requests.post(api_url, json=diz_risposta, verify=False)
        if request_vendita.status_code==200:
            print("Le case trovate sono:\n",request_vendita.json())
        else:
            print("Attenzione, errore " + str(request_vendita.status_code))

    elif risp =="2":
        api_url = base_url + '/CercaCasaAffitto'

        print("Mettere il prezzo minimo mensile con il quale vuole cercare la casa")
        risposta_prezzo_min_mensile = input()
        print("Mettere il prezzo massimo mensile con il quale vuole cercare la casa")
        risposta_prezzo_max_mensile = input()

        while contr:
            print("quale tipo di affitto si vuole PARZIALE | TOTALE? p/t\n")
            tipo_affitto = input()
            if tipo_affitto == "p":
                tipo_affitto = 'PARZIALE'
                contr=False

            elif tipo_affitto == "t":
                tipo_affitto = 'TOTALE'
                contr=False
            
            else:
                print("ERROE dato non valido")

        contr = True
                
        while contr:
            print("Vuole avere un bagno personale? s/n\n")
            bagno = input()

            if bagno == "s":
                bagno = True
                contr = False
            
            elif bagno == "n":
                bagno = False
                contr = False
            
            else:
                print("ERROE dato non valido")
        
        contr = True

        diz_risposta = {"tipo_affitto" : tipo_affitto,
                        "bagno_personale" : bagno,
                        "prezzo_m" : risposta_prezzo_min_mensile,
                        "prezzo_M" : risposta_prezzo_max_mensile}
        
        request_vendita = requests.post(api_url, json=diz_risposta, verify=False)
        if request_vendita.status_code==200:
            print("Le case trovate sono:\n",request_vendita.json())
        else:
            print("Attenzione, errore " + str(request_vendita.status_code))


    elif risp =="3":
        api_url = base_url + '/VendiCasa'

        print("da quale filiale lo sta facendo?")
        filiale = input()

        print("inserire i m^2 della casa")
        metri= input()

        print("inserire il n di stanze")
        numero_stanze = input()

        print("il piano di dove si trova la casa")
        piano = input()

        print("inserire l'indirizzo della casa")
        indirizzo = input()

        print("inserire il civico della casa")
        civico = input()

        print("Mettere il prezzo di vendita")
        prezzo = input()

        print("Mettere la catastale")
        catastale = input()


        while contr:
            print("casa libera o ancora occupata? l/o")
            risoposta_stato = input()
            if risoposta_stato == "l":
                risoposta_stato = 'LIBERO'
                contr=False

            elif risoposta_stato == "o":
                risoposta_stato = 'OCCUPATO'
                contr=False
            
            else:
                print("ERROE dato non valido")
            
        contr = True

        diz_risposta = {"indirizzo" : indirizzo, "filiale_proponente" : filiale, 
                        "prezzo" : prezzo, "catastale" : catastale, 
                        "numero_civico": civico, "stato":risoposta_stato,
                        "piano":piano, "metri": metri,
                        "vani" : numero_stanze}
        
        request_vendita  = requests.post(api_url, json=diz_risposta, verify=False)
        print(request_vendita.status_code)
    elif risp =="4":

        api_url = base_url + '/AffittaCasa'

        print("da quale filiale lo sta facendo?")
        filiale = input()

        print("inserire l'indirizzo della casa")
        indirizzo = input()

        print("inserire il civico della casa")
        civico = input()

        print("Mettere il prezzo di affitto")
        prezzo = input()

        print("Mettere la catastale")
        catastale = input()

        while contr:
            print("quale tipo di affitto si vuole PARZIALE | TOTALE? p/t")
            tipo_affitto = input()
            if tipo_affitto == "p":
                tipo_affitto = 'PARZIALE'
                contr=False

            elif tipo_affitto == "t":
                tipo_affitto = 'TOTALE'
                contr=False
            
            else:
                print("ERROE dato non valido")

        contr = True
                
        while contr:
            print("Vuole avere un bagno personale? s/n")
            bagno = input()

            if bagno == "s":
                bagno = True
                contr = False
            
            elif bagno == "n":
                bagno = False
                contr = False
            
            else:
                print("ERROE dato non valido")
        
        contr = True


        diz_risposta = {"indirizzo" : indirizzo, "filiale_proponente" : filiale, 
                        "prezzo" : prezzo, "catastale" : catastale, 
                        "numero_civico": civico, "tipo_affitto" : tipo_affitto,
                        "bagno_personale": bagno}
        
        request_vendita  = requests.post(api_url, json=diz_risposta, verify=False)
        print(request_vendita.status_code)

    elif risp =="5":
        
        print("arrivederci")
        cycle = False
    
    else:
        print("ERRORE dato non valido")


        
