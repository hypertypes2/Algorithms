def solution(citations):
    lst=[]
    i=0
    while i<=len(citations):
        cnt=0
        for c in citations:
            if c>=i:
                cnt+=1
        if cnt>=i:
            lst.append(i)
        i+=1
    return max(lst)
            
        