def solution(want, number, discount):
    i,cnt=0,0
    while i+10<=len(discount):
        s=discount[i:i+10]
        for w,n in zip(want,number):
            if w not in s or n>s.count(w):
                cnt-=1
                break
        cnt+=1
        i+=1
    return cnt