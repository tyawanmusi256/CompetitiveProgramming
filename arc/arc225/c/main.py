# cost1の辺をk本ぴったり選びながら全域木構築
# 橋は明らかに選ばないといけない
# 辺連結度の小さい辺から貪欲に取りたいね
# フローって連結度見れなかったっけ
# そもそも1e5やん無理
# 難しすぎる 外れ方針っぽい
# 一旦構築可能性を考える
# コストの最大最小値は簡単 0優先,1優先の全域木構築をするだけ
# minK<=K<=maxKであるminmaxがわかる
# で？
# minK<=K<=maxKでありつつ構築不可能なKが存在する？
# 思いつかないので存在しないとする
# minKまたはmaxKで全域木を構築して、そこからKをズラせる？
# 難しくない？
# 意外と通している人が多いからシンプルな考察でしょう
# 構築してからズラすのはかなり難しい方針なので、やっぱり作りながら一発でKにしたい
# minKの木に含まれるコスト0の辺は必ずいる
# 逆にそれ以外の辺は自由な順番で選んでもよい？<-本当？
# 同様にmaxKの木に含まれるコスト1の辺は必ずいる
# 逆にそれ以外の辺は自由な順番で選んでもよい<-本当！

import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    edge=[]
    for i in range(m):
        a,b,c=map(int,input().split())
        edge.append((c,a-1,b-1,i+1))
    edge.sort()
    ufmin=UnionFind(n)
    ufmax=UnionFind(n)
    mintree=set()
    maxtree=set()
    minK=0
    maxK=0
    for i in range(m):
        c,a,b,id=edge[i]
        if not ufmin.is_same(a,b):
            ufmin.union(a,b)
            mintree.add(i)
            minK+=c
        c,a,b,id=edge[-1-i]
        if not ufmax.is_same(a,b):
            ufmax.union(a,b)
            maxtree.add(m-1-i)
            maxK+=c
    if k<minK or k>maxK:
        print(-1)
        continue
    must=set()
    uf=UnionFind(n)
    ans=[]
    cnt0=0
    for i in maxtree:
        c,a,b,id=edge[i]
        if c==1:
            continue
        must.add(i)
        uf.union(a,b)
        ans.append(id)
        cnt0+=1
    for i in range(m):
        if i in must:
            continue
        c,a,b,id=edge[i]
        if not uf.is_same(a,b) and ((c==0 and cnt0<n-1-k)or c==1):
            uf.union(a,b)
            ans.append(id)
            k-=c
            if c==0:
                cnt0+=1
    if k!=0:
        print(-1)
    else:
        print(*ans)