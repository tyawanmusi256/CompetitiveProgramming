# https://tjkendev.github.io/procon-library/python/graph/topological_sort.html
# V: 頂点数
# G[v] = [w, ...]:
#    有向グラフ上の頂点vから到達できる頂点w
# deg[v]:
#    頂点vに到達できる頂点の数
V, M = map(int, input().split())
G = [[] for i in range(V)]
deg = [0] * V
for _ in range(M):
    x, y = map(int, input().split())
    G[x-1].append(y-1)
    deg[y-1] += 1

from collections import deque
ans = list(v for v in range(V) if deg[v] == 0)
deq = deque(ans)
used = [0] * V

while deq:
    v = deq.popleft()
    for t in G[v]:
        deg[t] -= 1
        if deg[t] == 0:
            deq.append(t)
            ans.append(t)

# ans: トポロジカル順序に並べた頂点
if len(ans) != V:
    exit(print("No"))
for i in range(V-1):
    if not ans[i+1] in G[ans[i]]:
        exit(print("No"))
print("Yes")
x=[0] * V
for i in range(V):
    x[ans[i]] = i+1
print(*x)