def solution(brown, yellow):
    for i in range(1,int(yellow**0.5)+1):
        if yellow%i==0:
            x,y=max(yellow//i,i)+2,min(yellow//i,i)+2
            if 2*x+2*y-4==brown:
                return [x,y]
            continue

