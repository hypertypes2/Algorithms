def solution(people,limit):
    people.sort(reverse=True)
    cnt=0
    left,right=0,len(people)-1
    while left<right:
        if people[left]+people[right]<=limit:
            cnt+=1
            left+=1
            right-=1
        else:
            left+=1
            cnt+=1
    return cnt+int(left==right)  