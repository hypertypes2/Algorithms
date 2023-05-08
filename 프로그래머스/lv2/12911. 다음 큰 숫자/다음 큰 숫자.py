def solution(n):
    i=n+1
    cnt=0
    while n>1:
        if n%2==0:
            pass
        else:
            cnt+=1
        n//=2
        
    while True:
        m=i
        cnt2=0
        while m>1:
            if m%2==0:
                pass
            else:
                cnt2+=1
            m//=2
        if cnt2==cnt:
            break
        i+=1
        
    return i