def solution(word):
    mo = ['A','E','I','O','U']
    dic = []
    
    def DFS(path):
        if len(path) > 5:
            return
        
        dic.append(path[:])
        for i in range(5):
            DFS(path+mo[i])
            
    DFS('')
    
    for idx,w in enumerate(dic):
        if w == word:
            return idx