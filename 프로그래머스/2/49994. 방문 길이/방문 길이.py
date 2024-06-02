def solution(dirs):
    ans = 0
    now = (0,0)
    path = []
    
    for d in dirs:
        x,y = now
        if d == 'U':
            nx = x
            ny = y+1
        elif d == 'R':
            nx = x+1
            ny = y
        elif d == 'D':
            nx = x
            ny = y-1
        else:
            nx = x-1
            ny = y
        if nx<-5 or nx>5 or ny<-5 or ny>5:
            continue
        if (x,y,nx,ny) not in path and (nx,ny,x,y) not in path:
            ans +=1
            path.append((x,y,nx,ny))
            path.append((nx,ny,x,y))
        now = (nx,ny)
    print(path)    
    return ans