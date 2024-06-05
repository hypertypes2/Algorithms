def solution(rectangle, characterX, characterY, itemX, itemY):
    
    MAXN = 51
    maps = [[0 for _ in range(2*MAXN)] for _ in range(2*MAXN)]
    path = []
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for rec in rectangle:
        for i in range(2*(MAXN-rec[3])+1,2*(MAXN-rec[1])):
            for j in range(2*(rec[0])+1,2*(rec[2])):
                maps[i][j]=1

    for rec in rectangle:
        for i in range(2*(MAXN-rec[3]),2*(MAXN-rec[1])+1):
            for j in range(2*(rec[0]),2*(rec[2])+1):
                if maps[i][j]!=1:
                    path.append((i,j))

    start = (2*(MAXN-characterY), 2*characterX)
    target = (2*(MAXN-itemY), 2*itemX)

    ans = []
    path.sort()

    def DFS(start,path,cnt):
        nonlocal ans,target
        if start == target:
            ans.append(cnt)
            return
        x,y = start
        for o in range(4):
            nx = x + dx[o]
            ny = y + dy[o]
            if ((nx,ny) in path) and maps[nx][ny]!=1:
                temp = path[:]
                temp.remove((x,y))
                DFS((nx,ny),temp,cnt+1)
                
                
    DFS(start,path,0)
    
    return min(ans)//2