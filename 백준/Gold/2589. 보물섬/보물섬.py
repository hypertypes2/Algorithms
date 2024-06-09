from collections import deque
n,m = map(int,input().split())
maps = [list(input()) for _ in range(n)]
land = []
ans = 0
#ans = n*m+1
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'L':
            land.append([i,j])

def BFS(i,j):
    temp = [[0 for _ in range(m)] for _ in range(n)]
   # start, end = path[0],path[1]
    cnt = 0
    que = deque()
    que.append((i,j))
    temp[i][j] = 1
    while que:
        x,y = que.popleft()
        for o in range(4):
            nx = x +dx [o]
            ny = y +dy [o]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]=='L' and temp[nx][ny]==0:
                temp[nx][ny] = temp[x][y] + 1
                que.append((nx,ny))
                
    for i in range(n):
        for j in range(m):
            cnt = max(cnt, temp[i][j])
            
    return cnt-1
                

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'L':
            dist = BFS(i,j)
            ans = max(dist,ans)

print(ans)