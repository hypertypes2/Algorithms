from collections import deque
def solution(progresses,speeds):
    que = deque()
    ans = []
    for p,s in zip(progresses,speeds):
        if (100-p)%s==0:
            que.append((100-p)/s)
            continue
        que.append((100-p)//s+1)
    while que:
        now = que.popleft()
        cnt = 1
        if not que:
            ans.append(cnt)
            break
        while que and que[0] <= now:
            que.popleft()
            cnt+=1
        ans.append(cnt)

    return ans