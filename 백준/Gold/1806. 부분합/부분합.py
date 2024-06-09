n,s = map(int,input().split())
lst = list(map(int,input().split()))

ans = 100001
sum = lst[0]
left, right = 0,0

while left<=right and right<n:
    if sum < s:
        if right != n-1:
            right += 1
            sum += lst[right]
        else:
            break
    else:
        ans = min(ans,right-left+1)
        left += 1
        sum -= lst[left-1]

print(0) if ans == 100001 else print(ans)