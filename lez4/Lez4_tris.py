# Luca Cavalleri
# 22/04/2024
def lenght_of_last_word(s:str)-> int:
    return len( s.split()[ len(s.split())-1 ] )
