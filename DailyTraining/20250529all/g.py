from itertools import permutations
from math import sqrt
n,s,t=map(int, input().split())
abcd=[list(map(int, input().split())) for _ in range(n)]
ans=10**18
for p in permutations(abcd):
    for bit in range(1<<n):
        nowx=0
        nowy=0
        nowt=0
        for i in range(n):
            if bit & (1 << i):
                a,b,c,d=p[i]
            else:
                c,d,a,b=p[i]
            nowt+=sqrt((nowx-a)**2+(nowy-b)**2)/s
            nowt+=sqrt((c-a)**2+(d-b)**2)/t
            nowx=c
            nowy=d
        ans=min(ans, nowt)
print(ans)