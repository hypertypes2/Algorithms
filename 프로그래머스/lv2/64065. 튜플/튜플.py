import collections
def solution(s):
    que=collections.deque(s[1:-1])
    lst=[]
    while que:
        char=que.popleft()
        if char=='{':
            while '}' not in char:
                char+=que.popleft()          
            lst.append(list(map(int,char[1:-1].split(','))))
    
    lst=sorted(lst,key=lambda x:len(x))
    
    que=collections.deque(lst)
    result=[]
    
    while que:
        tupe=que.popleft()
        for t in tupe:
            if t not in result:
                result.append(t)
                break
                
    return result
        
    