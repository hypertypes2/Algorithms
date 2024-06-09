import heapq
n = int(input())
lst = list(map(int,input().split()))
lst.sort()

heap = []
left = 0
right = n-1

while left < right:
    sum = lst[left] + lst[right]
    heapq.heappush(heap,(abs(sum),lst[left],lst[right]))
    if sum < 0:
        left += 1
    elif sum > 0 :
        right -= 1
    else:
        break

ans = heapq.heappop(heap)
print(ans[1],ans[2])