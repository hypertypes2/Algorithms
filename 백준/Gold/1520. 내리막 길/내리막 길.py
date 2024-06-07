import sys
sys.setrecursionlimit(10000)
n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
DP = [[-1 for _ in range(m)] for _ in range(n)]

def DFS(x,y):
    if (x,y) == (n-1,m-1):
        return 1
    if DP[x][y] != -1:
        return DP[x][y]
    
    DP[x][y] = 0
     
    for o in range(4):
        nx = x + dx[o]
        ny = y + dy[o]
        if 0<=nx<n and 0<=ny<m and maps[nx][ny]<maps[x][y] :
            DP[x][y] += DFS(nx,ny) 

    return DP[x][y]
            
print(DFS(0,0))