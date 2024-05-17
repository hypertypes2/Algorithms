import sys
input = sys.stdin.readline
N,C = map(int,input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

start = 1
end = lst[-1] - lst[0]
while start <= end:
    mid = (start+end)//2
    now = lst[0]
    cnt = 1
    for i in range(1,N):
        if lst[i]-now >= mid:
            cnt+=1
            now = lst[i]
    if cnt < C:
        end  = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)