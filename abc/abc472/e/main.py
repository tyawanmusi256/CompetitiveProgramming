# 二部グラフ
import sys
sys.setrecursionlimit(10**6)
for _ in range(int(input())):
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    color = [-1]*n
    color[0] = 0
    s = [0]
    cycle = []
    for node in s:
        for mode in edge[node]:
            if color[mode] == -1:
                color[mode] = 1^color[node]
                s.append(mode)
            elif color[mode] == color[node]:
                if len(cycle) == 0:
                    cycle.append(node)
                    cycle.append(mode)
    if len(cycle) == 0:
        print(-1)
        continue
    parent = [-1]*n
    visited = [False]*n
    s = [cycle[0]]
    visited[cycle[0]] = True
    for node in s:
        if len(cycle) >= 3:
            break
        for mode in edge[node]:
            if color[mode] == color[node]:
                continue
            if mode == cycle[1]:
                while node != cycle[0]:
                    cycle.append(node)
                    node = parent[node]
                break
            if not visited[mode]:
                parent[mode] = node
                visited[mode] = True
                s.append(mode)
    print(len(cycle))
    print(*[x+1 for x in cycle])
