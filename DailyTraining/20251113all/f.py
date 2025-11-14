n,m=map(int,input().split())
s=[input()for _ in range(n)]
from itertools import permutations
for p in permutations(s):
    ok=True
    for i in range(n-1):
        x=sum(a!=b for a,b in zip(p[i],p[i+1]))
        if x>1:
            ok=False
            break
    if ok:
        print("Yes")
        exit()
print("No")