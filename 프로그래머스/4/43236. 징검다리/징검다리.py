def solution(distance, rocks, n):
    rocks.sort()
    start = 1
    end = distance
    ans = 0
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        now = 0
        for r in rocks+[distance]:
            if r-now < mid:
                cnt += 1
            else:
                now = r
        # if distance - r < mid:
        #     cnt += 1
        if cnt <= n:
            ans = max(ans,mid)
            start = mid + 1
        else:
            end = mid - 1
    
    return ans