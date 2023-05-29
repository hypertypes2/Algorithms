import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
lst.sort()
cnt=0
for l in lst:
    path=lst[:]
    path.remove(l)
    
    left,right=0,len(path)-1
    while left<right:
        if path[left]+path[right]==l:
            cnt+=1
            break
        elif path[left]+path[right]>l:
            right-=1
        else:
            left+=1

print(cnt)