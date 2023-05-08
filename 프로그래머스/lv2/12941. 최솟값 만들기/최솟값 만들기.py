def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    cum=0
    while A:
        cum+=A.pop()*B.pop()
    return cum