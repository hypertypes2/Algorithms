def solution(fees, records):
    nums=set()
    for r in records:
        nums.add(r.split(' ')[1])
    time,result={},[]
    for num in sorted(nums):
        time[num]=0
        s,e=[],[]
        for r in records:
            if num in r:
                if 'IN' in r:
                    s.append(r.split(' ')[0])
                elif 'OUT' in r:
                    e.append(r.split(' ')[0])
        if len(s)!=len(e):
            e.append('23:59')
        for x,y in zip(s,e):
            S=int(x.split(':')[0])*60+int(x.split(':')[1])
            E=int(y.split(':')[0])*60+int(y.split(':')[1])
            time[num]+=(E-S)

    for num in sorted(nums):
        overtime=max(0,time[num]-fees[0])
        if overtime==0:
            result.append(fees[1])
            continue
        if overtime%fees[2]==0:
            result.append(fees[1]+fees[3]*(overtime//fees[2]))
        else:
            result.append(fees[1]+fees[3]*(overtime//fees[2]+1))
            
    return result       