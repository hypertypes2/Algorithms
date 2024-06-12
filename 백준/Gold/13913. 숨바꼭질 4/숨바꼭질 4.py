from collections import deque
n,k = map(int,input().split())
MAXN = 100000
visit = [-1] * (MAXN+1)
que = deque()

start = n
que.append((start,0))
visit[start] = start
ans = [k]

while que:
    x,cnt = que.popleft()
    if x == k:
        now = x
        while now!=start:
            ans.append(visit[now])
            now = visit[now]
        break
    for nx in [x+1, x-1, 2*x]:
        if 0<=nx<=MAXN and visit[nx] == -1:
            visit[nx] = x
            que.append((nx,cnt+1))
print(cnt)
for a in ans[::-1]:
    print(a,end=' ')