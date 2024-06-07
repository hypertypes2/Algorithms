def solution(n):
    DP = [0] * (n+1)
    DP[1] = 1
    DP[2] = 2
    
    for num in range(3,n+1):
        DP[num] = (DP[num-1] + DP[num-2]) % 1000000007
        
    return DP[n] 