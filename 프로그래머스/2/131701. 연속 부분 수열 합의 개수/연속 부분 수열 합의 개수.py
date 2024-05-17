def solution(elements):
    lst = elements * 2 
    L = 1
    value = set()
    while L <= len(elements):
        for i in range(len(lst)-L):
            value.add(sum(lst[i:i+L]))
        L += 1
    return len(value)
        
    