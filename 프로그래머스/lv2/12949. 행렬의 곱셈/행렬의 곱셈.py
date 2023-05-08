def solution(arr1,arr2):
    lst=[]
    for i in range(len(arr2[0])):
        temp=[]
        for a2 in arr2:
            temp.append(a2[i])
        lst.append(temp)
    
    result=[]
    for a1 in arr1:
        temp=[]
        for i in range(len(lst)):
            cum=0
            for x,y in zip(a1,lst[i]):
                cum+=x*y
            temp.append(cum)
        result.append(temp)
    return result
    