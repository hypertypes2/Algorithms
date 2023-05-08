def solution(n,k):
    temp=''
    while n>k-1:
        temp+=str(n%k)
        n//=k
    num=(temp+str(n))[::-1]
    lst=num.split('0')
    
    def isprime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
        
    ans=0
    for l in lst:
        if len(l)==0 or int(l)==1:
            continue
        if int(l)==2:
            ans+=1
            continue
        if isprime(int(l)):
            ans+=1
    
    return ans
