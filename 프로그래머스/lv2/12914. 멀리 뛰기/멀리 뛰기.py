import math
def solution(n):
    cum=0
    for i in range(n//2,-1,-1):
        x=n-2*i
        cum+=math.comb(x+i,i) 
    return cum%1234567