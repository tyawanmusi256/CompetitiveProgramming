# Dijkstra: 非負重みの有向グラフの最短距離（無向辺は両方向に追加）
# dijkstra(starts, edge, inf=10**18, return_prev=False): 各頂点までの距離のリストを返す。
# starts は始点のindex、または始点のリスト。複数始点はすべて距離0。
# edge[u] は (行き先 v, 重み w) のリスト。頂点は 0-indexed。
# 到達不能は inf。必要な最短距離より大きい inf を指定すること。
# 大きな距離には inf=float("inf") を指定できる。空の始点集合にも対応。
# return_prev=True の場合は (dist, prev) を返す。prev[v] は最短経路上の直前の頂点。
# 始点 s は prev[s] = s、到達不能な頂点は prev[v] = -1。
# 単一始点では O(V + E log(E))、追加メモリ O(V + E)。

# restore_path(prev, goal): 始点から goal までの頂点列を返す（両端を含む）。
# 到達不能なら []、goal が始点なら [goal]。複数始点では最も近い始点の一つから復元。
# prev は dijkstra が返したものを使用。復元は経路長に比例する時間・メモリ。

# 使用例:
# edge = [[(1, 2), (2, 5)], [(2, 1)], []]
# print(dijkstra(0, edge))      # [0, 2, 3]
# print(dijkstra([0, 2], edge)) # [0, 2, 0]
# dist, prev = dijkstra(0, edge, return_prev=True)
# print(restore_path(prev, 2))  # [0, 1, 2]

# 単純重み付き有向グラフの最短経路+復元 N, M <= 5e5
# https://judge.yosupo.jp/submission/406686 / PyPy3 / 1055 ms

from heapq import heapify, heappop, heappush
def dijkstra(starts, edge, inf=10**18, return_prev=False):
    n = len(edge)
    dist = [inf] * n
    prev = [-1] * n if return_prev else None
    pq = []
    if isinstance(starts, int):
        starts = (starts,)
    for s in starts:
        assert 0 <= s < n
        if dist[s] != 0:
            dist[s] = 0
            if prev is not None:
                prev[s] = s
            pq.append((0, s))
    heapify(pq)

    while pq:
        d, u = heappop(pq)
        if dist[u] < d:
            continue
        for v, w in edge[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                if prev is not None:
                    prev[v] = u
                heappush(pq, (nd, v))
    if return_prev:
        return dist, prev
    return dist


def restore_path(prev, goal):
    assert 0 <= goal < len(prev)
    if prev[goal] == -1:
        return []
    path = [goal]
    while prev[goal] != goal:
        goal = prev[goal]
        path.append(goal)
    path.reverse()
    return path
