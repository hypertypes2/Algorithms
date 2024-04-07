def solution(n):
    ans=n+1
    while True:
        if bin(ans).count('1')==bin(n).count('1'):
            break
        ans+=1
    return ans