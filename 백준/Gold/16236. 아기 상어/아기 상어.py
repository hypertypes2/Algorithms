from collections import deque
import copy
n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            x,y = (i,j)

maps[x][y] = 0
size = 2
time = 0
ate = 0


def check(x,y):
    target = []
    next_go = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] < size and maps[i][j]!=0:
                target.append((i,j))
                
    if not target:
        return None
    
    temp = copy.deepcopy(maps)
    for i in range(n):
        for j in range(n):
            if maps[i][j] > size:
                temp[i][j] = -1
            else:
                temp[i][j] = 0

    temp[x][y]=0
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for o in range(4):
            nx = x + dx[o]
            ny = y + dy[o]
            if 0<=nx<n and 0<=ny<n and temp[nx][ny]==0:
                temp[nx][ny] = temp[x][y] + 1
                que.append((nx,ny))
    

    for i,j in target:
        if temp[i][j]!=0:
            next_go.append((i,j,temp[i][j]))
    if not next_go:
        return None
    next_go.sort(key=lambda x:(x[2],x[0],x[1]))

    return next_go[0]

while True:
    go = check(x,y)
    if not go:
        break
    x,y,t = go
    maps[x][y]=0
    time += t
    ate += 1
    if ate == size:
        size += 1
        ate = 0
    
print(time)