import sys
input = sys.stdin.readline
h,w=map(int,input().split())
s = [input() for _ in range(h)]
edge = [[] for _ in range(h*w)]
import heapq
def dijkstra(s, edge):
    n=len(edge)
    dist=[float('inf')]*n
    dist[s]=0
    q=[(0,s)]
    while q:
        d,x=heapq.heappop(q)
        if dist[x]<d:
            continue
        for y,c in edge[x]:
            if dist[y]>d+c:
                dist[y]=d+c
                heapq.heappush(q,(dist[y],y))
    return dist

d=lambda x,y: x*w+y
for i in range(h):
    for j in range(w):
        if i!=0:
            if s[i-1][j]==".":
                edge[d(i,j)].append((d(i-1,j),0))
            else:
                edge[d(i,j)].append((d(i-1,j),1))
            if i!=1:
                if s[i-2][j]=="#":
                    edge[d(i,j)].append((d(i-2,j),1))
        if j!=0:
            if s[i][j-1]==".":
                edge[d(i,j)].append((d(i,j-1),0))
            else:
                edge[d(i,j)].append((d(i,j-1),1))
            if j!=1:
                if s[i][j-2]=="#":
                    edge[d(i,j)].append((d(i,j-2),1))
        if i!=h-1:
            if s[i+1][j]==".":
                edge[d(i,j)].append((d(i+1,j),0))
            else:
                edge[d(i,j)].append((d(i+1,j),1))
            if i!=h-2:
                if s[i+2][j]=="#":
                    edge[d(i,j)].append((d(i+2,j),1))
        if j!=w-1:
            if s[i][j+1]==".":
                edge[d(i,j)].append((d(i,j+1),0))
            else:
                edge[d(i,j)].append((d(i,j+1),1))
            if j!=w-2:
                if s[i][j+2]=="#":
                    edge[d(i,j)].append((d(i,j+2),1))

si,sj,gi,gj=map(int,input().split())
dist = dijkstra(d(si-1,sj-1), edge)
print(dist[d(gi-1,gj-1)])