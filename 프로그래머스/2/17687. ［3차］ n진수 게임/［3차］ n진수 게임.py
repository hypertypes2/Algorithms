dic = {'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
def solution(n, t, m, p):
    result = ''
    lst = ''
    
    nums = 0
    while len(lst) < m*(t-1)+p:
        temp = ''
        num = nums
        while num >= n:
            res = str(num % n)
            if res in dic:
                temp += dic[res]
            else:
                temp += res
            num //= n
        x = str(num)
        if x in dic:
            temp += dic[x]
        else:
            temp += x
        temp = temp[::-1]
        for s in temp:
            lst += s     
        nums += 1
    
    for x in range(t):
        result += lst[m*x + p-1]
    return result