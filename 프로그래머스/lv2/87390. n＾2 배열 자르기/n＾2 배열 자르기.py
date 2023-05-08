def solution(n, left, right):
    s1,e1=left//n,left%n
    s2,e2=right//n,right%n
    ans=[]
    for idx in range(s1+1,s2+2):
        for i in range(idx-1):
            ans.append(idx)
        while idx<n+1:
            ans.append(idx)
            idx+=1
    return ans[e1:-(n-e2)+1] if -(n-e2)+1!=0 else ans[e1:]