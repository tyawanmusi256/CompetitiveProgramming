class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

n=int(input())
a=list(map(int,input().split()))
p=[-1]*(10**6+1)
for i in range(n):
    p[a[i]]=i
uf=UnionFind(n)
edge_cnt=0
ans=0
for i in range(10**6,0,-1):
    x=-1
    for j in range(i,10**6+1,i):
        if p[j]!=-1:
            if x==-1:
                x=p[j]
            else:
                if not uf.same(x,p[j]):
                    ans+=i
                    uf.union(x,p[j])
                    edge_cnt+=1
                    if edge_cnt==n-1:
                        print(ans)
                        exit()