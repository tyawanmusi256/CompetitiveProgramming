h,w=map(int,input().split())
s=[input()for _ in range(h)]
f=lambda i,j:i*w+j
edge=[[]for _ in range(h*w)]
dij=[(-2,-1),(-2,0),(-2,1),
       (-1,-2),(-1,-1),(-1,0),(-1,1),(-1,2),
       (0,-2),(0,-1),(0,0),(0,1),(0,2),
       (1,-2),(1,-1),(1,0),(1,1),(1,2),
       (2,-1),(2,0),(2,1)]
for i in range(h):
    for j in range(w):
        if i<h-1 and s[i+1][j]==".":
            edge[f(i,j)].append((f(i+1,j), 0))
        if j<w-1 and s[i][j+1]==".":
            edge[f(i,j)].append((f(i,j+1), 0))
        if i>0 and s[i-1][j]==".":
            edge[f(i,j)].append((f(i-1,j), 0))
        if j>0 and s[i][j-1]==".":
            edge[f(i,j)].append((f(i,j-1), 0))
        for di,dj in dij:
            if 0<=i+di<h and 0<=j+dj<w:
                edge[f(i,j)].append((f(i+di,j+dj), 1))
from heapq import heappush, heappop
def dijkstra(start):
    dist = [float("inf")] * (h * w)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, cost in edge[u]:
            if dist[v] > d + cost:
                dist[v] = d + cost
                heappush(pq, (dist[v], v))
    return dist
print(dijkstra(0)[f(h-1,w-1)])