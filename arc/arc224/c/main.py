import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

for _ in range(int(input())):
    n,m=map(int,input().split())
    edge=[[]for _ in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        a-=1
        b-=1
        edge[a].append(b)
        edge[b].append(a)
    #連結なのありがて～～～
    ans=[-1]*n
    def dfs(node,d):
        ans[node]=d
        for mode in edge[node]:
            if ans[mode]==-1:
                dfs(mode,d+1)
    dfs(0,0)
    print(*ans)
        