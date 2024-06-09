n = int(input())
if n==1:
    print(0)
    exit(0)
table = [0] * (n+1)
table[0]=1
table[1]=1
prime = []
k = 0
ans = 0

for num in range(2,int(n**0.5)+1):
    for i in range(num*num,n+1,num):
        table[i] = 1

for i in range(1,n+1):
    if table[i] == 0:
        k += 1
        prime.append(i)

del table

left = 0
right = 0
sum = prime[0]

while left <= right and right < k:
    if sum == n:
        ans += 1
        if right != k-1:
            right += 1
            left += 1
            sum += prime[right]
            sum -= prime[left-1]
        else:
            break
    elif sum < n:
        if right != k-1:
            right += 1
            sum += prime[right]
        else:
            left += 1
            sum -= prime[left-1]
    else:
        left += 1
        sum -= prime[left-1]

print(ans)        