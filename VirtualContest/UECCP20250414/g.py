import sys
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
edge=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
visited=[False]*n
ans=0
def dfs(v,visited):
    global ans
    ans+=1
    if ans>=1000000:
        print(1000000)
        exit()
    visited[v]=True
    for i in edge[v]:
        if not visited[i]:
            dfs(i,visited)
    visited[v]=False
dfs(0,visited)
print(ans)