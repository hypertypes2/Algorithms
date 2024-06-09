import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
time = 0
flag = False

def get_island():
    cnt = 0
    temp = copy.deepcopy(maps)
    for i in range(n):
        for j in range(m):
            if temp[i][j] != 0:
                temp = DFS(i,j,temp)
                cnt += 1
    return cnt

def DFS(x,y,graph):
    graph[x][y] = 0
    for o in range(4):
        nx = x + dx[o]
        ny = y + dy[o]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=0:
            DFS(nx,ny,graph)
            
    return graph

def melt():
    bing = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] !=0:
                sea = 0
                for o in range(4):
                    ni = i +dx[o]
                    nj = j +dy[o]
                    if 0<=ni<n and 0<=nj<m and maps[ni][nj]==0:
                        sea += 1
                bing.append((i,j,sea))
    return bing
        
while True:
    num = get_island()
    if num == 0 :
        time = 0
        break
    if num > 1:
        break

    lst = melt()
    for x,y,c in lst:
        maps[x][y] = max(maps[x][y]-c, 0)
        
    time += 1
    
print(time)