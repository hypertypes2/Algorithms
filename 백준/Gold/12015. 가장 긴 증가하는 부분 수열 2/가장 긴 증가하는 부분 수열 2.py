import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))

array = [lst[0]]
 
for l in lst:
    if array[-1] < l:
        array.append(l)
    else:
        start = 0
        end = len(array)-1        
        while start <= end:
            mid = (start+end) // 2
            if array[mid] < l:
                start = mid + 1
            else:
                end = mid - 1
                
        array[start] = l

print(len(array))