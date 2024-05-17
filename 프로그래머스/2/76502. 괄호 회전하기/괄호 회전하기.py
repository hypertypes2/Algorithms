from collections import deque

table = {']':'[', ')':'(', '}':'{'}

def solution(s):
    cnt = 0
    for x in range(len(s)):
        que = deque(s)
        stack = []
        for _ in range(x):
            que.append(que.popleft())
            
        for q in que:
            if stack and q in table and table[q] == stack[-1]:
                stack.pop()
                continue
            stack.append(q)
            
        if not stack:
            cnt+=1
            
    return cnt