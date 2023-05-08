import collections
def solution(s):
    stack=[]
    que=collections.deque(s)
    while que:
        char=que.popleft()
        if not stack or stack[-1]!=char:
            stack.append(char)
        else:
            stack.pop()
    return int(len(stack)==0)       