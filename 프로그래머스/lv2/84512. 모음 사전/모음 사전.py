def solution(word):
    dic='AEIOU'
    result=[]
    def DFS(k,path):
        if k==6:
            return
        result.append(path[:])
        for i in range(len(dic)):
            DFS(k+1,path+dic[i])
    DFS(0,'')
    return result.index(word)