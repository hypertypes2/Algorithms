stack=[]
def solution(S):
    for s in S:
        if not stack:
            stack.append(s)
        else:
            if stack[-1]==s:
                stack.pop()
            else:
                stack.append(s)
    return int(not stack)