from collections import deque

n,k = map(int,input().split())
MAXN = 100000

visit = [False] * (MAXN+1)
cnt = [0] * (MAXN+1)

def BFS(start):
    que = deque()
    que.append(start)
    while que:
        x = que.popleft()
        if x == k:
            print(cnt[k])
            return
        for w,nx in enumerate([2*x, x-1, x+1]):
            if 0>nx or nx>MAXN or visit[nx]:
                continue
                
            if w == 0:
                cnt[nx] = cnt[x]
                que.appendleft(nx)
                visit[nx] = True
            else:
                cnt[nx] = cnt[x] + 1
                que.append(nx)
                visit[nx] = True
BFS(n)