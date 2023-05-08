import heapq
def solution(scoville,K):
    heapq.heapify(scoville)
    cnt=0
    while len(scoville)>1:
        a1=heapq.heappop(scoville)
        a2=heapq.heappop(scoville)
        if a1>=K and a2>=K:
            return cnt
        heapq.heappush(scoville,a1+a2*2)
        cnt+=1
    a=heapq.heappop(scoville)
    return cnt if a>=K else -1