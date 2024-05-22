import sys
sys.setrecursionlimit(10000)

n,l,r = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
status = [[0 for _ in range(n)] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
time = 0

def DFS(x,y,k):
    global cnt,csum
    status[x][y] = k
    csum += maps[x][y]
    cnt += 1
    for o in range(4):
        nx = x + dx[o]
        ny = y + dy[o]
        if 0<=nx<n and 0<=ny<n and status[nx][ny]==0:
            if l<=abs(maps[nx][ny]-maps[x][y])<=r:
                DFS(nx,ny,k)
               
while True:
    status = [[0 for _ in range(n)] for _ in range(n)]
    k=1
    dict = {}
    for i in range(n):
        for j in range(n):
            if status[i][j] == 0:
                cnt,csum = 0,0
                DFS(i,j,k)                    
                dict[k] = csum//cnt
                k += 1

    if k == n**2+1:
        break
    
    for i in range(n):
        for j in range(n):
            if status[i][j] in dict:
                maps[i][j] = dict[status[i][j]]
    time += 1

print(time)