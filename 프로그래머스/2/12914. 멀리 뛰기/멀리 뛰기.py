def solution(n):
    if n<3:
        return n
    dp=[0]*(n+1)
    dp[1],dp[2]=1,2
    
    def fibo(x):
        nonlocal dp
        for x in range(3,n+1):
            dp[x]=(dp[x-1]+dp[x-2])%1234567
    
    fibo(n)
    
    return dp[n]
        
    