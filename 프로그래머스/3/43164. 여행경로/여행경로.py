from collections import defaultdict
import copy
dict = defaultdict(list)

def solution(tickets):
    ans = []
    for t in tickets:
        dict[t[0]].append(t[1])

    for k,v in dict.items():
        v.sort()
    
    def DFS(start,path,dict):
        nonlocal ans
        if ans:
            return
        if len(path)==len(tickets)+1:
            ans = path[:]
            return
        for edge in dict[start]:
            temp = copy.deepcopy(dict)
            temp[start].remove(edge)
            DFS(edge, path + [edge], temp)
            
    DFS('ICN',['ICN'],dict)
    
    return ans