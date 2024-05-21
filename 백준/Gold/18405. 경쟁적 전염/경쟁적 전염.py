import sys
from collections import deque

input = sys.stdin.readline
n,K = map(int,input().split())
test = [list(map(int,input().split())) for _ in range(n)]
S,X,Y = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

temp = []
time = 0

for i in range(n):
    for j in range(n):
        if test[i][j]!=0:
            temp.append((i,j,test[i][j],time))

temp.sort(key=lambda x:x[2])
que = deque(temp)

while que:
    x,y,k,t = que.popleft()
    if t == S:
        break
    for o in range(4):
        nx = x + dx[o]
        ny = y + dy[o]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if test[nx][ny]==0:
            test[nx][ny]=k
            que.append((nx,ny,k,t+1))

print(test[X-1][Y-1])  