import sys
sys.setrecursionlimit(10**6)
n=int(input())
d=list(map(int, input().split()))
edge=[[]for _ in range(n)]
for i in range(n-1):
    a,b,c=map(int, input().split())
    if d[a-1] == 0 or d[b-1] == 0:
        c=0
    edge[a-1].append((b-1, c))
    edge[b-1].append((a-1, c))

dp=[[0]*2 for _ in range(n)]
#dp[node][0]...1本余裕あり　[1]...d_node本全部使った
#親から見てdp[child][0]+costかdp[child][1]の選択
#前者を選べる回数はd_parentを考慮
def dfs(parent, node):
    ans=0
    dif=[]
    for child, cost in edge[node]:
        if child == parent:
            continue
        dfs(node, child)
        ans+=dp[child][1]
        dif.append(max(dp[child][0]+cost - dp[child][1],0))
    dif.sort(reverse=True)
    dp[node][0]=ans+sum(dif[:min(len(dif), d[node]-1)])
    dp[node][1]=ans+sum(dif[:min(len(dif), d[node])])
dfs(-1, 0)
print(max(dp[0]))
        