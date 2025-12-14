class LazySegmentTree:

    # f(X, X) -> X
    # g(X, M) -> X
    # h(M, M) -> M

    __slots__ = ["n", "seg", "x_unit", "m_unit", "f", "g", "h", "lazy"]

    def __init__(self, n, p, x_unit, m_unit, f, g, h):
        self.n = n
        self.seg = p * 2
        self.x_unit = x_unit
        self.m_unit = m_unit
        self.f = f
        self.g = g
        self.h = h
        for i in range(self.n-1, 0, -1):
            self.seg[i] = self.f(self.seg[i<<1], self.seg[(i<<1)+1])
        self.lazy = [m_unit] * (self.n * 2)

    def update(self, l, r, x):
        l += self.n
        r += self.n
        ll = l // (l & -l)
        rr = r // (r & -r) - 1
        for shift in range(ll.bit_length()-1, 0, -1):
            i = ll >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
            self.lazy[(i << 1)+1] = self.h(self.lazy[(i << 1)+1], self.lazy[i])
            self.seg[i] = self.g(self.seg[i], self.lazy[i])
            self.lazy[i] = self.m_unit
        for shift in range(rr.bit_length()-1, 0, -1):
            i = rr >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1],   self.lazy[i])
            self.lazy[(i << 1)+1] = self.h(self.lazy[(i << 1)+1], self.lazy[i])
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
            self.seg[ll] = self.f(self.g(self.seg[ll << 1], self.lazy[ll << 1]), self.g(self.seg[(ll << 1)+1], self.lazy[(ll << 1)+1]))
            self.lazy[ll] = self.m_unit
        while rr > 1:
            rr >>= 1
            self.seg[rr] = self.f(self.g(self.seg[rr << 1], self.lazy[rr << 1]), self.g(self.seg[(rr << 1)+1], self.lazy[(rr << 1)+1]))
            self.lazy[rr] = self.m_unit

    def query(self, l, r):
        l += self.n
        r += self.n
        ll = l // (l & -l)
        rr = r // (r & -r) - 1
        for shift in range(ll.bit_length()-1, 0, -1):
            i = ll >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
            self.lazy[(i << 1)+1] = self.h(self.lazy[(i << 1)+1], self.lazy[i])
            self.seg[i] = self.g(self.seg[i], self.lazy[i])
            self.lazy[i] = self.m_unit
        for shift in range(rr.bit_length()-1, 0, -1):
            i = rr >> shift
            self.lazy[i << 1] = self.h(self.lazy[i << 1],   self.lazy[i])
            self.lazy[(i << 1)+1] = self.h(self.lazy[(i << 1)+1], self.lazy[i])
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


# Range Affine Range Sum
# Update: a[i] <- b*a[i] + c for i in [l, r)
# Query: output sum(a[i] for i in [l, r) ) mod 998244353

import sys
input = sys.stdin.readline

mod = 998244353
mask = (1 << 32) - 1

def f(a, b):
    m = a + b
    return ((m >> 32) << 32) + ((m & mask) % mod)

def g(a, x):
    a1 = a >> 32
    a2 = a & mask
    b = x >> 32
    c = x & mask
    return (a1 << 32) + (a1 * c + a2 * b) % mod

def h(x, y):
    b1 = x >> 32
    c1 = x & mask
    b2 = y >> 32
    c2 = y & mask
    b = b1 * b2 % mod
    c = (c1 * b2 + c2) % mod
    return (b << 32) + c

n, q = map(int, input().split())
a = [(1 << 32) + i for i in map(int, input().split())]

seg = LazySegmentTree(n, a, 0, (1 << 32), f, g, h)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        l, r, b, c = query[1], query[2], query[3], query[4]
        seg.update(l, r, (b << 32) + c)
    else:
        l, r = query[1], query[2]
        print(seg.query(l, r) & mask)

