def solution(numbers):
    nums=[int(char) for char in numbers]
    result,prev_nums=[],[]
    cnt=0

    def isprime(n):
        if n==2:
            return True
        if n==0 or n==1 or n%2==0:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def DFS(nums):
        result.append(prev_nums[:])
        if len(nums)==0:
            return
        for n in nums[:]:
            next_nums=nums[:]
            next_nums.remove(n)

            prev_nums.append(n)
            DFS(next_nums)
            prev_nums.pop()

    DFS(nums)

    temp=[]
    for r in result[:]:
        temp.append(''.join(map(str,r)))

    ans=set()
    for t in temp[1:]:
        ans.add(int(t))

    for a in ans:
        if isprime(a):
            cnt+=1
            
    return cnt