from heapq import heappop, heappush
def dijkstra(starts, edge):
    n = len(edge)
    inf = 10**18
    dist = [inf] * n
    pq = []

    if type(starts) != list:
        starts = [starts]
    for s in starts:
        dist[s] = 0
        heappush(pq, (0, s))

    while pq:
        d, u = heappop(pq)
        if dist[u] < d:
            continue
        for v, w in edge[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))

    return dist