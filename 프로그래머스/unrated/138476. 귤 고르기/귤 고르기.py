import collections
def solution(k, tangerine):
    C=collections.Counter(tangerine)
    C=sorted(C.items(),key=lambda x:x[1],reverse=True)
    put=0
    for i in range(len(C)):
        put+=C[i][1]
        if put>=k:
            return i+1
        continue
        