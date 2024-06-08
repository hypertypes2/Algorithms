def solution(n, times):
    start = n*min(times)//len(times)
    end = n*max(times)//len(times)
    
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for t in times:
            cnt += mid//t
        if cnt < n:
            start = mid +1
        else:
            end = mid - 1
            ans = mid
            
    return ans