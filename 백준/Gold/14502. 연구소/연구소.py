import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
temp=[[0 for col in range(m)] for row in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
ans=0

def deepcopy(graph):
    for i in range(n):
        for j in range(m):
            temp[i][j]=graph[i][j]
    return temp

def DFS1(x,y):
    for o in range(4):
        nx=x+dx[o]
        ny=y+dy[o]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if temp[nx][ny]==0:
            temp[nx][ny]=2
            DFS1(nx,ny)
            
def DFS2(w):
    global ans
    if w==3:
        cnt=0
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    DFS1(i,j)
        for i in range(n):
            for j in range(m):
                if temp[i][j]==0:
                    cnt+=1
        ans=max(ans,cnt)        
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                w+=1
                DFS2(w)
                graph[i][j]=0
                w-=1

DFS2(0)
print(ans)