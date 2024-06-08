n = int(input())
lst = list(map(int,input().split()))
lst.sort()

ans = []
start = 0
end = n-1

while start < end:
    sum = lst[start]+lst[end]
    ans.append((lst[start],lst[end],abs(sum)))
    if sum < 0:
        start += 1
    elif sum > 0:
        end -= 1
    else:
        break

ans.sort(key=lambda x:x[2])
x,y,_ = ans[0]
print(x,y)