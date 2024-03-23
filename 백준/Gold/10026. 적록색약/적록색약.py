import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

n=int(input())
graph1=[[0 for _ in range(n)] for _ in range(n)]
graph2=[[0 for _ in range(n)] for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
cnt1,cnt2=0,0

for i in range(n):
    s=input()
    for j in range(n):
        graph1[i][j]=s[j]
        graph2[i][j]=s[j]

for i in range(n):
    for j in range(n):
        if graph2[i][j]=='G':
            graph2[i][j]='R'
                   
def DFS1(x,y):
    now=graph1[x][y]
    graph1[x][y]='X'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n or graph1[nx][ny]=='X':
            continue
        if graph1[nx][ny]==now:
            DFS1(nx,ny)

def DFS2(x,y):
    now=graph2[x][y]
    graph2[x][y]='X'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n or graph2[nx][ny]=='X':
            continue
        if graph2[nx][ny]==now:
            DFS2(nx,ny)

for i in range(n):
    for j in range(n):
        if graph1[i][j]!='X':
            DFS1(i,j)
            cnt1+=1
            
for i in range(n):
    for j in range(n):
        if graph2[i][j]!='X':
            DFS2(i,j)
            cnt2+=1
print(cnt1,cnt2,sep=' ')