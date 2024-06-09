def solution(m, n, puddles):
    DP = [[-1 for _ in range(m)] for _ in range(n)]
    dx = [1,0]
    dy = [0,1]
    num = 1000000007
    
    def DFS(x,y):
        if x == n-1 and y == m-1:
            return 1
        if DP[x][y] != -1:
            return DP[x][y]
        
        DP[x][y] = 0
        
        for o in range(2):
            nx = x + dx[o]
            ny = y + dy[o]
            if 0<=nx<n and 0<=ny<m and [ny+1,nx+1] not in puddles:
                DP[x][y] += DFS(nx,ny) % num
                
        return DP[x][y] % num
    
    ans = DFS(0,0)

    return ans