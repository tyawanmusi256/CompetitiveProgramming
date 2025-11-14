class SegmentTree:
    def __init__(self, n, p, unit, f):
        self.n = n
        self.num = 2**((n-1).bit_length())
        self.seg = [unit]*(self.num*2)
        for i in range(n):
            self.seg[self.num+i] = p[i]
        for i in range(self.num-1, 0, -1):
            self.seg[i] = f(self.seg[i << 1], self.seg[(i << 1)+1])
        self.unit = unit
        self.f = f

    def update(self, i, x):
        i += self.num
        self.seg[i] = x
        while i:
            i >>= 1
            self.seg[i] = self.f(self.seg[i << 1], self.seg[(i << 1)+1])

    def query(self, l, r):
        ansl = ansr = self.unit
        l += self.num
        r += self.num-1
        if l == r:
            return self.seg[l]
        while l < r:
            if l & 1:
                ansl = self.f(ansl, self.seg[l])
                l += 1
            if ~r & 1:
                ansr = self.f(self.seg[r], ansr)
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            ansl = self.f(ansl, self.seg[l])
        return self.f(ansl, ansr)

    def max_right(self, l, g):
        l += self.num
        ll = l // (l & -l)
        ans = self.unit
        while g(self.f(ans, self.seg[ll])):
            ans = self.f(ans, self.seg[ll])
            ll += 1
            while ~ll & 1:
                ll >>= 1
            if ll == 1:
                return self.n
        while ll < self.num:
            ll <<= 1
            if g(self.f(ans, self.seg[ll])):
                ans = self.f(ans, self.seg[ll])
                ll += 1
        return ll-self.num
  
    def min_left(self, r, g):
        r += self.num
        rr = max(r // (~r & -~r), 1)
        ans = self.unit
        while g(self.f(self.seg[rr], ans)):
            ans = self.f(self.seg[rr], ans)
            rr -= 1
            while rr & 1:
                rr >>= 1
            if rr == 0:
                return -1
        while rr < self.num:
            rr <<= 1
            if g(self.f(self.seg[rr+1], ans)):
                ans = self.f(self.seg[rr+1], ans)
            else:
                rr += 1
        return rr - self.num
    
    def get(self, i):
        return self.seg[i + self.num]

n,q=map(int, input().split())
a=list(map(int, input().split()))
st=SegmentTree(n, a, 0, lambda x,y: x+y)
for _ in range(q):
    t,x,y=map(int, input().split())
    if t==0:
        st.update(x, y+a[x])
        a[x]+=y
    else:
        print(st.query(x, y))