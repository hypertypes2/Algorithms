def solution(n,wires):
    ans = 101

    for i in range(n-1):
        global cnt
        cnt = 0
        graph = [[] for _ in range(n+1)]
        visit = [False] * (n+1)
        result = []

        def DFS(start):
            global cnt
            visit[start]=True
            cnt += 1
            for node in graph[start]:
                if not visit[node]:
                    DFS(node)
            return  
        
        removed = wires[:]
        removed.remove(wires[i])
        
        for edge in removed:
            s,e = edge[0],edge[1]
            graph[s].append(e)
            graph[e].append(s)

        for start in range(1,n+1):
            if not visit[start]:
                cnt = 0
                DFS(start)
                result.append(cnt)
        
        ans = min(ans,abs(result[0]-result[1]))
        
    return ans