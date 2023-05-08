def solution(s):
    a,b=0,0
    while s!='1':
        a+=s.count('0')
        s=s.replace('0','')
        c=len(s)
        ns=''
        while c!=1:
            ns+=str(c%2)
            c//=2
        b+=1
        s=str(c)+ns[::-1]
    return [b,a]