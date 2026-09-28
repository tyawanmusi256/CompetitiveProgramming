# LazySegmentTree: 0-indexed、区間は半開区間 [l, r)
# LazySegmentTree(n, p, x_unit, m_unit, f, g, h, power_of_two=False)
# p は長さ n のリスト。構築 O(n)、各操作 O(log n)（f/g/h が O(1) の場合）。
# f(a, b): 左右の集約。結合律を満たし、x_unit は単位元。
# g(a, x): 集約値 a に操作 x を適用。区間長が必要なら a に持たせる。
# h(old, new): old の後に new を適用する合成。m_unit は恒等操作。
# f/g/h は引数を変更しないこと。遅延値は m_unit と == で比較できること。
# update(l, r, x): [l, r) に x を適用。空区間は何もしない。
# query(l, r): [l, r) の集約。空区間は x_unit。get(i): a[i]。
# max_right(l, check) / min_left(r, check): 条件を満たす最大の右端 / 最小の左端。
# 境界探索には power_of_two=True を指定。
# check は副作用なし・区間拡大に対して単調、check(x_unit) は真。
# 0 <= l <= r <= n。max_right(n, check) = n、min_left(0, check) = 0。

# 使用例（区間加算・区間和、値は (和, 長さ)）:
# f = lambda a, b: (a[0] + b[0], a[1] + b[1])
# g = lambda a, x: (a[0] + x * a[1], a[1])
# h = lambda old, new: old + new
# seg = LazySegmentTree(3, [(1, 1), (2, 1), (3, 1)], (0, 0), 0, f, g, h, True) # [1, 2, 3]
# seg.update(0, 2, 4)                               # [5, 6, 3]
# print(seg.query(1, 3)[0])                         # 9
# print(seg.max_right(0, lambda a: a[0] <= 11))     # 2
# print(seg.min_left(3, lambda a: a[0] <= 9))       # 1

# 区間アフィン変換・区間和クエリ N, Q <= 2e5
# 提出: https://judge.yosupo.jp/submission/406683 / AC / PyPy3 / 1263 ms


