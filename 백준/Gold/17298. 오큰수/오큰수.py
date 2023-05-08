import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))

stack=[]
ans=[0]*len(A)
for i,a in enumerate(A):
    while stack and a>A[stack[-1]]:
        ans[stack[-1]]=a
        stack.pop()
    stack.append(i)

for idx in stack:
    ans[idx]=-1

print(*ans)