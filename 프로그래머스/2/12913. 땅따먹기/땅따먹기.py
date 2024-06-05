def solution(land):
    N = len(land)
    DP = [[0 for _ in range(4)] for _ in range(N)]
    DP[0] = land[0][:]
    
    for row in range(1,N):
        for col in range(4):
            prev = DP[row-1][:] 
            max_value = 0
            for idx,score in enumerate(prev):
                if idx == col:
                    continue
                max_value = max(max_value,score) 
                
            DP[row][col] = land[row][col] + max_value
            
    return max(DP[-1])
        