class LazySegmentTree:

    # f(X, X) -> X
    # g(X, M) -> X
    # h(M, M) -> M

    # max_right / min_left を使いたいなら N を 2冪 に切り上げて渡すこと

    __slots__ = ["n0", "n", "seg", "x_unit", "m_unit", "f", "g", "h", "lazy"]

    def __init__(self, n, p, x_unit, m_unit, f, g, h, power_of_two=False):
        self.n0 = n
        if power_of_two:
            self.n = 1 << (n - 1).bit_length()
            self.seg = (p + [x_unit] * (self.n - n)) * 2
        else:
            self.n = n
            self.seg = p * 2
        self.x_unit = x_unit
        self.m_unit = m_unit
        self.f = f
        self.g = g
        self.h = h
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.f(self.seg[i << 1], self.seg[(i << 1) + 1])
        self.lazy = [m_unit] * (self.n * 2)

    def update(self, l, r, x):
        l += self.n
        r += self.n
        ll = l // (l & -l)
        rr = r // (r & -r) - 1
        for shift in range(ll.bit_length() - 1, 0, -1):
            i = ll >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
            self.lazy[(i << 1) + 1] = self.h(self.lazy[(i << 1) + 1], self.lazy[i])
            self.seg[i] = self.g(self.seg[i], self.lazy[i])
            self.lazy[i] = self.m_unit
        for shift in range(rr.bit_length()-1, 0, -1):
            i = rr >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
            self.lazy[(i << 1) + 1] = self.h(self.lazy[(i << 1) + 1], self.lazy[i])
            self.seg[i] = self.g(self.seg[i], self.lazy[i])
            self.lazy[i] = self.m_unit
        while l < r:
            if l & 1:
                self.lazy[l] = self.h(self.lazy[l], x)
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = self.h(self.lazy[r], x)
            l >>= 1
            r >>= 1
        while ll > 1:
            ll >>= 1
            self.seg[ll] = self.f(self.g(self.seg[ll << 1], self.lazy[ll << 1]), self.g(self.seg[(ll << 1) + 1], self.lazy[(ll << 1) + 1]))
            self.lazy[ll] = self.m_unit
        while rr > 1:
            rr >>= 1
            self.seg[rr] = self.f(self.g(self.seg[rr << 1], self.lazy[rr << 1]), self.g(self.seg[(rr << 1) + 1], self.lazy[(rr << 1) + 1]))
            self.lazy[rr] = self.m_unit

    def query(self, l, r):
        l += self.n
        r += self.n
        ll = l // (l & -l)
        rr = r // (r & -r) - 1
        for shift in range(ll.bit_length() - 1, 0, -1):
            i = ll >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
            self.lazy[(i << 1) + 1] = self.h(self.lazy[(i << 1) + 1], self.lazy[i])
            self.seg[i] = self.g(self.seg[i], self.lazy[i])
            self.lazy[i] = self.m_unit
        for shift in range(rr.bit_length() - 1, 0, -1):
            i = rr >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
            self.lazy[(i << 1) + 1] = self.h(self.lazy[(i << 1) + 1], self.lazy[i])
            self.seg[i] = self.g(self.seg[i], self.lazy[i])
            self.lazy[i] = self.m_unit
        ans_l = ans_r = self.x_unit
        while l < r:
            if l & 1:
                ans_l = self.f(ans_l, self.g(self.seg[l], self.lazy[l]))
                l += 1
            if r & 1:
                r -= 1
                ans_r = self.f(self.g(self.seg[r], self.lazy[r]), ans_r)
            l >>= 1
            r >>= 1
        return self.f(ans_l, ans_r)

    def get(self, i):
        assert 0 <= i < self.n0
        i += self.n
        for shift in range(i.bit_length() - 1, 0, -1):
            j = i >> shift
            self.lazy[j << 1] = self.h(self.lazy[j << 1], self.lazy[j])
            self.lazy[(j << 1) + 1] = self.h(self.lazy[(j << 1) + 1], self.lazy[j])
            self.seg[j] = self.g(self.seg[j], self.lazy[j])
            self.lazy[j] = self.m_unit
        return self.g(self.seg[i], self.lazy[i])

    def max_right(self, l, check):
        if l == self.n0:
            return self.n0
        assert 0 <= l < self.n0
        assert check(self.x_unit)
        l += self.n
        ll = l // (l & -l)
        for shift in range(ll.bit_length() - 1, 0, -1):
            i = ll >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
            self.lazy[(i << 1) + 1] = self.h(self.lazy[(i << 1) + 1], self.lazy[i])
            self.seg[i] = self.g(self.seg[i], self.lazy[i])
            self.lazy[i] = self.m_unit
        ans = self.x_unit
        while True:
            while (l & 1) == 0:
                l >>= 1
            nxt = self.f(ans, self.g(self.seg[l], self.lazy[l]))
            if not check(nxt):
                while l < self.n:
                    self.lazy[l << 1] = self.h(self.lazy[l << 1], self.lazy[l])
                    self.lazy[(l << 1) + 1] = self.h(self.lazy[(l << 1) + 1], self.lazy[l])
                    self.seg[l] = self.g(self.seg[l], self.lazy[l])
                    self.lazy[l] = self.m_unit
                    l <<= 1
                    nxt = self.f(ans, self.g(self.seg[l], self.lazy[l]))
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
        if r == 0:
            return 0
        assert 0 <= r < self.n0
        assert check(self.x_unit)
        r += self.n
        k = r - 1
        for shift in range(k.bit_length() - 1, 0, -1):
            i = k >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
            self.lazy[(i << 1) + 1] = self.h(self.lazy[(i << 1) + 1], self.lazy[i])
            self.seg[i] = self.g(self.seg[i], self.lazy[i])
            self.lazy[i] = self.m_unit
        ans = self.x_unit
        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            nxt = self.f(self.g(self.seg[r], self.lazy[r]), ans)
            if not check(nxt):
                while r < self.n:
                    self.lazy[r << 1] = self.h(self.lazy[r << 1], self.lazy[r])
                    self.lazy[(r << 1) + 1] = self.h(self.lazy[(r << 1) + 1], self.lazy[r])
                    self.seg[r] = self.g(self.seg[r], self.lazy[r])
                    self.lazy[r] = self.m_unit
                    r = (r << 1) + 1
                    nxt = self.f(self.g(self.seg[r], self.lazy[r]), ans)
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

import sys

def main():
    sys.setrecursionlimit(1_000_000)
    input = sys.stdin.buffer.readline

    n, b, q = map(int, input().split())
    a = list(map(int, input().split()))

    # sum[i] = (a[0]-b) + ... + (a[i]-b)
    s = [0] * n
    cur = 0
    for i in range(n):
        cur += a[i] - b
        s[i] = cur

    NEG_INF = -10**30

    f = max                     # X×X -> X
    g = lambda x, m: x + m      # X×M -> X (range add)
    h = lambda m1, m2: m1 + m2  # M×M -> M (add composition)
    x_unit = NEG_INF
    m_unit = 0

    seg = LazySegmentTree(n, s, x_unit, m_unit, f, g, h, True)

    out = []
    for _ in range(q):
        c, x = map(int, input().split())
        c -= 1
        diff = x - a[c]
        a[c] = x
        seg.update(c, n, diff)  # suffix add

        # first i where prefix max becomes >= 0
        i = seg.max_right(0, lambda mx: mx < 0)
        if i == n:
            i = n - 1

        ans = seg.get(i) / (i + 1) + b
        out.append(f"{ans:.10f}\n")

    sys.stdout.write("".join(out))

if __name__ == "__main__":
    main()