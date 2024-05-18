def solution(k,dungeons):
    start_list = []
    result = []
    visit = [0]*len(dungeons)
    
    for i in range(len(dungeons)):
        if dungeons[i][0]<=k:
            start_list.append(i)
    
    def DFS(p,now):
        nonlocal visit
        p -= dungeons[now][1]
        visit[now]=1
        for i in range(len(dungeons)):
            if dungeons[i][0]<=p and visit[i]==0:
                DFS(p,i)
        result.append(visit.count(1))
        p += dungeons[now][1]
        visit[now]=0
        return
        
    for start in start_list:
        visit = [0]*len(dungeons)
        DFS(k,start)
            
    return max(result)