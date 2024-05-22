from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]
        
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    print(n,m)
    start = (0,0)
    ans = -1
    
    def BFS(start):
        que = deque([start])
        while que:
            x,y = que.popleft()
            for o in range(4):
                nx = x + dx[o]
                ny = y + dy[o]
                if 0 <=nx<n and 0<=ny<m and maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y] + 1
                    que.append((nx,ny))

        return  maps[n-1][m-1]
    
    ans = BFS(start)
    if ans == 1:
        return -1
    return ans