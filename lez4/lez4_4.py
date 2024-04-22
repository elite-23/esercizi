def convert_to_title(p:int):
    alphabet: list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    modul=p
    risp=""
    if p<=26:
        print()
    else:
        while modul>0:
            ind=modul%26
            risp=alphabet[ind-1]+risp
            modul=modul//26
        print(risp)
    return risp
convert_to_title(1021)