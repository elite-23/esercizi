def symmetric(tree: list[int]) -> bool:
    tree_dict={"0a":tree[1],"0b":tree[2]}
    floor=2
    if tree_dict["0a"] != tree_dict["0b"]:
        return False
    
    for i in range(1,len(tree)//2,2):
        if 2*(i+1)+1<len(tree):
            for j in range(1,floor*2+1):
                
            #tree_dict[str(i)+"a"]=[tree[2*i+1],tree[2*(i+1)]]
            #tree_dict[str(i)+"b"]=[tree[2*(i+1)+1],tree[2*((i+1)+1)]]
            print(tree_dict)
            if tree_dict[str(i)+"a"]!=list(reversed(tree_dict[str(i)+"b"])):
                return False
    
    return True
print(symmetric([1,2,2,3,4,4,3]))
print(symmetric([1,2,2,None,3,None,3]))
print(symmetric([1,2,2,None,3,3,None]))
print(symmetric([1,2,2,3,None,None,3]))
print(symmetric([1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]))