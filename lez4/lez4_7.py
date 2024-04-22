def intersection(nums1: list[int], nums2:list[int])->list[int]:
    intersec=[]
    for i in set(nums1):
        if i in set(nums2):
            intersec.append(i)
    return intersec
num1=[2,2,4,2,1]
num2=[1,1,2,0,2,1,2]
print(intersection(num1,num2))