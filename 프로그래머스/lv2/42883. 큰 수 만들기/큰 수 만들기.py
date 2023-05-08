def solution(number,k):
    cnt=0
    stack=[]
    while cnt<k:
        for i,n in enumerate(number):
            if stack:
                while stack and cnt<k and int(n)>int(number[stack[-1]]):
                    stack.pop()
                    cnt+=1
            stack.append(i)    
        while stack and cnt<k:
            stack.pop()
            cnt+=1
            
    ans=''        
    for idx in stack:
        ans+=number[idx]    
    return ans