import heapq
def dijkstra(start, n, edge):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v in edge[u]:
            if dist[v] > d + 1:
                dist[v] = d + 1
                heapq.heappush(pq, (dist[v], v))
    
    return dist

n,m=map(int,input().split())
edge=[[] for _ in range(n)]
redge=[[] for _ in range(n)]
for i in range(n):
    s=input()
    for j in range(m):
        if s[j]=='1':
            edge[i].append(i+j+1)
            redge[i+j+1].append(i)
dist=dijkstra(0,n,edge)
rdist=dijkstra(n-1,n,redge)
for k in range(1,n-1):
    ans=10**18
    for i in range(max(0,k-m),k):
        for j in edge[i]:
            if j<=k:continue
            ans=min(ans,dist[i]+rdist[j]+1)
    print(ans if ans<10**18 else -1)
