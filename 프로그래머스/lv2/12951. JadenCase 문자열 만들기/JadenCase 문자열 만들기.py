def solution(s):
    ans=[]
    for l in s.split(' '):
        if ' ' in l:
            continue
        else:
            ans.append(l[:1].upper()+l[1:].lower())
    return ' '.join(ans)