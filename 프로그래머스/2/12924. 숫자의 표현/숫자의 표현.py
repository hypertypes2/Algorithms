def solution(n):
    lst=[i for i in range(1,n+1)]
    end,sum,cnt=0,0,0
    for start in range(n):
        while sum<n and end<n:
            sum+=lst[end]
            end+=1
        if sum==n:
            cnt+=1
        sum-=lst[start]
    return cnt