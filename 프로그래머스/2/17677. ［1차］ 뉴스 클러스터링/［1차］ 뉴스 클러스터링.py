def solution(str1,str2):
    arr1, arr2 = [], []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append((str1[i]+str1[i+1]).lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            arr2.append((str2[i]+str2[i+1]).lower())
    
    AND = list(set(arr1) & set(arr2))
    OR = list(set(arr1) | set(arr2))
    
    x,y = 0,0
    for a in AND:
        x += min(arr1.count(a),arr2.count(a))
    for o in OR:
        y += max(arr1.count(o),arr2.count(o))
    
    if y == 0:
        ans = 65536
    else:
        ans = (x/y) * 65536
    
    return int(ans)