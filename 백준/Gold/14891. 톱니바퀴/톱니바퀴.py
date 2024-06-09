tops = [[] for _ in range(5)]
for i in range(4):
    tops[i+1] = [int(char) for char in input()]

k = int(input())
    
def touch(top,d):
    diff = []
    if top==1:
        if tops[1][2]!=tops[2][6]:
            diff.append((2,-d))
            if tops[2][2]!=tops[3][6]:
                diff.append((3,d))
                if tops[3][2]!=tops[4][6]:
                    diff.append((4,-d))
    elif top==2:
        if tops[2][6]!=tops[1][2]:
            diff.append((1,-d))
        if tops[2][2]!=tops[3][6]:
            diff.append((3,-d))
            if tops[3][2]!=tops[4][6]:
                diff.append((4,d))
    elif top==3:
        if tops[3][6]!=tops[2][2]:
            diff.append((2,-d))
            if tops[1][2]!=tops[2][6]:
                diff.append((1,d))
        if tops[3][2]!=tops[4][6]:
            diff.append((4,-d))

    elif top==4:
        if tops[4][6]!=tops[3][2]:
            diff.append((3,-d))
            if tops[3][6]!=tops[2][2]:
                diff.append((2,d))
                if tops[2][6]!=tops[1][2]:
                    diff.append((1,-d))
            
    return diff

def turn(top,direction):
    if direction == 1:
        new_top = [top[-1]] + top[:-1]
    else:
        new_top = top[1:] + [top[0]] 
    return new_top

for _ in range(k):
    v,d = map(int,input().split())
    get = touch(v,d)
    tops[v] = turn(tops[v],d)
    for g,o in get:
        tops[g] = turn(tops[g],o)
        
ans = 0
for n in range(1,5):
    ans += tops[n][0] * 2**(n-1)
    
print(ans)