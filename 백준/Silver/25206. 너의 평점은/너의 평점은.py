a,b=0,0
table={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
for _ in range(20):
    score=list(input().split())
    if score[2] not in table:
        continue
    a+=table[score[2]]*float(score[1])
    b+=float(score[1])
print(a/b)