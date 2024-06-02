def solution(n, computers):
    ans = 0
    visit = [False] * n
    
    def DFS(start):
        nonlocal visit
        visit[start] = True
        graph = computers[start]
        for edge in range(n):
            if not visit[edge] and graph[edge]==1:
                DFS(edge)
                
    for start in range(n):
        if not visit[start]:
            DFS(start)
            ans += 1
        
    return ans