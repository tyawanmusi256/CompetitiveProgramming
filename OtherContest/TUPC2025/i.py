# ベクトルに対する射影が大きい順に1/2,1/4,...の重みづけをする
# ベクトルを回転させたい
from functools import cmp_to_key
import sys
sys = lambda:sys.stdin.readline().rstrip()
mod = 998244353

def sub(p1, p2):
    return (p1[0]-p2[0], p1[1]-p2[1])

# 符号付き面積の2倍
def signed_area_vector(v1, v2):
    area = v1[0]*v2[1] - v2[0]*v1[1]
    return area

# x座標最小の点から反時計回りに頂点を列挙
# p_list = [(x1, y1), (x2, y2), (x3, y3), ...]
def convex_hull_list(p_list):
    assert len(p_list) >= 3
    p_list.sort()
    res = []
    k = 0
    for p in p_list:
        while k >= 2 and signed_area_vector(sub(res[k-1], res[k-2]), sub(p, res[k-1])) <= 0:
            res.pop()
            k -= 1
        res.append(p)
        k += 1
    t = k+1
    for p in p_list[:-1][::-1]:
        while k >= t and signed_area_vector(sub(res[k-1], res[k-2]), sub(p, res[k-1])) <= 0:
            res.pop()
            k -= 1
        res.append(p)
        k += 1
    res.pop()
    return res

# 2倍の面積。座標が整数の場合、この値は整数になる。
def area_convex_hull(p_list):
    res = convex_hull_list(p_list)
    ans = sum(signed_area_vector(res[i], res[(i+1)%len(res)]) for i in range(len(res)))
    return abs(ans)

def half(p):
    """点 p が上半平面 (y > 0 または +x 軸上) に属する場合は 0 を, さもなくば 1 を返す"""
    x, y = p
    if y > 0 or (y == 0 and x >= 0):
        return 0
    else:
        return 1


def cross(a, b):
    """原点から見たベクトル a, b の外積 (符号付き面積) の値を返す"""
    ax, ay = a
    bx, by = b
    return ax * by - ay * bx


def norm2(p):
    """点 p の原点からの距離の二乗を返す"""
    x, y = p
    return x * x + y * y


def angle_cmp(a, b):
    if type(a) == tuple:
        a = a[0]
        b = b[0]
    """点 a, b の偏角と距離に基づく比較関数"""
    ha = half(a)
    hb = half(b)
    if ha < hb:
        return -1
    elif ha > hb:
        return 1

    c = cross(a, b)
    if c > 0:
        return -1
    elif c < 0:
        return 1

    da = norm2(a)
    db = norm2(b)
    if da < db:
        return -1
    elif da > db:
        return 1

    return 0


def is_same_dir(a, b):
    """点 a, b が原点でなく, かつ原点を始点とする同一半直線上にある場合は True を, さもなくば False を返す"""
    if (a[0] == 0 and a[1] == 0) or (b[0] == 0 and b[1] == 0):
        return False
    return half(a) == half(b) and cross(a, b) == 0

def vabs(a):
    # |a|^2
    ax, ay = a
    return ax**2 + ay**2

def syaei(a, b):
    # ベクトルbをaに射影 (a*b/|a|^2)a
    ax, ay = a
    bx, by = b
    t = ax*bx + ay*by
    return t

def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    events = []
    for i in range(n-1):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            vx, vy = x1-x2, y1-y2

            events.append(((-vy, vx), i, j))
            events.append(((vy, -vx), i, j))
    events.sort(key=cmp_to_key(angle_cmp))

    totu_points = []
    v = events[0][0]
    inv2w = [0] * n
    syae = [(syaei(v, points[i]), i) for i in range(n)]
    syae.sort(reverse=1)
    totux = totuy = 0
    for i in range(n):
        t, idx = syae[i]
        x, y = points[idx]
        if i!=n-1:
            totux+=x*pow(2,n-1-(i+1),mod)
            totuy+=y*pow(2,n-1-(i+1),mod)
            inv2w[idx] = i+1
        else:
            totux+=x*pow(2,n-1-i,mod)
            totuy+=y*pow(2,n-1-i,mod)
            inv2w[idx] = i
    totu_points.append((totux%mod,totuy%mod))

    for _, i, j in events:
        ix, iy = points[i]
        jx, jy = points[j]
        totux -= ix * pow(2, n-1 - inv2w[i], mod)
        totux -= jx * pow(2, n-1 - inv2w[j], mod)
        totuy -= iy * pow(2, n-1 - inv2w[i], mod)
        totuy -= jy * pow(2, n-1 - inv2w[j], mod)
        inv2w[i], inv2w[j] = inv2w[j], inv2w[i]
        totux += ix * pow(2, n-1 - inv2w[i], mod)
        totux += jx * pow(2, n-1 - inv2w[j], mod)
        totuy += iy * pow(2, n-1 - inv2w[i], mod)
        totuy += jy * pow(2, n-1 - inv2w[j], mod)
        totu_points.append((totux%mod,totuy%mod))
    ans = area_convex_hull(totu_points) * pow(2, n, mod) % mod
    print(ans)
for _ in range(int(input())):
    solve()