from collections import defaultdict
dict = defaultdict(list)

def solution(genres, plays):
    ans = []
    total = defaultdict(int)
    idx = 0
    for g,p in zip(genres,plays):
        dict[g].append((idx,p))
        total[g] += p
        idx += 1
        
    total = sorted(total.items(), key=lambda x:-x[1])
    #dict = sorted(dict.items(), key=lambda x:-x[1][1])
    
    for g,t in total:
        temp = dict[g]
        if len(temp)==1:
            ans.append(temp[0][0])
        else:
            temp.sort(key=lambda x:-x[1])
            ans.append(temp[0][0])
            ans.append(temp[1][0])
    
    return ans