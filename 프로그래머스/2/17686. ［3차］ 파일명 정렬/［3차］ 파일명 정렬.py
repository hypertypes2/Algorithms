from collections import defaultdict

def solution(files):
    dict = defaultdict(list)
    ans = []
    
    for file in files:
        idx = 0
        HEAD, NUM = '', ''

        while idx < len(file):
            while idx < len(file) and file[idx].isdigit():
                NUM += file[idx]
                idx += 1
            if NUM:
                break
            else:
                HEAD += file[idx]
            idx += 1

        dict[file].append(HEAD.lower())
        dict[file].append(int(NUM))

    dict = sorted(dict.items(), key = lambda x:(x[1][0],x[1][1]))
    
    for k,v in dict:
        ans.append(k)
        
    return ans