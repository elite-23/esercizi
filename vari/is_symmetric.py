#Luca Cavalleri

def symmetric(tree: list[int]) -> bool:
    tree_dict={"0a":tree[1],"0b":tree[2]}
    floor=0
    if tree_dict["0a"] != tree_dict["0b"]:
        return False
    
    #step=2
    for i in range(1,len(tree)//2,2):
        floor+=1
        tree_dict[str(floor)+"a"]=[]
        tree_dict[str(floor)+"b"]=[]
        if 2*(i+1)+(floor*2)<len(tree):
            
            for j in range(0,floor*2):
                #print("i=",i)
                #print("j=",j)
                tree_dict[str(floor)+"a"].append(tree[2*i+1+j])
                tree_dict[str(floor)+"b"].append(tree[2*i+1+(floor*2)+j])
                
            
            if i!=1 and tree_dict[str(i-1)+"a"]!=list(reversed(tree_dict[str(i-1)+"b"])):
                return False
    print(tree_dict)    
    return True

print(symmetric([1,2,2,3,4,4,3]))
print(symmetric([1,2,2,None,3,None,3]))
print(symmetric([1,2,2,None,3,3,None]))
print(symmetric([1,2,2,3,None,None,3]))
print(symmetric([1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]))