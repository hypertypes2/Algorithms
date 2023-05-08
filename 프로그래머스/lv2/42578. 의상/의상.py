def solution(clothes):
    dic={c[1]:0 for c in clothes}
    for c in clothes:
        dic[c[1]]+=1
    cum=1
    for k,v in dic.items():
        cum*=v+1
    return cum-1