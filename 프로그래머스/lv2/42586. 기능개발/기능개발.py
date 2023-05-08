from collections import deque
def solution(progresses,speeds):
    day=[]
    for p,s in zip(progresses,speeds):
        left=(100-p)/s
        if left!=int(left):
            left=int(left)+1
        day.append(left)
    que=deque(day)

    result=[]
    while que:
        work=que.popleft()
        cnt=1
        if not que:
            result.append(cnt)
            break
        else:
            while work>=que[0]:
                que.popleft()
                cnt+=1
                if not que:
                    break
            result.append(cnt)
                
    return result