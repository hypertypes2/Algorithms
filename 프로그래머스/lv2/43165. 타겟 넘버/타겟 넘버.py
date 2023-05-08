def solution(numbers, target):
    cnt=0
    def DFS(csum,s):
        if s==len(numbers):
            if csum!=0:
                return
            nonlocal cnt
            cnt+=1
            return
        for next_num in [numbers[s],-numbers[s]]:
            DFS(csum-next_num,s+1)
            
    DFS(target,0)
    return cnt