import collections
def solution(s):
    table={')':'(',']':'[','}':'{'}
    cnt=0
    for x in range(len(s)):
        que=collections.deque(s)
        i=0
        while i<x:
            que.append(que.popleft())
            i+=1
            
        stack=[]
        while que:
            char=que.popleft()
            if not stack or char not in table:
                stack.append(char)
            else:
                if stack[-1]==table[char]:
                    stack.pop()
                else:
                    break
                    
        if len(stack)==0:
            cnt+=1
        else:
            continue
            
    return cnt