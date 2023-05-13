import sys
sys.setrecursionlimit(10000)
V,E=map(int,sys.stdin.readline().split())
adj=[[] for _ in range(V)]
visit=[False] * (V)
exist=False

def DFS(v,deep):
    global exist
    if deep==5:
        exist=True
        return 
    visit[v]=True
    for e in adj[v]:
        if not visit[e]:
            DFS(e,deep+1)
    visit[v]=False
    
for _ in range(E):
    s,e=map(int,sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)
       
for v in range(V):
    DFS(v,1)
    if exist:
        break

print(int(exist))