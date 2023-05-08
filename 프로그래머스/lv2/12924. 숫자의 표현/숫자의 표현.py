def solution(n):
    lst=set([i+1 for i in range(n)])
    cnt=0
    for l in lst:
        cum=0
        while cum<n:
            cum+=l
            l+=1
        if cum==n or (n-cum) > l and (n-cum) in lst:
            cnt+=1
    return cnt