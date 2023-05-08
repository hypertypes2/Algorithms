from collections import deque
def solution(priorities,location):
    que=deque([i for i in range(len(priorities))])
    score=deque(priorities)
    
    cnt=0
    while location in que:
        work=que.popleft()
        s=score.popleft()
        if not que:
            cnt+=1
            break
        if s>=max(score):
            cnt+=1
            continue
        else:
            que.append(work)
            score.append(s)
    return cnt
            

        