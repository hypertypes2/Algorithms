import sys
import heapq
input=sys.stdin.readline

N=int(input())
heap=[]
for _ in range(N):
    heapq.heappush(heap,int(input()))
    
cum=0
while len(heap)>1:
    x1=heapq.heappop(heap)
    x2=heapq.heappop(heap)
    heapq.heappush(heap,x1+x2)
    cum+=x1+x2

print(cum)