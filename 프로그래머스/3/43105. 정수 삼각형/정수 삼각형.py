def solution(triangle):
    n = len(triangle)
    DP = []
    for i in range(n):
        DP.append(triangle[i])
        
    for i in range(1,n):
        for j in range(i+1):
            if j == 0:
                DP[i][j] += DP[i-1][0]
            elif j == i:
                DP[i][j] += DP[i-1][j-1]
            else:
                DP[i][j] += max(DP[i-1][j-1],DP[i-1][j])
    
    return max(DP[n-1])    