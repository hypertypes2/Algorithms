import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
lst.sort()

flag = False
ans = (3000000001,0,0,0)
for std in range(n-2):
    if flag:
        break
    if std != 0 and lst[std]==lst[std-1]:
        continue        
    left = std + 1
    right = n-1
    while left < right:
        sum = lst[std] + lst[left] + lst[right]
        if abs(sum) < ans[0]:
            ans = (abs(sum),lst[std],lst[left],lst[right])
        if sum < 0:
            left += 1
        elif sum > 0 :
            right -= 1
        else:
            flag =True
            break

print(ans[1],ans[2],ans[3])
