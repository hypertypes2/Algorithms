def solution(game_board, table):
    n = len(game_board)
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    puzzle,target = [], []
    ans = 0

    def DFS(i,j):
        table[i][j] = 0
        path.append((i,j))
        for o in range(4):
            ni = i + di[o]
            nj = j + dj[o]
            if 0<=ni<n and 0<=nj<n and table[ni][nj]==1:
                DFS(ni,nj)

    def DFS2(i,j):
        game_board[i][j] = 1
        temp.append((i,j))
        for o in range(4):
            ni = i + di[o]
            nj = j + dj[o]
            if 0<=ni<n and 0<=nj<n and game_board[ni][nj]==0:
                DFS2(ni,nj)

    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                path = []
                DFS(i,j)
                puzzle.append(path)
            if game_board[i][j]==0:
                temp = []
                DFS2(i,j)
                target.append(temp)

    for p in puzzle:
        flag = False
        size = len(p)
        rotate = [p]
        cx,cy = p[0]
        diff = []
        for x,y in p[1:]:
            diff.append((x-cx, y-cy))
        rotate.append([(cx,cy)]+[(cx+ny,cy-nx) for nx,ny in diff])
        rotate.append([(cx,cy)]+[(cx-nx,cy-ny) for nx,ny in diff])
        rotate.append([(cx,cy)]+[(cx-ny,cy+nx) for nx,ny in diff]) 
        for r in rotate:
            r.sort()
        candi = []
        for t in target:
            if len(t) == size:
                candi.append(t)
        if not candi:
            continue
        for c in candi:
            if flag:
                break
            for i in range(len(c)):
                a,b = c[i]
                diff_x,diff_y = a-cx,b-cy
                shift = [(i-diff_x,j-diff_y) for i,j in c]
                shift.sort()
                if shift in rotate:
                    flag = True
                    ans += size
                    target.remove(c)
                    break

    return ans