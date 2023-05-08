def solution(n):
    dic={0:0,1:1}
    i=2
    while i<=n:
        dic[i]=dic[i-1]+dic[i-2]
        i+=1
    return dic[n]%1234567