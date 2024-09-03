#Luca Cavalleri

def lenght_of_last_word(s:str)-> int:
    return len( s.split()[ len(s.split())-1 ] )
