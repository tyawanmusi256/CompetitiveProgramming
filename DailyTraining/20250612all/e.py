class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        root_x = self.find(x)
        return sum(1 for i in range(len(self.parent)) if self.find(i) == root_x)

n,m=map(int,input().split())
inout=[0]*n
uf = UnionFind(n)
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    inout[a]+=1
    inout[b]+=1
    uf.union(a,b)
if uf.size(0)==n and inout==[2]*n:
    print("Yes")
else:
    print("No")