def solution(sequence, k):
    left, right = 0, 0
    n = len(sequence)
    sum = sequence[0]
    ans = []
    while left <= right and left < n and right < n:
        if sum == k:
            ans.append([left,right,right-left])
            if right == n-1:
                left += 1
                sum -= sequence[left-1]
            else:
                right += 1
                left += 1
                sum = sum + sequence[right] - sequence[left-1]
        elif sum < k:
            if right == n-1:
                break
            right += 1
            sum += sequence[right]
        else:
            left += 1
            sum -= sequence[left-1]
            
    ans.sort(key=lambda x:x[2])
    x,y,_ = ans[0]
    return [x,y]
    
            
                
    