import copy
def move_elements(lista :list[int], k :int):
    l=copy.deepcopy(lista)
    if k==len(lista):
        return lista
    elif k>len(lista):
        print(k)
        k=k-((k//len(lista))*len(lista))
        print(k)
    for i in range(len(lista)):
        print(l)
        if i+k<=len(lista)-1:
            l[i+k]=lista[i]
        else:
            l[i+k-len(lista)]=lista[i]
    return l
li=[0,1,2,3,4,5]
print(move_elements(li,6))