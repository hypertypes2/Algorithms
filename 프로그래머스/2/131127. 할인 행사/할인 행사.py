def solution(want, number, discount):
    cnt=0
    total = []
    for w,n in zip(want,number):
        total += [w] * n
    total.sort()
    
    for i in range(len(discount)-9):
        lst = discount[i:i+10]
        lst.sort()
        if lst == total:
            cnt+=1

    return cnt 