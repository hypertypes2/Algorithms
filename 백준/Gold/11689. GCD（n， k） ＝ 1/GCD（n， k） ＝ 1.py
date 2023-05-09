N=int(input())
total=N
for p in range(2,int(N**0.5)+1):
    if N%p==0:
        total-=total/p
        while N%p==0:
            N/=p
if N==1:
    print(int(total))
else:
    total-=total/N
    print(int(total))