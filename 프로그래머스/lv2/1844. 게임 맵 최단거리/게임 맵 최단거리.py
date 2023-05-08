from collections import deque
def solution(maps):
    def BFS(i,j):
        que=deque()
        que.append((i,j))
        while que:
            i,j=que.popleft()
            for o in range(4):
                ni=i+dx[o]
                nj=j+dy[o]
                if ni<0 or ni>=n or nj<0 or nj>=m or maps[ni][nj]!=1:
                    continue
                que.append((ni,nj))
                maps[ni][nj]=maps[i][j]+1     
        
        return maps[n-1][m-1]
    
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    n,m=len(maps),len(maps[0])
    i,j=0,0
    ans=BFS(i,j)
    return ans if ans!=1 else -1  