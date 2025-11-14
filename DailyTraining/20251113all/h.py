import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

ans=0
s=set()
def dfs(v,p):
    global ans
    if ans==10**6:
        return
    ans+=1
    s.add(v)
    for node in edge[v]:
        if node==p:
            continue
        if node in s:
            continue
        dfs(node,v)
    s.remove(v)
dfs(0,-1)
print(ans)