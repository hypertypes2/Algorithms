from itertools import combinations
import string

n,k=map(int,(input().split()))
lst=input().split()

al=string.ascii_lowercase
Mo=set(['a','e','i','o','u'])
Ja=set(al)-Mo

candi=list(combinations(lst,n))
for char in candi[:]:
    M,J=0,0
    for c in char:
        if c in Mo:
            M+=1
        if c in Ja:
            J+=1
    if M<1 or J<2:
        candi.remove(char)

result=[]
for char in candi:
    result.append(''.join(char))
    
ans=[]
for r in result:
    ans.append(''.join(sorted(r)))

for a in sorted(ans):
    print(a)