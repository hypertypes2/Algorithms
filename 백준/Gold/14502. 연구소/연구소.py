import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

loc = []
virus = []
ans = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            loc.append((i,j))
        elif maps[i][j] == 2:
            virus.append((i,j))

def BFS(temp,que):
    while que:
        x,y = que.popleft()
        for o in range(4):
            nx = x + dx[o]
            ny = y + dy[o]
            if 0<=nx<n and 0<=ny<m and temp[nx][ny]==0:
                temp[nx][ny] = 2
                que.append((nx,ny))
    return temp
                 
def DFS(idx,path):
    global ans, maps, virus
    if len(path) == 3:
        wall = path[:]
        temp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                temp[i][j] = maps[i][j]
        for i,j in wall:
            temp[i][j] = 1
            
        que = deque()
        for (x,y) in virus:
            que.append((x,y))    
            
        temp = BFS(temp,que)
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    cnt += 1
        ans = max(ans,cnt)
                    
        return
    
    for i in range(idx, len(loc)):
        path.append((loc[i]))
        DFS(i+1,path)
        path.pop()

DFS(0,[])    
print(ans)