def solution(msg):    
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {}
    idx = 0
    ans = []
    
    for i,s in enumerate(string):
        dic[s]=i+1
        
    while idx < len(msg):
        temp = msg[idx]
        while temp in dic and idx < len(msg)-1:
            idx += 1
            temp += msg[idx]
        if temp in dic:
            ans.append(dic[temp])
            return ans
        else:
            ans.append(dic[temp[:-1]])
            dic[temp]=len(dic)+1
    return ans