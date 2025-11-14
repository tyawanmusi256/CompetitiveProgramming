# 最短距離をダイクストラで調べてsum(x[0:i])で調べる...という解法
# ↑ある辺の距離が10で、x=[11,11,11,9,11,11...]みたいな場合がきもい
# ある程度リアルタイムにダイクストラを回す必要がある
# 距離が低い順の頂点を持つのではなく、感染しうる距離が短い順の辺を持てばよさそう
# heapで管理すれば辺を見る回数も定数回
# サンプル1きもすぎ
# 一日で複数頂点をまたいで感染する例
# 辺を見る→今日感染したところから残りの感染力をもってダイクストラ→感染力が足りない辺はheapに戻す
# これを繰り返す

from heapq import heappop, heappush
n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    edge[a-1].append((b-1,c))
    edge[b-1].append((a-1,c))
k=int(input())
a=list(map(int,input().split()))
a=[x-1 for x in a]
d=int(input())
x=list(map(int,input().split()))

day=[-1]*n
h=[]
for node in a:
    day[node]=0
for node in a:
    for to,c in edge[node]:
        if day[to]==-1:
            heappush(h,(c,to))
for today in range(d):
    g=[]
    while h and h[0][0]<=x[today]:
        c,to=heappop(h)
        if day[to]!=-1:
            continue
        day[to]=today+1
        heappush(g,(c-x[today],to))
    while g:
        power,node=heappop(g)
        power=-power
        for to,c in edge[node]:
            if c<=power and day[to]==-1:
                day[to]=today+1
                heappush(g,(c-power,to))
            else:
                if day[to]==-1:
                    heappush(h,(c,to))
for i in range(n):
    print(day[i])