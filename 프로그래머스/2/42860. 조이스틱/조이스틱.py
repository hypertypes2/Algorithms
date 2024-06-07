def solution(name):
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    k = len(string)
    ans = []
    n = len(name)
    
    def DFS(idx,name,cnt):
        #print(idx,name,cnt)
        if name == 'A' * n:
            nonlocal ans
            ans.append(cnt)
            return
        
        now = name[idx]
        
        if now == 'A':
            target_idx = []
            for i in range(len(name)):
                if name[i] != 'A':
                    target_idx.append(i)
            temp = []
            for i in target_idx:
                if idx > i:
                    temp.append((i, min(n-idx+i,idx-i)))
                else:
                    temp.append((i, min(i-idx,n-i+idx)))
            
            temp.sort(key=lambda x:x[1])
            for x,y in temp:
                DFS(x,name,cnt+y)

        else:
            DFS(idx, name[:idx] + 'A' + name[idx+1:],
                cnt+min(string.index(now)-string.index('A'),string.index('Z')-string.index(now)+1))
    
    DFS(0,name,0)
    
    return min(ans)