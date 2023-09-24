def solution(s):
    cnt,num=0,0
    while s!='1':
        num+=s.count('0')
        s=s.replace('0','')
        c=len(s)
        temp=''
        while c!=1:
            temp+=str(c%2)
            c//=2
        temp+='1'
        s=temp[::-1]
        cnt+=1
    return cnt,num