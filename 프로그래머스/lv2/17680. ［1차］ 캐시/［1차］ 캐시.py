from collections import deque

def solution(cacheSize, cities):
    que=deque(maxlen=cacheSize)
    cnt=0
    for c in cities:
        c=c.lower()
        if c in que:
            que.remove(c)
            que.append(c)
            cnt+=1
            continue
        que.append(c)
        cnt+=5
    return cnt