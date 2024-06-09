def solution(routes):
    routes.sort(key=lambda x:x[1])
    ans = 0
    path = routes[:]
    idx = 0
    while idx < len(routes):
        now = routes[idx][1]
        while path[idx][0] <= now <= path[idx][1]:
                idx+=1
                if idx == len(routes):
                    break
        ans += 1
        
        
    return ans