class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.parent[x_root] > self.parent[y_root]:
            x_root, y_root = y_root, x_root

        self.parent[x_root] += self.parent[y_root]
        self.parent[y_root] = x_root
        return True

    def size(self, x):
        return -self.parent[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def is_root(self, x):
        return self.parent[x] < 0

mod=998244353
frac=[1]*(10**6+1)
inv=[1]*(10**6+1)
for i in range(1,10**6+1):
    frac[i]=frac[i-1]*i%mod
    inv[i]=pow(frac[i],mod-2,mod)

n,m=map(int,input().split())
s=input()
uf=UnionFind(n)
for _ in range(m):
    a,b=map(int,input().split())
    uf.union(a-1,b-1)
d={}
for i in range(n):
    if uf.is_root(i):
        d[i]=[]
for i in range(n):
    d[uf.find(i)].append(s[i])
from collections import Counter
ans=1
flag=False
for _,v in d.items():
    c=Counter(v)
    ans*=frac[sum(c.values())]
    for x in c.values():
        if x>=2:
            flag=True
        ans*=inv[x]
        ans%=mod
if flag:
    print(ans)
else:
    print(ans*inv[2]%mod)