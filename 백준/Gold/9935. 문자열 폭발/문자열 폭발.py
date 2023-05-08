import sys
from collections import deque
input=sys.stdin.readline
s=input().rstrip()
w=input().rstrip()

que=deque(s)
stack=[]
while que:
    stack.append(que.popleft())
    if ''.join(stack[-len(w):])==w:
        for i in range(len(w)):
            stack.pop()
    
print(''.join(stack)) if stack else print('FRULA')