def solution(word):
    mo = 'AEIOU'
    dic = []

    def DFS(path):
        dic.append(path)
        if len(path) == 5:
            return
        for idx in range(len(mo)):
            DFS(path+mo[idx])

    DFS('')
    
    for ans,char in enumerate(dic):
        if char == word:
            return ans