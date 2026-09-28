import sys
sys.setrecursionlimit(10**6)
n=int(input())
a=list(map(int,input().split()))
edge=[[] for _ in range(n)]
for i in range(n-1):
    u,v=map(int,input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)

lis=[10**10]*n
lis[0]=a[0]
ans=[-1]*n
ans[0]=1

from bisect import bisect_left as bl
def dfs(s,p,lis):
    ind=bl(lis,a[s])
    tmp=lis[ind]
    lis[ind]=a[s]
    ans[s]=bl(lis,10**10)
    for i in edge[s]:
        if i==p:
            continue
        dfs(i,s,lis)    
    lis[ind]=tmp
    return

dfs(0,-1,lis)
for i in ans:
    print(i)