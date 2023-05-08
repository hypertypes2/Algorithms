from collections import deque

def solution(x, y, n):
    maxsize=1000000
    visit=[0]*(maxsize+1)
    if x==y:
        return 0
    
    def BFS(x,y):
        que=deque([x])
        while que:
            x=que.popleft()
            if x==y:
                break
            for nx in [x+n,x*2,x*3]:
                if nx>y or nx>maxsize:
                    continue 
                else:
                    if visit[nx]==0:
                        que.append(nx)
                        visit[nx]=visit[x]+1
                        
        return visit[y] if visit[y]!=0 else -1 
    
    return BFS(x,y)
