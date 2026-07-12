#x=100 a=9,8,2
#9:[0,9)*11,[0,2)*1
#8:[0,8)*11,[0,2)*1,[0]*11
#2:[0,2)*45,[0]*11
#計算量足りてる？

from heapq import heappop,heappush
from collections import defaultdict
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    d=defaultdict(int)
    h=[-x]
    d[x]=1
    ans=0
    for i in a:
        while -h[0]>=i:
            p=heappop(h)
            c=d[-p]
            d[-p]=0
            p=-p
            if i-1 not in d:
                heappush(h,-(i-1))
            d[i-1]+=c*(p//i)
            if p%i!=0:
                if p%i not in d:
                    heappush(h,-(p%i))
                d[p%i]+=c
            else:
                ans+=c
    for p in h:
        ans+=d[-p]
    print(ans-1)
