def solution(elements):
    n=len(elements)
    result=set()
    for l in range(1,n+1):
        i=0
        while i<n:
            if i+l>n:
                result.add(sum(elements[i:n])+sum(elements[:(i+l)%n]))
            else:
                result.add(sum(elements[i:(i+l)]))
            i+=1
    return len(result)