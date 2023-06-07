import sys
input=sys.stdin.readline

n,m=map(int,input().split())
x,y,d=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turnleft():
    global d
    d-=1
    if d==-1:
        d=3
    return d

while True:
    flag=False
    if graph[x][y]==0:
        graph[x][y]=2
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            flag=True
    if not flag:
        nx=x-dx[d]
        ny=y-dy[d]
        if not 0<=nx<n or not 0<=ny<m or graph[nx][ny]==1:
            break
        x,y=nx,ny
        continue
    else:
        turnleft()
        nx=x+dx[d]
        ny=y+dy[d]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            x,y=nx,ny
            continue

cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            cnt+=1

print(cnt)