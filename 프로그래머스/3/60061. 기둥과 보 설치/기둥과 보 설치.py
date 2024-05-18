def solution(n, build_frame):
    temp = []

    for build in build_frame:
        x,y,a,b = build[0], build[1], build[2], build[3]

        if b == 1: # 설치
            if a==0: # 기둥
                if y==0 or [x-1,y,1] in temp or [x,y,1] in temp or [x,y-1,0] in temp:
                    temp.append([x,y,a])
                else:
                    continue
            else: # 보
                if [x,y-1,0] in temp or \
                [x+1,y-1,0] in temp or  \
                ([x-1,y,1] in temp and [x+1,y,1] in temp):
                    temp.append([x,y,a])
                else:
                    continue
        else:
            act = [x,y,a]
            temp.remove(act)
            flag = True
            for t in temp:
                x,y,a= t[0],t[1],t[2]
                if a==0: # 기둥
                    if y==0 or [x-1,y,1] in temp or [x,y,1] in temp or [x,y-1,0] in temp:
                        continue
                    else:
                        flag=False
                        break
                else: # 보
                    if [x,y-1,0] in temp or \
                    [x+1,y-1,0] in temp or  \
                    ([x-1,y,1] in temp and [x+1,y,1] in temp):     
                        continue
                    else:
                        flag=False
                        break
            if not flag:
                temp.append(act)

    return (sorted(temp,key=lambda x:(x[0],x[1],x[2])))