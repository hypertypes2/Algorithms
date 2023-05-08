def solution(str1,str2):
    str1,str2=str1.lower(),str2.lower()
    A,B=[],[]
    for i in range(len(str1)-1):
        A.append(str1[i:i+2])
    for i in range(len(str2)-1):
        B.append(str2[i:i+2]) 
    for a in A[:]:
        if not a.isalpha():
            A.remove(a)
    for b in B[:]:
        if not b.isalpha():
            B.remove(b)
    if not A and not B:
        J=1
    else:        
        x=0    
        for a in set(A):
            if a in B:
                x+=min(A.count(a),B.count(a))
        J=x/(len(A)+len(B)-x)
        
    return int(2**16*J)