import sys
from collections import deque
input = sys.stdin.readline
bridge, snake = {}, {}
visit = [0] * (101)

n,m = map(int,input().split())

for _ in range(n):
    s,e = map(int,input().split())
    bridge[s] = e
    
for _ in range(m):
    s,e = map(int,input().split())
    snake[s] = e
    
que = deque()
que.append(1)

while que:
    x = que.popleft()
    for dx in range(1,7):
        nx = x + dx
        if nx <= 100 and visit[nx] == 0:
            if nx in bridge:
                nx = bridge[nx]
            if nx in snake:
                nx = snake[nx]
            if visit[nx] == 0:
                visit[nx] = visit[x] + 1
                que.append(nx)
        
print(visit[100])