import sys
from collections import deque
input=sys.stdin.readline
m,n,h=map(int,input().split())
graph=[[[0 for col in range(m)] for row in range(n)] for height in range(h)]
que=deque()
flag=True
ans=1

di=[1,-1]
dj=[1,0,-1,0]
dk=[0,1,0,-1]

for i in range(h):
    for j in range(n):
        s=list(map(int,input().split()))
        for k in range(m):
            graph[i][j][k]=int(s[k])
            if graph[i][j][k]==1:
                que.append((i,j,k))
            
def BFS():
    while que:
        i,j,k=que.popleft()
        for o in range(4):
            nj=j+dj[o]
            nk=k+dk[o]
            if 0<=nj<n and 0<=nk<m and graph[i][nj][nk]==0:
                graph[i][nj][nk]=graph[i][j][k]+1
                que.append((i,nj,nk))
        for o in range(2):
            ni=i+di[o]
            if 0<=ni<h and graph[ni][j][k]==0:
                graph[ni][j][k]=graph[i][j][k]+1
                que.append((ni,j,k))
                   
if len(que)==n*m*h:
    print(0)
else:
    BFS()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k]==0:
                    flag=False
                    break
                ans=max(ans,graph[i][j][k])
                
    if not flag:
        print(-1)
    else:
        print(ans-1)