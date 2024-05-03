def visiting_tree(tree:dict[int,list[int]], root:int):
    stack=[root]
    while stack:
        node=stack.pop(0)
        if node:
            left_child, right_child = tree[node]        
            if left_child:
                stack.append(left_child)
            if right_child:
                stack.append(right_child)


def average_tree_level(tree:dict[int,list[int]], root:int):
    stack=[root]
    averages={1:root}
    while stack:
        node=stack.pop(0)
        if node:
            left_child, right_child = tree[node]
            if left_child:
                stack.append(left_child)
            if right_child:
                stack.append(right_child)