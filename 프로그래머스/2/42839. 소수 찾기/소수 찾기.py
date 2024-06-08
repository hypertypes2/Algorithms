def isprime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    cnt = 0
    dict = {}
    n = len(numbers)
    visit = [False] * n

    def DFS(char):
        nonlocal cnt
        if not char:
            pass
        else:
            if len(char) > n:
                return
            if isprime(int(char)):
                if int(char) not in dict:
                    cnt += 1
                    dict[int(char)] = 1
        for idx in range(n):
            if not visit[idx]:
                visit[idx] = True
                DFS(char + numbers[idx])
                visit[idx] = False
            
    DFS('')

    return cnt
    
    
    
    