import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[0 for _ in range(m)] for _ in range(n)]
graph2=[[[0,0] for _ in range(m)] for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

for i in range(n):
    s=input()
    for j in range(m):
        graph[i][j]=int(s[j])

def BFS():
    que=deque()
    que.append((0,0,0))
    while que:
        x,y,z=que.popleft()
        if x==n-1 and y==m-1:
            return graph2[x][y][z]
        for o in range(4):
            nx=x+dx[o]
            ny=y+dy[o]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and z==0:
                    nz=z+1
                    graph2[nx][ny][nz]=graph2[x][y][z]+1
                    que.append((nx,ny,nz))
                    continue
                if graph[nx][ny]==0 and graph2[nx][ny][z]==0:
                    graph2[nx][ny][z]=graph2[x][y][z]+1
                    que.append((nx,ny,z))
              
    return -2
      
print(BFS()+1)