import collections
T=int(input())

for _ in range(T):
    order=input()
    n=int(input())
    que=collections.deque(input()[1:-1].split(','))
    flag=0
    if n==0:
        que=[]
    for o in order:
        if o=='R':
            flag+=1
        elif o=='D':
            if not que:
                print('error')
                break
            else:
                if flag%2==0:
                    que.popleft()
                else:
                    que.pop()
    else:
        if flag%2==0:
            print('['+','.join(que)+']')
        else:
            que.reverse()
            print('['+','.join(que)+']')