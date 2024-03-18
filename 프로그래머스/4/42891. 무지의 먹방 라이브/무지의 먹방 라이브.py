import heapq
def solution(food_times,k):
    heap=[]
    n=len(food_times)
    cum,temp=0,0
    
    if sum(food_times)<=k:
        return -1
    for i,t in enumerate(food_times):
        heapq.heappush(heap,(t,i+1))
    
    while cum+(heap[0][0]-temp)*n<=k:
        now=heapq.heappop(heap)[0]
        cum+=(now-temp)*n
        n-=1
        temp=now
        
    answer=sorted(heap,key=lambda x:x[1])
    key=(k-cum)%n
    return answer[key][1]