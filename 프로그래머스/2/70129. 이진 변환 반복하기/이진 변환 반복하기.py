def binary_trans(W):
    c=0
    temp=''
    for w in W:
        if w!='0':
            c+=1
            temp+=w
    return bin(c)[2:],len(W)-c
    
def solution(s):
    ans,cnt=0,0
    while True:
        if s=='1':
            break
        s,x=binary_trans(s)
        cnt+=x
        ans+=1
    return [ans,cnt]