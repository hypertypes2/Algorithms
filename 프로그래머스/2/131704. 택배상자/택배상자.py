from collections import deque
def solution(order):
    que = deque(order)
    n = len(order)
    belt = [i+1 for i in range(n)]
    stack = []
    cnt = 0
    idx = 0

    while True:
        if idx >= n:
            pass
        else:
            now = belt[idx]
        if not que:
            break
        need = que[0]
        if not stack:
            if now != need:
                stack.append(now)
                idx += 1
            else:
                que.popleft()
                cnt += 1
                idx += 1
            continue
        else:
            if now == need:
                que.popleft()
                cnt += 1
                idx += 1
                continue
            else:
                if stack[-1] == need:
                    stack.pop()
                    que.popleft()
                    cnt += 1
                    continue
                else:
                    if idx < n:
                        stack.append(now)
                        idx += 1
                        continue
                    break
    return cnt          