# SegmentTree: 0-indexed、区間は半開区間 [l, r)
# SegmentTree(n, p, unit, f): 長さ n のリスト p から O(n) で構築
# f は結合的な演算、unit はその単位元。非可換な演算にも対応。
# update(i, x): a[i] = x、O(log n)
# query(l, r): [l, r) の集約。空区間では unit、O(log n)
# get(i): a[i]、O(1)
# max_right(l, g): g(query(l, r)) が真となる最大の r
# min_left(r, g): g(query(l, r)) が真となる最小の l
# 境界探索は O(log n)。g は副作用なし・区間拡大に対して単調、g(unit) は真。
# 0 <= l <= r <= n。max_right(n, g) = n、min_left(0, g) = 0。

# 一点更新・区間和クエリ N, Q <= 5e5
# https://judge.yosupo.jp/submission/406680 / PyPy3 / 386 ms
# 一点更新・区間max, max_rightクエリ N, Q <= 2e5
# https://atcoder.jp/contests/practice2/submissions/79603251 / PyPy 3.11-v7.3.20 / 239 ms


class SegmentTree:
    __slots__ = ["n", "num", "seg", "unit", "f"]

    def __init__(self, n, p, unit, f):
        assert n >= 0 and len(p) == n
        self.n = n
        self.num = 1 << (max(1, n) - 1).bit_length()
        seg = [unit] * (self.num * 2)
        seg[self.num:self.num + n] = p
        for i in range(self.num - 1, 0, -1):
            seg[i] = f(seg[i << 1], seg[i << 1 | 1])
        self.seg = seg
        self.unit = unit
        self.f = f

    def update(self, i, x):
        assert 0 <= i < self.n
        seg, f = self.seg, self.f
        i += self.num
        seg[i] = x
        while i > 1:
            i >>= 1
            seg[i] = f(seg[i << 1], seg[i << 1 | 1])

    def query(self, l, r):
        assert 0 <= l <= r <= self.n
        seg, f = self.seg, self.f
        ans_l = ans_r = self.unit
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                ans_l = f(ans_l, seg[l])
                l += 1
            if r & 1:
                r -= 1
                ans_r = f(seg[r], ans_r)
            l >>= 1
            r >>= 1
        return f(ans_l, ans_r)

    def max_right(self, l, g):
        assert 0 <= l <= self.n
        assert g(self.unit)
        if l == self.n:
            return self.n
        seg, f, num = self.seg, self.f, self.num
        l += num
        ans = self.unit
        while True:
            while (l & 1) == 0:
                l >>= 1
            nxt = f(ans, seg[l])
            if not g(nxt):
                while l < num:
                    l <<= 1
                    nxt = f(ans, seg[l])
                    if g(nxt):
                        ans = nxt
                        l += 1
                return l - num
            ans = nxt
            l += 1
            if (l & -l) == l:
                return self.n

    def min_left(self, r, g):
        assert 0 <= r <= self.n
        assert g(self.unit)
        if r == 0:
            return 0
        seg, f, num = self.seg, self.f, self.num
        r += num
        ans = self.unit
        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            nxt = f(seg[r], ans)
            if not g(nxt):
                while r < num:
                    r = r << 1 | 1
                    nxt = f(seg[r], ans)
                    if g(nxt):
                        ans = nxt
                        r -= 1
                return r - num + 1
            ans = nxt
            if (r & -r) == r:
                return 0

    def get(self, i):
        assert 0 <= i < self.n
        return self.seg[i + self.num]
