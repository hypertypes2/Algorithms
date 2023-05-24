from collections import deque
m,n=map(int,input().split())
graph=[[0 for col in range(m)] for row in range(n)]
for i in range(n):
    S=list(map(int,input().split()))
    for j in range(m):
        graph[i][j]=S[j]
        
di=[0,1,0,-1]
dj=[1,0,-1,0]
flag=True

que=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            que.append((i,j))
            
def BFS():
    while que:
        i,j=que.popleft()
        for o in range(4):
            ni=i+di[o]
            nj=j+dj[o]
            if 0<=ni<n and 0<=nj<m and graph[ni][nj]==0:
                que.append((ni,nj))
                graph[ni][nj]=graph[i][j]+1   
                                 

BFS()

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            flag=False
            pass
if not flag:
    print(-1)
else:
    t=[]
    for g in graph:
        g.sort()
    for sg in graph:
        t.append(sg[-1])        
        
    print(max(t)-1)