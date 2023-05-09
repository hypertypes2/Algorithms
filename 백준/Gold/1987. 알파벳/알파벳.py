import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[0 for col in range(m)] for row in range(n)]
for i in range(n):
    s=input()
    for j in range(m):
        graph[i][j]=ord(s[j])-65

visit=[False]*26
dx=[0,1,0,-1]
dy=[1,0,-1,0]
i,j,cnt=0,0,0

def DFS(i,j,k):
    global cnt
    visit[graph[i][j]]=True
    cnt=max(cnt,k)
    for d in range(4):
        ni=i+dx[d]
        nj=j+dy[d]
        if ni<0 or ni>=n or nj<0 or nj>=m or visit[graph[ni][nj]]:
            continue
        visit[graph[ni][nj]]=True
        DFS(ni,nj,k+1)
        visit[graph[ni][nj]]=False
        
DFS(0,0,1)
print(cnt)