def majority_element(nums: list[int])->int:
    obg=len(nums)//2
    dict = {key: 0 for key in set(nums)}

    for i in nums:
        dict[i]+=1
    x=sorted(dict.items(),key=lambda item: item[1],reverse=True)
    print("La lista:",nums,"\n la lista ordinata in base al numero di presenze del numero:",x)
    if x[0][1]>=obg:
        return x[0][0]
    else:
        print("Nessun numero è presente più volte della metà della lunghezza della lista.")

print(majority_element([1,1,2,1,5,2,3,1,3,1,7]))