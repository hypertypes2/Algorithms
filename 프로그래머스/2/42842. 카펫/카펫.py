def solution(brown,yellow):
    temp=[]
    n=brown+yellow
    for i in range(2,int((n)**0.5)+1):
        if n%i==0:
            a=n//i
            b=i
            temp.append((a,b))
    while temp:
        x,y=temp.pop()
        if (x-2)*(y-2)==yellow:
            return [x,y]
