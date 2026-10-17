# WarshallFloyd: 重み付き有向グラフの全点対間最短距離
# warshall_floyd(n, edges, inf=float("inf")): dist[u][v] を返す。頂点は 0-indexed。
# edges は (始点 u, 終点 v, 重み w) の列。無向辺は両方向に追加する。
# 負の辺・多重辺・自己ループに対応。到達不能な組は inf。
# 有限の inf を指定する場合は、必要な最短距離より大きい値にする。
# 負閉路があるかは any(dist[v][v] < 0 for v in range(n)) で判定する。
# 負閉路がある場合、影響を受ける組の最短距離は定義されない。
# 計算量 O(n^3 + E)、使用メモリ O(n^2)（E は辺の数）。
#
# 使用例:
# edges = [(0, 1, 2), (1, 2, -1), (0, 2, 5)]
# dist = warshall_floyd(3, edges)
# print(dist[0][2])  # 1
# print(any(dist[v][v] < 0 for v in range(3)))  # False


def warshall_floyd(n, edges, inf=float("inf")):
    assert n >= 0
    dist = [[inf] * n for _ in range(n)]
    for v in range(n):
        dist[v][v] = 0
    for u, v, w in edges:
        assert 0 <= u < n and 0 <= v < n
        if w < dist[u][v]:
            dist[u][v] = w

    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == inf:
                continue
            di = dist[i]
            for j in range(n):
                dkj = dk[j]
                if dkj == inf:
                    continue
                nd = dik + dkj
                if nd < di[j]:
                    di[j] = nd
    return dist
