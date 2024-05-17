from collections import defaultdict

def solution(clothes):
    
    dict = defaultdict(list)
    
    for v,k in clothes:
        dict[k].append(v)
    
    ans = 1
    for k,v in dict.items():
        ans *= len(v)+1
    
    return ans-1