from collections import defaultdict

def solution(fees, records):
    dict, total = defaultdict(list), defaultdict(int)
    ans = []
    
    for rec in records:
        t, car, _ = rec.split(' ')
        h,m = t.split(':')
        M = int(h) * 60 + int(m)
        if not dict[car]:
            dict[car].append(M)
        else:
            diff = M - dict[car].pop()
            total[car] += diff

    for k,v in dict.items():
        if v:
            total[k] += 1439 - v.pop()
    
    for car,cum in sorted(total.items()):
        base = fees[1] 
        temp = (cum - fees[0]) / fees[2]
        if temp <= 0 :
            ans.append(base)
            continue
        if temp == int(temp):
            base += temp * fees[3]
        else:
            base += (int(temp)+1) * fees[3]
        ans.append(base)
    
    return ans