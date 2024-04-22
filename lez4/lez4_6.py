def move_zeroes(num:list[int]):
    for i in range(len(num)-1):
        if num[i]==0:
            num.append(0)
            num.pop(i)

num=[0,2,0,3,0,3,4,5]
move_zeroes(num)
print(num)