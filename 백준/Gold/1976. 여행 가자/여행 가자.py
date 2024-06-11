from collections import defaultdict
n = int(input())
m = int(input())
flag = True

graph = [list(map(int,input().split())) for _ in range(n)]   
path = list(map(int,input().split()))[::-1]
dict = defaultdict(list)

for i in range(n):
    dict[i+1] = graph[i]
    
def DFS(start):
    visit[start] = True
    if visit[target]:
        return
    for idx in range(n):
        if dict[start][idx] == 1 and not visit[idx+1]:
            DFS(idx+1)
    
start = path.pop()
 
while True:
    if not path:
        break
    target = path.pop()
    visit = [False] * (n+1)
    DFS(start)
    if visit[target]:
        start = target
        continue
    flag = False
    break

print("NO") if not flag else print('YES')

