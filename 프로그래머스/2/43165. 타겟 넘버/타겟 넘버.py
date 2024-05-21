def solution(numbers, target):
    cnt = 0
    def DFS(csum, idx):
        nonlocal cnt
        if idx == len(numbers):
            if csum == target:
                cnt += 1
            return
        DFS(csum+numbers[idx],idx+1)
        DFS(csum-numbers[idx],idx+1)
        
    DFS(0,0)
    return cnt