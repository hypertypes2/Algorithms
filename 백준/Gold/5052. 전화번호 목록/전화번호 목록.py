import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    flag=True
    lst=[]
    for _ in range(n):
        lst.append(input().rstrip())
    lst.sort()
    for a,b in zip(lst,lst[1:]):
        if b.startswith(a):
            flag=False
            break
    print('YES') if flag else print('NO')