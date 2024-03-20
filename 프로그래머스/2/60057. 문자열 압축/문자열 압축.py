def solution(s):
    ans=len(s)
    for i in range(1,len(s)//2+1):
        word=s[:i]
        cnt,temp=1,''
        for j in range(i,len(s),i):
            if word==s[j:j+i]:
                cnt+=1
                continue
            if cnt>=2:
                temp+=(str(cnt)+word)
            else:
                temp+=word
            cnt,word=1,s[j:j+i]
        if cnt>=2:
            temp+=(str(cnt)+word)
        else:
            temp+=word
        ans=min(ans,len(temp))
    return ans