class LazySegmentTree:
    __slots__ = ["n0", "n", "seg", "x_unit", "m_unit", "f", "g", "h", "lazy"]

    def __init__(self, n, p, x_unit, m_unit, f, g, h, power_of_two=False):
        assert n >= 0 and len(p) == n
        self.n0 = n
        self.n = 1 << (max(1, n) - 1).bit_length() if power_of_two else max(1, n)
        self.seg = [x_unit] * self.n + p.copy() + [x_unit] * (self.n - n)
        self.x_unit = x_unit
        self.m_unit = m_unit
        self.f = f
        self.g = g
        self.h = h
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.f(self.seg[i << 1], self.seg[(i << 1) + 1])
        self.lazy = [m_unit] * (self.n * 2)

    def update(self, l, r, x):
        seg = self.seg
        lazy = self.lazy
        f = self.f
        g = self.g
        h = self.h
        m_unit = self.m_unit
        assert 0 <= l <= r <= self.n0
        if l == r or x == m_unit:
            return
        l += self.n
        r += self.n
        ll = l // (l & -l)
        rr = r // (r & -r) - 1
        for shift in range(ll.bit_length() - 1, 0, -1):
            i = ll >> shift
            if lazy[i] == m_unit:
                continue
            lazy[i << 1] = h(lazy[i << 1], lazy[i])
            lazy[(i << 1) + 1] = h(lazy[(i << 1) + 1], lazy[i])
            seg[i] = g(seg[i], lazy[i])
            lazy[i] = m_unit
        for shift in range(rr.bit_length()-1, 0, -1):
            i = rr >> shift
            if lazy[i] == m_unit:
                continue
            lazy[i << 1] = h(lazy[i << 1], lazy[i])
            lazy[(i << 1) + 1] = h(lazy[(i << 1) + 1], lazy[i])
            seg[i] = g(seg[i], lazy[i])
            lazy[i] = m_unit
        while l < r:
            if l & 1:
                lazy[l] = h(lazy[l], x)
                l += 1
            if r & 1:
                r -= 1
                lazy[r] = h(lazy[r], x)
            l >>= 1
            r >>= 1
        while ll > 1:
            ll >>= 1
            left = ll << 1
            right = left | 1
            a = seg[left] if lazy[left] == m_unit else g(seg[left], lazy[left])
            b = seg[right] if lazy[right] == m_unit else g(seg[right], lazy[right])
            seg[ll] = f(a, b)
            lazy[ll] = m_unit
        while rr > 1:
            rr >>= 1
            left = rr << 1
            right = left | 1
            a = seg[left] if lazy[left] == m_unit else g(seg[left], lazy[left])
            b = seg[right] if lazy[right] == m_unit else g(seg[right], lazy[right])
            seg[rr] = f(a, b)
            lazy[rr] = m_unit

    def query(self, l, r):
        seg = self.seg
        lazy = self.lazy
        f = self.f
        g = self.g
        h = self.h
        m_unit = self.m_unit
        assert 0 <= l <= r <= self.n0
        if l == r:
            return self.x_unit
        l += self.n
        r += self.n
        ll = l // (l & -l)
        rr = r // (r & -r) - 1
        for shift in range(ll.bit_length() - 1, 0, -1):
            i = ll >> shift
            if lazy[i] == m_unit:
                continue
            lazy[i << 1] = h(lazy[i << 1], lazy[i])
            lazy[(i << 1) + 1] = h(lazy[(i << 1) + 1], lazy[i])
            seg[i] = g(seg[i], lazy[i])
            lazy[i] = m_unit
        for shift in range(rr.bit_length() - 1, 0, -1):
            i = rr >> shift
            if lazy[i] == m_unit:
                continue
            lazy[i << 1] = h(lazy[i << 1], lazy[i])
            lazy[(i << 1) + 1] = h(lazy[(i << 1) + 1], lazy[i])
            seg[i] = g(seg[i], lazy[i])
            lazy[i] = m_unit
        ans_l = ans_r = self.x_unit
        while l < r:
            if l & 1:
                ans_l = f(ans_l, (seg[l] if lazy[l] == m_unit else g(seg[l], lazy[l])))
                l += 1
            if r & 1:
                r -= 1
                ans_r = f((seg[r] if lazy[r] == m_unit else g(seg[r], lazy[r])), ans_r)
            l >>= 1
            r >>= 1
        return f(ans_l, ans_r)

    def get(self, i):
        seg = self.seg
        lazy = self.lazy
        g = self.g
        h = self.h
        m_unit = self.m_unit
        assert 0 <= i < self.n0
        i += self.n
        for shift in range(i.bit_length() - 1, 0, -1):
            j = i >> shift
            if lazy[j] == m_unit:
                continue
            lazy[j << 1] = h(lazy[j << 1], lazy[j])
            lazy[(j << 1) + 1] = h(lazy[(j << 1) + 1], lazy[j])
            seg[j] = g(seg[j], lazy[j])
            lazy[j] = m_unit
        return (seg[i] if lazy[i] == m_unit else g(seg[i], lazy[i]))

    def max_right(self, l, check):
        seg = self.seg
        lazy = self.lazy
        f = self.f
        g = self.g
        h = self.h
        m_unit = self.m_unit
        assert 0 <= l <= self.n0
        assert check(self.x_unit)
        if l == self.n0:
            return self.n0
        assert self.n & (self.n - 1) == 0, "use power_of_two=True"
        l += self.n
        ll = l // (l & -l)
        for shift in range(ll.bit_length() - 1, 0, -1):
            i = ll >> shift
            if lazy[i] == m_unit:
                continue
            lazy[i << 1] = h(lazy[i << 1], lazy[i])
            lazy[(i << 1) + 1] = h(lazy[(i << 1) + 1], lazy[i])
            seg[i] = g(seg[i], lazy[i])
            lazy[i] = m_unit
        ans = self.x_unit
        while True:
            while (l & 1) == 0:
                l >>= 1
            nxt = f(ans, (seg[l] if lazy[l] == m_unit else g(seg[l], lazy[l])))
            if not check(nxt):
                while l < self.n:
                    if lazy[l] != m_unit:
                        lazy[l << 1] = h(lazy[l << 1], lazy[l])
                        lazy[(l << 1) + 1] = h(lazy[(l << 1) + 1], lazy[l])
                        seg[l] = g(seg[l], lazy[l])
                        lazy[l] = m_unit
                    l <<= 1
                    nxt = f(ans, (seg[l] if lazy[l] == m_unit else g(seg[l], lazy[l])))
                    if check(nxt):
                        ans = nxt
                        l += 1
                res = l - self.n
                return self.n0 if res > self.n0 else res
            ans = nxt
            l += 1
            if (l & -l) == l:
                break
        return self.n0

    def min_left(self, r, check):
        seg = self.seg
        lazy = self.lazy
        f = self.f
        g = self.g
        h = self.h
        m_unit = self.m_unit
        assert 0 <= r <= self.n0
        assert check(self.x_unit)
        if r == 0:
            return 0
        assert self.n & (self.n - 1) == 0, "use power_of_two=True"
        r += self.n
        k = r - 1
        for shift in range(k.bit_length() - 1, 0, -1):
            i = k >> shift
            if lazy[i] == m_unit:
                continue
            lazy[i << 1] = h(lazy[i << 1], lazy[i])
            lazy[(i << 1) + 1] = h(lazy[(i << 1) + 1], lazy[i])
            seg[i] = g(seg[i], lazy[i])
            lazy[i] = m_unit
        ans = self.x_unit
        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            nxt = f((seg[r] if lazy[r] == m_unit else g(seg[r], lazy[r])), ans)
            if not check(nxt):
                while r < self.n:
                    if lazy[r] != m_unit:
                        lazy[r << 1] = h(lazy[r << 1], lazy[r])
                        lazy[(r << 1) + 1] = h(lazy[(r << 1) + 1], lazy[r])
                        seg[r] = g(seg[r], lazy[r])
                        lazy[r] = m_unit
                    r = (r << 1) + 1
                    nxt = f((seg[r] if lazy[r] == m_unit else g(seg[r], lazy[r])), ans)
                    if check(nxt):
                        ans = nxt
                        r -= 1
                res = r - self.n + 1
                if res < 0:
                    return 0
                return self.n0 if res > self.n0 else res
            ans = nxt
            if (r & -r) == r:
                break
        return 0
