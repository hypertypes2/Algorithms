def lcm(a,b):
    t=a*b
    while b>0:
        a,b=b,a%b
    return t//a    

def solution(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        temp=lcm(temp,arr[i])
    return temp    