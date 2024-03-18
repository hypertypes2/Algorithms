def solution(s):
    lst=list(map(int,s.split()))
    lst.sort()
    return str(lst[0])+' '+str(lst[-1])