# https://izumi-math.jp/F_Nakamura/heso/heso3.htm
# 三角形に分割し、重心*面積の総和をもとの多角形の面積で割りたい
# 原点をもとに各頂点の位置ベクトルを考える
# P'の面積は u_j -> v_j, u_j の隣り合う頂点同士の外積を足し合わせると2倍で求まる
n, q = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
s = [0] * (n + 1)
mx = [0] * (n + 1)
my = [0] * (n + 1)
# s[i] ... xy[i-1],xy[i]の情報が含まれる
for i in range(n):
    j = (i + 1) % n
    tmp = xy[i][0] * xy[j][1] - xy[j][0] * xy[i][1]
    # 面積2倍
    # 後でまた面積で割るからどうでもいい
    s[i + 1] = s[i] + tmp
    # 重心3倍
    mx[i + 1] = mx[i] + (xy[i][0] + xy[j][0]) * tmp
    my[i + 1] = my[i] + (xy[i][1] + xy[j][1]) * tmp
for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if u < v:
        s_ans = s[v] - s[u]
        mx_ans = mx[v] - mx[u]
        my_ans = my[v] - my[u]
    else:
        s_ans = s[n] - s[u] + s[v]
        mx_ans = mx[n] - mx[u] + mx[v]
        my_ans = my[n] - my[u] + my[v]
    ux, uy = xy[u]
    vx, vy = xy[v]
    s_ans += vx * uy - ux * vy
    mx_ans += (ux + vx) * (vx * uy - ux * vy)
    my_ans += (uy + vy) * (vx * uy - ux * vy)
    print(mx_ans / (s_ans * 3.0), my_ans / (s_ans * 3.0))