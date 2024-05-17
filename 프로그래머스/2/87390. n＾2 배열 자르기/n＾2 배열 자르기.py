def solution(n, left, right):
    array = []
    i1,j1 = left // n, left % n
    i2, j2 = right // n, right % n 
      
    for i in range(i1,i2+1):
        for j in range(n):
            array.append(max(i,j)+1)
            
    if -n+1+j2==0:
        return array[j1:]
    
    return array[j1:-n+1+j2] 