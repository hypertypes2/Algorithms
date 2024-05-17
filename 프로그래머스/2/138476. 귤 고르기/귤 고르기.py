from collections import defaultdict
def solution(k, tangerine):
    dic=defaultdict(int)
    cnt=0
    ans=0
    for t in tangerine:
        dic[t]+=1
    
    lst = sorted(dic.items(),key=lambda x:x[1], reverse=True)
    
    for key,value in lst:
        ans+=1
        cnt+=value
        if cnt>=k:
            return ans