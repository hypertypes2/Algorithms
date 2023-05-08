def solution(k,dungeons):
    result,prev_dungeons=[],[]
    def DFS(cum,dungeons):
        if cum<0:
            return
        else:
            result.append(prev_dungeons[:])
        for d in dungeons[:]:
            if d[0]>cum:
                continue
            next_dungeons=dungeons[:]
            next_dungeons.remove(d)
            
            prev_dungeons.append(d)
            DFS(cum-d[1],next_dungeons)
            prev_dungeons.pop()
            
    DFS(k,dungeons)
    result.sort(key=len)
    return len(result.pop())
    