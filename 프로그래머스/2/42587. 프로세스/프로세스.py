from collections import deque

def solution(priorities,location):
    idx = deque([i for i in range(len(priorities))])
    que = deque(priorities)
    cnt = 0
    while que:
        now = que.popleft()
        now_idx = idx.popleft()
        if not que:
            return cnt+1
        if now >= max(que):
            cnt += 1
            if now_idx == location:
                return cnt
        else:
            que.append(now)
            idx.append(now_idx)