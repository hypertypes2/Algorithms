import collections
def solution(s):
    que=collections.deque(s)
    stack=[]
    table={')':'('}
    while que:
        q=que.popleft()
        if not stack or q not in table:
            stack.append(q)
        else:
            if stack[-1]==table[q]:
                stack.pop()
            else:
                return False
    return len(stack)==0