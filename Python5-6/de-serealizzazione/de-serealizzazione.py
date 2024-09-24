mylist_1 = "['mario', 'gino', 'lucrezia']"

mylist_2 = ['mario', 'gino', 'lucrezia']

def serealizza(value:list)->str:
    return str(value)


def deserealizza(value:str)->list:
    value=value.replace("[","")
    value=value.replace("]","")
    value=value.replace(" ","")
    value=value.replace("'","")
    value=value.split(",")
    return value


print(mylist_1)
print(deserealizza(mylist_1))
print(mylist_2)
print(serealizza(mylist_2))