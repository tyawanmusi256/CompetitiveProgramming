n, m = map(int, input().split())
changes = [[] for _ in range(m+1)]
color_cnt = [0] * (n+1)
for i in range(n):
    a, d, b = map(int, input().split())
    changes[d].append((a, -1))
    changes[d].append((b, 1))
    if d == 1:
        color_cnt[b] += 1
    else:
        color_cnt[a] += 1
kind = 0
for cnt in color_cnt:
    if cnt > 0:
        kind += 1
print(kind)
for day in range(2, m+1):
    for color, diff in changes[day]:
        if color_cnt[color] == 0:
            kind += 1
        color_cnt[color] += diff
        if color_cnt[color] == 0:
            kind -= 1
    print(kind)
