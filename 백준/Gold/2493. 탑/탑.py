import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

answer=[0]*n
stack=[]
for i,l in enumerate(lst):
    while stack:
        if lst[stack[-1]]<=l:
            stack.pop()
        else:
            answer[i]=stack[-1]+1
            break
    stack.append(i)
        
print(*answer)