import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))
edges=[tuple(map(lambda x:int(x)-1,input().split())) for _ in range(m)]
edge=[[] for _ in range(n)]
for u,v in edges:
    if a[u]<=a[v]:
        edge[u].append(v)
    if a[v]<=a[u]:
        edge[v].append(u)

from heapq import heappop,heappush
visited=set()
dp=[-1]*n
dp[0]=0
s=[(a[0]*(2*n),0)]
while s:
    c,u=heappop(s)
    if u in visited:
        continue
    visited.add(u)
    for v in edge[u]:
        if a[u]==a[v]:
            dp[v]=max(dp[v],dp[u])
        else:
            dp[v]=max(dp[v],dp[u]+1)
        if v not in visited:
            heappush(s,(a[v]*(2*n)-dp[v],v))
print(dp[n-1]+1)