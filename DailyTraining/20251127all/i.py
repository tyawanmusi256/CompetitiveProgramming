import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

#オイラーツアー
#in,out配列を作るときは別途実装が必要
def euler_tour(edge, s):
    n=len(edge)
    visited=[0]*n
    tour=[]
    in_time=[-1]*n
    out_time=[-1]*n
    time=0
    def dfs(v):
        nonlocal time
        visited[v]=1
        tour.append(v)
        in_time[v]=time
        time+=1
        for node in edge[v]:
            if not visited[node]:
                dfs(node)
                tour.append(v)
                out_time[v]=time
                time+=1
    dfs(s)
    for i in range(n):
        if out_time[i]==-1:
            out_time[i]=in_time[i]
    return tour,in_time,out_time

#セグ木
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

n=int(input())
edge=[[] for _ in range(n)]
edges=[]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edges.append((a,b))
tour,in_time,out_time=euler_tour(edge,0)
# print(tour)
# print(in_time)
# print(out_time)
seg=SegmentTree(len(tour),[0]*len(tour),0,lambda x,y: x+y)
for i in range(n):
    l=in_time[i]
    seg.update(l,1)
sumw=n
for _ in range(int(input())):
    q=list(map(int,input().split()))
    if q[0]==1:
        x,w=q[1]-1,q[2]
        l=in_time[x]
        seg.update(l,seg.get(l)+w)
        sumw+=w
    else:
        y=q[1]-1
        a,b=edges[y]
        if in_time[a]<in_time[b]:
            x=b
        else:
            x=a
        l=in_time[x]
        r=out_time[x]
        # print("-",x,(l,r))
        print(abs(sumw-seg.query(l,r+1)*2))