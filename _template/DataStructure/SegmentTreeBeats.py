class SegmentTreeBeats:

    """
    SegmentTreeBeats
    Initialization: SegmentTreeBeats(a)
    Range Update:
        update_add(l, r, x): a[i] += x for i in [l, r)
        update_chmin(l, r, x): a[i] = min(a[i], x) for i in [l, r)
        update_chmax(l, r, x): a[i] = max(a[i], x) for i in [l, r)
    Range Query:
        query_sum(l, r): sum(a[i] for i in [l, r))
        query_min(l, r): min(a[i] for i in [l, r))
        query_max(l, r): max(a[i] for i in [l, r))
    """

    __slots__ = ["n0", "n", "h", "len", "sum", "max_v", "smax_v", "max_c", "min_v", "smin_v", "min_c", "add"]

    INF = 10**30

    def __init__(self, a):
        n = len(a)
        self.n0 = n
        self.n = 1 << (n - 1).bit_length()
        self.h = n.bit_length() - 1
        size = 2 * self.n
        self.len = [0] * size
        self.sum = [0] * size
        self.max_v = [-self.INF] * size
        self.smax_v = [-self.INF] * size
        self.max_c = [0] * size
        self.min_v = [self.INF] * size
        self.smin_v = [self.INF] * size
        self.min_c = [0] * size
        self.add = [0] * size
        for i, v in enumerate(a):
            k = self.n + i
            self.len[k] = 1
            self.sum[k] = v
            self.max_v[k] = v
            self.min_v[k] = v
            self.max_c[k] = 1
            self.min_c[k] = 1
        for k in range(self.n - 1, 0, -1):
            self._pull(k)

    def _pull(self, k):
        l = k << 1
        r = l | 1
        self.len[k] = self.len[l] + self.len[r]
        self.sum[k] = self.sum[l] + self.sum[r]
        if self.max_v[l] > self.max_v[r]:
            self.max_v[k] = self.max_v[l]
            self.max_c[k] = self.max_c[l]
            self.smax_v[k] = max(self.smax_v[l], self.max_v[r])
        elif self.max_v[l] < self.max_v[r]:
            self.max_v[k] = self.max_v[r]
            self.max_c[k] = self.max_c[r]
            self.smax_v[k] = max(self.max_v[l], self.smax_v[r])
        else:
            self.max_v[k] = self.max_v[l]
            self.max_c[k] = self.max_c[l] + self.max_c[r]
            self.smax_v[k] = max(self.smax_v[l], self.smax_v[r])
        if self.min_v[l] < self.min_v[r]:
            self.min_v[k] = self.min_v[l]
            self.min_c[k] = self.min_c[l]
            self.smin_v[k] = min(self.smin_v[l], self.min_v[r])
        elif self.min_v[l] > self.min_v[r]:
            self.min_v[k] = self.min_v[r]
            self.min_c[k] = self.min_c[r]
            self.smin_v[k] = min(self.min_v[l], self.smin_v[r])
        else:
            self.min_v[k] = self.min_v[l]
            self.min_c[k] = self.min_c[l] + self.min_c[r]
            self.smin_v[k] = min(self.smin_v[l], self.smin_v[r])

    def _apply_add(self, k, x):
        if self.len[k] == 0:
            return
        self.sum[k] += x * self.len[k]
        self.max_v[k] += x
        self.min_v[k] += x
        if self.smax_v[k] != -self.INF:
            self.smax_v[k] += x
        if self.smin_v[k] != self.INF:
            self.smin_v[k] += x
        self.add[k] += x

    def _apply_chmin(self, k, x):
        if self.len[k] == 0 or self.max_v[k] <= x:
            return
        self.sum[k] += (x - self.max_v[k]) * self.max_c[k]
        if self.max_v[k] == self.min_v[k]:
            self.max_v[k] = self.min_v[k] = x
        elif self.max_v[k] == self.smin_v[k]:
            self.max_v[k] = self.smin_v[k] = x
        else:
            self.max_v[k] = x

    def _apply_chmax(self, k, x):
        if self.len[k] == 0 or self.min_v[k] >= x:
            return
        self.sum[k] += (x - self.min_v[k]) * self.min_c[k]
        if self.max_v[k] == self.min_v[k]:
            self.max_v[k] = self.min_v[k] = x
        elif self.min_v[k] == self.smax_v[k]:
            self.min_v[k] = self.smax_v[k] = x
        else:
            self.min_v[k] = x

    def _push(self, k):
        if k >= self.n:
            return
        l = k << 1
        r = l | 1
        if self.add[k] != 0:
            x = self.add[k]
            self._apply_add(l, x)
            self._apply_add(r, x)
            self.add[k] = 0
        pv_max = self.max_v[k]
        pv_min = self.min_v[k]
        if self.max_v[l] > pv_max:
            self._apply_chmin(l, pv_max)
        if self.max_v[r] > pv_max:
            self._apply_chmin(r, pv_max)
        if self.min_v[l] < pv_min:
            self._apply_chmax(l, pv_min)
        if self.min_v[r] < pv_min:
            self._apply_chmax(r, pv_min)

    def _push_to(self, k):
        for s in range(self.h, 0, -1):
            self._push(k >> s)

    def _rebuild_from(self, k):
        while k > 1:
            k >>= 1
            self._pull(k)

    def update_add(self, l, r, x):
        if l >= r:
            return
        assert 0 <= l < r <= self.n0
        stack = [(1, 0, self.n, 0)]
        while stack:
            k, nl, nr, st = stack.pop()
            if st == 1:
                self._pull(k)
                continue
            if r <= nl or nr <= l or self.len[k] == 0:
                continue
            if l <= nl and nr <= r:
                self._apply_add(k, x)
                continue
            self._push(k)
            stack.append((k, nl, nr, 1))
            m = (nl + nr) >> 1
            stack.append(((k << 1) | 1, m, nr, 0))
            stack.append((k << 1, nl, m, 0))

    def update_chmin(self, l, r, x):
        if l >= r:
            return
        assert 0 <= l < r <= self.n0
        stack = [(1, 0, self.n, 0)]
        while stack:
            k, nl, nr, st = stack.pop()
            if st == 1:
                self._pull(k)
                continue
            if r <= nl or nr <= l or self.len[k] == 0 or self.max_v[k] <= x:
                continue
            if l <= nl and nr <= r and self.smax_v[k] < x:
                self._apply_chmin(k, x)
                continue
            self._push(k)
            stack.append((k, nl, nr, 1))
            m = (nl + nr) >> 1
            stack.append(((k << 1) | 1, m, nr, 0))
            stack.append((k << 1, nl, m, 0))

    def update_chmax(self, l, r, x):
        if l >= r:
            return
        assert 0 <= l < r <= self.n0
        stack = [(1, 0, self.n, 0)]
        while stack:
            k, nl, nr, st = stack.pop()
            if st == 1:
                self._pull(k)
                continue
            if r <= nl or nr <= l or self.len[k] == 0 or self.min_v[k] >= x:
                continue
            if l <= nl and nr <= r and self.smin_v[k] > x:
                self._apply_chmax(k, x)
                continue
            self._push(k)
            stack.append((k, nl, nr, 1))
            m = (nl + nr) >> 1
            stack.append(((k << 1) | 1, m, nr, 0))
            stack.append((k << 1, nl, m, 0))

    def query_sum(self, l, r):
        if l >= r:
            return 0
        assert 0 <= l < r <= self.n0
        res = 0
        stack = [(1, 0, self.n)]
        while stack:
            k, nl, nr = stack.pop()
            if r <= nl or nr <= l or self.len[k] == 0:
                continue
            if l <= nl and nr <= r:
                res += self.sum[k]
                continue
            self._push(k)
            m = (nl + nr) >> 1
            stack.append(((k << 1) | 1, m, nr))
            stack.append((k << 1, nl, m))
        return res

    def query_min(self, l, r):
        if l >= r:
            return self.INF
        assert 0 <= l < r <= self.n0
        res = self.INF
        stack = [(1, 0, self.n)]
        while stack:
            k, nl, nr = stack.pop()
            if r <= nl or nr <= l or self.len[k] == 0:
                continue
            if l <= nl and nr <= r:
                v = self.min_v[k]
                if v < res:
                    res = v
                continue
            self._push(k)
            m = (nl + nr) >> 1
            stack.append(((k << 1) | 1, m, nr))
            stack.append((k << 1, nl, m))
        return res

    def query_max(self, l, r):
        if l >= r:
            return -self.INF
        assert 0 <= l < r <= self.n0
        res = -self.INF
        stack = [(1, 0, self.n)]
        while stack:
            k, nl, nr = stack.pop()
            if r <= nl or nr <= l or self.len[k] == 0:
                continue
            if l <= nl and nr <= r:
                v = self.max_v[k]
                if v > res:
                    res = v
                continue
            self._push(k)
            m = (nl + nr) >> 1
            stack.append(((k << 1) | 1, m, nr))
            stack.append((k << 1, nl, m))
        return res

    def get(self, i):
        assert 0 <= i < self.n0
        k = 1
        nl = 0
        nr = self.n
        while nr - nl > 1:
            self._push(k)
            m = (nl + nr) >> 1
            if i < m:
                k = k << 1
                nr = m
            else:
                k = (k << 1) | 1
                nl = m
        return self.sum[k]

    def set(self, i, v):
        assert 0 <= i < self.n0
        path = []
        k = 1
        nl = 0
        nr = self.n
        while nr - nl > 1:
            path.append(k)
            self._push(k)
            m = (nl + nr) >> 1
            if i < m:
                k = k << 1
                nr = m
            else:
                k = (k << 1) | 1
                nl = m
        self.len[k] = 1
        self.sum[k] = v
        self.max_v[k] = v
        self.min_v[k] = v
        self.smax_v[k] = -self.INF
        self.smin_v[k] = self.INF
        self.max_c[k] = 1
        self.min_c[k] = 1
        self.add[k] = 0
        for k in reversed(path):
            self._pull(k)

# https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum
# Range Chmin Chmax Add Range Sum

import sys
input = sys.stdin.buffer.readline

n, q = map(int, input().split())
seg = SegmentTreeBeats(list(map(int, input().split())))

f = (seg.update_chmin, seg.update_chmax, seg.update_add)
ans = []
for _ in range(q):
    q = tuple(map(int, input().split()))
    if q[0] == 3:
        _, l, r = q
        ans.append(seg.query_sum(l, r))
    else:
        qt, l, r, b = q
        f[qt](l, r, b)

sys.stdout.write("\n".join(map(str, ans)) + "\n")