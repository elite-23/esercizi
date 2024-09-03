# Luca Cavalleri
# 22/04/2024
x: int=123456789
s=str(x)
def is_palindrome(s):
    print(s)
    f:str=""
    for i in range(len(s)-1,-1,-1):
        f=f+s[i]
        print(f)
    if s==f:
        return True
    else:
        return False

is_palindrome(s)
