import sys
input = sys.stdin.readline

n,m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]
house, chic, remain = [], [], []
total = 999999

for i in range(n):
    for j in range(n):
        if city[i][j]==2:
            chic.append((i,j))
        elif city[i][j]==1:
            house.append((i,j))

def DFS(start,path):
    if len(path) == m:
        remain.append(path[:])
        return
    for i in range(start,len(chic)):
        path.append(chic[i])
        DFS(i+1,path)
        path.pop()

DFS(0,[])

for comb in remain:
    cum = 0
    for x,y in house:
        dist = 999999
        for i,j in comb:
            dist = min(dist,abs(x-i)+abs(y-j))
        cum += dist
    total = min(total,cum)

print(total)