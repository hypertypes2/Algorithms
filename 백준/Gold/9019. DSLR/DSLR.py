import sys
from collections import deque
input = sys.stdin.readline
t= int(input())

for _ in range(t):
    A,B = map(int,input().split())
    n = 10000
    visit = [0] * n
    que = deque()

    que.append(('',A))
    while que:
        k, now = que.popleft()

        if visit[2 * now % n] == 0:
            visit[2 * now % n] = visit[now] + 1
            que.append((k+'D',2 * now % n))
            if visit[B] != 0:
                ans = (k+'D')
                break

        if now == 0:
            new = 9999
        else:
            new = now - 1

        if visit[new] == 0:
            visit[new] = visit[now] + 1
            que.append((k+'S',new))
            if visit[B] != 0:
                ans = (k+'S')
                break

        diff = 4 - len(str(now))
        now = '0' * diff + str(now)

        if visit[int(now[1:]+now[0])] == 0:
            visit[int(now[1:]+now[0])] = visit[int(now)] + 1
            que.append((k+'L', int(now[1:]+now[0])))
            if visit[B] != 0:
                ans = (k+'L')
                break
        if visit[int(now[-1]+now[:-1])] == 0:
            visit[int(now[-1]+now[:-1])] = visit[int(now)] + 1
            que.append((k+'R', int(now[-1]+now[:-1])))
            if visit[B] != 0:
                ans = (k+'R')
                break   
    print(ans)