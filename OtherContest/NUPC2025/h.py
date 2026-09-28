

def verify(grid):
    n = len(grid)
    g = [grid[i//n][i%n]for i in range(n**2)]
    if  sorted(g)!=list(range(n**2)):
        return False
    x = 0
    if n&1:
        x = n**2-1
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp ^= grid[i][j]
        if x != tmp:
            return False
    for j in range(n):
        tmp = 0
        for i in range(n):
            tmp ^= grid[i][j]
        if x != tmp:
            return False
    tmp = 0
    for i in range(n):
        tmp ^= grid[i][i]
    if x != tmp:
        return False
    tmp = 0
    for i in range(n):
        tmp ^= grid[i][n-1-i]
    if x != tmp:
        return False
    return True

map_5x5 = [
    [20, 16, 1, 17, 12],
[13, 10, 22, 2, 11],
[6, 18, 7, 19, 24],
[3, 21, 8, 15, 9],
[4, 5, 0, 23, 14]
]

map_7x7 = [
[0, 47, 11, 10, 5, 28, 7],
[23, 9, 22, 24, 48, 14, 30],
[12, 25, 29, 38, 37, 19, 40],
[32, 26, 31, 6, 27, 41, 33],
[43, 18, 16, 45, 4, 20, 36],
[34, 8, 42, 3, 17, 1, 35],
[2, 15, 21, 44, 46, 13, 39]
]

map_6x6 = [
    [0, 1, 0, 3, 0, 2],
    [2, 3, 1, 2, 3, 1],
    [0, 2, 0, 1, 0, 3],
    [3, 1, 3, 2, 1, 2],
    [0, 2, 0, 1, 0, 3],
    [1, 3, 2, 3, 2, 1],
]

map_6xn = [
    [0, 1],
    [3, 2],
    [0, 1],
    [2, 3],
    [0, 3],
    [1, 2],
]

map_nx6 = [
    [0, 3, 0, 2, 0, 1],
    [2, 1, 3, 1, 3, 2],
]


def solve_even(n):
    if n == 2:
        return False

    a = [[0]*n for _ in range(n)]

    if n % 4 == 0:
        for i in range(n):
            for j in range(n):
                a[i][j] = 4*((i//2)*(n//2) + j // 2)  # 4 の倍数を足す

                x, y = i % 2, j % 2
                if (x, y) == (0, 1):
                    a[i][j] += 2
                if (x, y) == (1, 0):
                    a[i][j] += 3
                if (x, y) == (1, 1):
                    a[i][j] += 1

    else:
        for i in range(n):  # 4 の倍数を先に足しておく
            for j in range(n):
                a[i][j] = 4*((i//2)*(n//2) + j // 2)

        for i in range(6):  # 左上の 6x6
            for j in range(6):
                a[i][j] += map_6x6[i][j]

        for i in range(6):  # 上の 6 x n-6 
            for j in range(6, n):
                a[i][j] += map_6xn[i][j%2]

        for i in range(6, n):  # 左の n-6 x 6
            for j in range(6):
                a[i][j] += map_nx6[i%2][j]

        for i in range(6, n):  # 左下の n-6 x n-6
            for j in range(6, n):
                x, y = i % 2, j % 2
                if (x, y) == (0, 1):
                    a[i][j] += 2
                if (x, y) == (1, 0):
                    a[i][j] += 3
                if (x, y) == (1, 1):
                    a[i][j] += 1

    return a

def solve_odd(n):

    if n == 363 or n == 725:
    #ゆるしてください
        return False

    if n <= 3 or n == 23 or n == 91:
        return False
    if n == 5:
        return map_5x5
    if n == 7:
        return map_7x7

    x = n**2-1
    used = [1]*x

def put_tile(a, rows, cols, base, h=1, v=2):
    # base は4の倍数。base..base+3 を1回ずつ置く。
    r, s = rows
    c, d = cols
    a[r][c], a[r][d] = base, base + h
    a[s][c], a[s][d] = base + v, base + (h ^ v)


def solve_odd(n):
    if n == 1:
        return [[0]]
    if n == 363 or n == 725:
        #ゆるしてください
            return False
    if n == 3 or n == 23 or n == 91:
        return False
    if n == 5:
        return map_5x5
    if n == 7:
        return map_7x7

    # 中央を共有する5x5を組み合わせる
    x = n*n-1
    r = x // 8
    p = 1 << (r.bit_length() - 1)
    k = 1 if n % 4 == 1 else 7
    g = (n - k) // 4

    used = [0]*r
    grid = [[0] * n for _ in range(n)]
    mid = n // 2
    grid[mid][mid] = x
    groups = [[2*i, 2*i+1, n-2-2*i, n-1-2*i] for i in range((n-k)//4)]

    if k == 7:
        w = 1 << ((r^p).bit_length() - 1)
        shift = r ^ p ^ w

        def f(x):
            return shift ^ (x & 1) ^ (w if x & 2 else 0) ^ (p if x & 4 else 0)

        for x in range(6):
            used[f(x)] = 1
        idx = list(range(mid - 3, mid + 4))
        for i in range(7):
            for j in range(7):
                x = map_7x7[i][j]
                grid[idx[i]][idx[j]] = 8*f(x // 8) + x % 8
        peripheral = [i for i in idx if i != mid]

    for group in groups:
        A = r-1
        while not used[A]:
            A -= 1
        B = 0
        while not used[B] and not used[r^A^B]:
            B += 1
        C = r^A^B
        used[A]=used[B]=used[C]=1
        labels = [A, B, C, r]
        idx = [group[0], group[1], mid, group[2], group[3]]
        for i in range(5):
            for j in range(5):
                z = map_5x5[i][j]
                grid[idx[i]][idx[j]] = 8*labels[z // 8] + z % 8

    remaining = [i for i in range(r) if not used[i]]
    rem_id = 0
    if k == 7:
        # 中央の残り6行・列との間を、XOR=0 の4x6、6x4で埋める。
        for group in groups:
            for transpose in (False, True):
                for j, (h, v) in enumerate(((1, 2), (2, 1), (3, 1))):
                    base = 8 * remaining[rem_id]
                    rem_id += 1
                    for i in (0, 2):
                        rows = group[i:i+2]
                        cols = peripheral[2*j:2*j+2]
                        if transpose:
                            put_tile(grid, cols, rows, base + 2*i, v, h)
                        else:
                            put_tile(grid, rows, cols, base + 2*i, h, v)

    for i, r in enumerate(groups):
        for j, c in enumerate(groups):
            if i == j:
                continue
            for u in range(2):
                base = 8 * remaining[rem_id]
                rem_id += 1
                for v in range(2):
                    grid[r[u*2]][c[v*2]] = base + 2*v
                    grid[r[u*2]][c[v*2]+1] = base + 2*v + 1
                    grid[r[u*2]+1][c[v*2]] = base + 2*v + 2
                    grid[r[u*2]+1][c[v*2]+1] = base + 2*v + 3

    return grid


n = int(input())

if n % 2 == 0:
    res = solve_even(n)
    if not res:
        print("No")
        exit()

    print("Yes")
    for row in res:
        print(*row)

    # print(verify(res))
else:
    # bit_l = (n**2-1).bit_length()-1
    # print(n,1<<bit_l)
    grid = solve_odd(n)
    if verify(grid):
        print("Yes")
        for i in grid:
            print(*i)
    else:
        print("No")