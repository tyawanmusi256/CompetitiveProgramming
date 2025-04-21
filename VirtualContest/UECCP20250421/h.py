import sys
sys.setrecursionlimit(10**6)

n=int(input())
a=list(map(lambda x:int(x)-1,input().split()))

# https://tjkendev.github.io/procon-library/python/graph/scc.html
# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

edge = [[] for _ in range(n)]
redge = [[] for _ in range(n)]
for i in range(n):
    edge[i].append(a[i])
    redge[a[i]].append(i)
label, group = scc(n, edge, redge)
G0, GP = construct(n, edge, label, group)
#print(label,group)
#print(G0,GP)
from collections import deque
deg=[0] * label
for i in range(label):
    for j in G0[i]:
        deg[j]+=1
ans = [i for i in range(label) if deg[i]==0]
deq = deque(ans)
used = [0] * label

while deq:
    v = deq.popleft()
    for t in G0[v]:
        deg[t] -= 1
        if deg[t] == 0:
            deq.append(t)
            ans.append(t)

#print(ans)
dp=[0] * label
for i in range(label):
    dp[i] = len(GP[i])
for i in range(label):
    for j in G0[i]:
        dp[j] += dp[i]
#print(dp)
print(sum(dp[i]*len(GP[i]) for i in range(label)))