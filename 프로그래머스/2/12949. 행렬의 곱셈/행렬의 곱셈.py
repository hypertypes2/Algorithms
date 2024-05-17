def solution(arr1,arr2):
    m,n = len(arr1),len(arr2[0])
    arr = [[0 for _ in range(n)] for _ in range(m)]
    p = len(arr2)
     
    for i in range(m):
        for j in range(n):
            cum=0
            for k in range(p):
                cum += arr1[i][k] * arr2[k][j]
            arr[i][j]=cum
    return arr