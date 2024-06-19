def decorator(func):

    def wrapper():
        print("Prima di func")

        func()

        print("Dopo di func")
    
    return wrapper

def ciao():

    print("ciao")

ciaoB=decorator(ciao)

ciaoB()