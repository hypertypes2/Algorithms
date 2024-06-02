import heapq
def solution(scoville,K):
    heap = []
    cnt = 0
    for s in scoville:
        heapq.heappush(heap,s)
    
    while len(heap)>1:
        x1 = heapq.heappop(heap)
        if x1 >= K:
            return cnt
        x2 = heapq.heappop(heap)
        heapq.heappush(heap,(x1+2*x2))
        cnt += 1
    
    if heapq.heappop(heap) >= K:
        return cnt
    return -1