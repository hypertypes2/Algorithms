def solution(begin, target, words):
    ans = 51
    if target not in words:
        return 0
    
    def DFS(begin,words,cnt):
        nonlocal ans
        if begin == target:
            ans = min(ans,cnt)
            return
        for w in words:
            temp = 0
            for c1,c2 in zip(begin,w):
                if c1!=c2:
                    temp+=1
            if temp == 1:
                next = words[:]
                next.remove(w)
                DFS(w,next,cnt+1)
                
    DFS(begin,words,0)
    
    return ans