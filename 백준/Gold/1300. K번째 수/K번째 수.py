n=int(input())
k=int(input())

start=1
end=k 

while start<=end:
    mid=(start+end)//2
    sum=0
    for i in range(1,n+1):
        d=mid//i
        if d>n:
            d=n
        sum+=d
    if sum>=k:
        sol=mid
        end=mid-1
    else:
        start=mid+1
        
print(sol)