n = int(input())
map = [(input().split()) for _ in range(n)]

empty = []
teach = []
stude = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(n):
        if map[i][j] == 'X':
            empty.append((i,j))
        elif map[i][j] == 'T':
            teach.append((i,j))
        else:
            stude.append((i,j))
            
def DFS(wall, idx):
    global ans
    if len(wall) == 3:
        for i,j in wall:
            map[i][j] = 'O'
        for x,y in teach:
            for o in range(4):
                for k in range(1,n+1):
                    nx = x + dx[o] * k
                    ny = y + dy[o] * k
                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        break
                    if map[nx][ny] == 'O':
                        break
                    if map[nx][ny] == 'S':
                        for i,j in wall:
                            map[i][j] = 'X'
                        return
        print('YES')
        exit(0)
 
    for i in range(idx,len(empty)):
        wall.append(empty[i])
        DFS(wall, i+1)
        wall.pop()


DFS([],0)

print("NO")