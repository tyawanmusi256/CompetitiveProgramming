n,m,l=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
aa=[(a[i],i)for i in range(n)]
bb=[(b[i],i)for i in range(m)]
aa.sort(reverse=True)
bb.sort(reverse=True)
bad=set()
for _ in range(l):
    c,d=map(int,input().split())
    bad.add((c-1,d-1))
from heapq import heappush,heappop
q=[]
for i in range(n):
    heappush(q,(-aa[i][0]-bb[0][0],aa[i][1],bb[0][1],i,0))
while q:
    t,ii,jj,i,j=heappop(q)
    if (ii,jj) in bad:
        if j+1<m:
            heappush(q,(-aa[i][0]-bb[j+1][0],aa[i][1],bb[j+1][1],i,j+1))
        continue
    print(-t)
    break