from collections import deque

N,L=map(int,input().split())
lst=list(map(int,input().split()))

que=deque()
for i,n in enumerate(lst):
    while que and que[-1][1]>n:
        que.pop()
    que.append((i,n))
    if que[0][0]<=i-L:
        que.popleft()
    print(que[0][1],end=' ')