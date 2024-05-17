from collections import deque
def solution(people,limit):
    people.sort(reverse=True)
    que=deque(people)
    cnt=0
    while len(que)>1:
        cnt+=1
        x,y=que.popleft(),que.pop()
        if x+y<=limit:
            continue
        que.append(y)
    if que:
        cnt+=1
    return cnt
        
            