from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a,b = map(int,input().split())

    stores = []
    for _ in range(n):
        i,j = map(int,input().split())
        stores.append((i,j))
        
    i,j = map(int,input().split())
    end = (i,j)
    stores.append(end)
    visit = [(a,b)]
    que = deque()
    que.append((a,b,20))
    flag =False

    while que:
        if flag:
            break
        x,y,cnt = que.popleft()
        for nx,ny in stores:
            if (nx,ny) not in visit:
                dist = abs(x-nx)+abs(y-ny)
                if dist % 50 == 0:
                    beer = dist//50
                else:
                    beer = dist // 50 + 1
                if beer <= cnt:
                    visit.append((nx,ny))
                    if (nx,ny) == end:
                        flag = True
                        break
                    que.append((nx,ny,20))
                
    print("happy") if end in visit else print("sad")
    