n=int(input())
edge=[[]for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
g=[[]for _ in range(n)]
for i in range(n):
    l=len(edge[i])
    for node in edge[i]:
        g[node].append(l)
ans=0
for i in range(n):
    g[i].sort(reverse=1)
    for j in range(len(g[i])):
        if ans<(j+1)*g[i][j]:
            ans=(j+1)*g[i][j]
print(n-ans-1)