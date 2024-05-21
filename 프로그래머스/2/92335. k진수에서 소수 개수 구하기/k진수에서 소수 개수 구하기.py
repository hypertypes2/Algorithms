def isprime(A):
    if A == 1:
        return False
    if A == 2:
        return True
    for i in range(2,int(A**0.5)+1):
        if A % i == 0:
            return False
    return True
    
def solution(n,k):
    cnt = 0
    temp = ''
    
    while n >= k:
        temp += str(n%k)
        n //= k
    
    num = (temp + str(n))[::-1].split('0')
    
    for n in num:
        if not n:
            continue
        if isprime(int(n)):
            cnt += 1
    
    return cnt
