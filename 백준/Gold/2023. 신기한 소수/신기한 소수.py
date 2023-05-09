import sys
sys.setrecursionlimit(1000)
N=int(sys.stdin.readline())
answer=[]
S=[2,3,5,7]
def PRIME(n):
    p=2
    while p<=int(n**0.5):
        if n%p==0:
            return False
        p+=1
    return True

def DFS(s):
    if len(str(s))==N:
        answer.append(s)
    else:    
        for e in [1,3,7,9]:
            if PRIME(s*10+e):
                DFS(s*10+e)
            
for s in S:
    DFS(s)
    
for a in answer:
    print(a)