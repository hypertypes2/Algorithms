n = int(input())
a = int(input())

MAP = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(a):
    i,j = map(int,input().split())
    MAP[i-1][j-1] = 2

command = []
t = int(input())
for _ in range(t):
    command.append(list(input().split()))

head_x, head_y = 0,0
tail_x, tail_y = 0,0

MAP[head_x][head_y] = 1
MAP[tail_x][tail_y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
d = 1
cnt = 0
path = [(tail_x, tail_y)]

while True:
    if command and cnt == int(command[0][0]):
        cmd = command.pop(0)[1]
        if cmd=='L':
            d+=3
        else:
            d+=1
        d %= 4
    
    nx = head_x + dx[d]
    ny = head_y + dy[d]
    
    if not(0<=nx<n and 0<=ny<n):
        cnt += 1
        break
    if (nx,ny) in path:
        cnt += 1
        break
        
    if MAP[nx][ny] == 2:
        MAP[nx][ny] = 1
    else:
        MAP[nx][ny] = 1
        MAP[tail_x][tail_y] = 0
        tail_x, tail_y = path.pop(0)
    
    path.append((nx,ny))
    cnt += 1
    head_x,head_y = nx, ny

print(cnt)