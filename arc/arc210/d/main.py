import sys
input = sys.stdin.readline

# UnionFind
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        # 連結成分に含まれる辺の数
        self.count = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
                self.count[rootX] += self.count[rootY] + 1
            else:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
                self.count[rootY] += self.count[rootX] + 1
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootY] += 1
        else:
            self.count[rootX] += 1

    def get_size(self, x):
        return self.size[self.find(x)]
    
    def get_count(self, x):
        return self.count[self.find(x)]

# Nimでなんとかなりませんか？
# わかんね～

# 次数最大の頂点(10以上くらい)があるとき、aliceはかなりそれを取りたくない
# bobは必ずそれを押し付けられるので、aliceの勝つ方法はその頂点との隣接点を全てbobに押し付けること
# bobはそれを拒否できるので、bob必勝
# o-o-o
#   |
#   o
# のような形があるとき、aliceは中央の頂点を取りたくないけど、どうしようもなくないですか

# うわ～Nが偶数のときもあります
# うわ～

# Nが奇数ときに絞って考察を続けます
# 偶奇で勝敗反転とかしてくれるといいな
# 次数を2以下に制限できますので、閉路グラフかパスグラフになりますです
# パスグラフ
# 1-a, 2-a, 3-b, 4-a, 5-b, 6-b, これ以降はずっとbobの勝ち
# 閉路グラフ
# 3-b, 4-b, 5-b, これ以降はずっとbobの勝ち
# 孤立点が"奇数個"あったら、aliceが1手有利を取れる→bobはそこらへんで1手潰すためどこかの連結成分の頂点数を-1する

# 結構解けそうなので偶数の場合に戻る
# o-o-o
#   |
#   o
# 思ったけどこの形が2個以上あったら結局aliceが負けなので1個だけに絞る
# この中心の点から伸びるパスを切り取って、それぞれの長さを[a,b,c,...]とすると、これらがかなり短くないとaliceが勝てない
# o-o-o-o
#   \/
#   o
# この形に加えて孤立点があるときだけaliceの勝ち

# 考えをまとめる
# Nが奇数のとき
# 全頂点の次数が2以下ではないとき、bobの勝ち
# 長さ3のパスが1個でもあるとbobの勝ち←N奇数なら長さ3以上としても良い
# 部分グラフとして長さ3のパスがある、としてもよさそう
# その余事象は長さ1,2のパスのみからなるグラフなので、aliceの勝ち

# Nが偶数のとき
# 長さ3のパス(部分グラフ)が2個あるとき、N-6個の頂点で時間を潰したあとにbobの勝ち
# 長さ5のサイクル(部分グラフ)があるとき、N-5個の頂点で時間を潰したあとにaliceの勝ち←複数個あったらもちろんbobの勝ち
# 長さ4のサイクル(部分グラフ)があるとき、N-4個の頂点で時間を潰したあとにbobの勝ち
# 長さ3のサイクル(部分グラフ)があるとき←あとで考える
# 次数3以上の頂点が2個あるとき、だいたいbobの勝ち
# 1個の時、その頂点を削除して(最後にbobに押し付ける)残りを帰納的に考える

def solveodd(n,m,edge):
    if max(len(node)for node in edge)>=2:
        print("Bob")
        return
    print("Alice")
    return
    uf=UnionFind(n)
    for node in range(n):
        if len(edge[node])>=3:
            print("Bob")
            return
        for mode in edge[node]:
            uf.union(node,mode)
    for i in range(n):
        if uf.get_size(i)>=3 :
            print("Bob")
            return
    print("Alice")
    return
    
def solveeven(n,m,edge):
    uf=UnionFind(n)
    d3=[]
    for node in range(n):
        if len(edge[node])>=3:
            d3.append(node)
        for mode in edge[node]:
            uf.union(node,mode)
    if len(d3)>=3:
        print("Bob")
        return
    if len(d3)==2:
        if uf.find(d3[0])!=uf.find(d3[1]):
            print("Bob")
            return
        if uf.get_size(d3[0])!=5:
            print("Bob")
            return
        if uf.get_count(d3[0])!=5:
            print("Bob")
            return
        for i in range(n):
            if uf.find(i)!=i:
                continue
            if uf.find(i)==uf.find(d3[0]):
                continue
            size=uf.get_size(i)
            if size>=3:
                print("Bob")
                return
        print("Alice")
        return
    if len(d3)==1:
        d3=d3[0]
        nn=n-1
        nedge=[[]for _ in range(nn)]
        for i in range(n):
            if i==d3:
                continue
            for j in edge[i]:
                if j==d3:
                    continue
                ni=i-(1 if i>d3 else 0)
                nj=j-(1 if j>d3 else 0)
                nedge[ni].append(nj)
        solveodd(nn,m-len(edge[d3]),nedge)
        return
    # 次数3以上の頂点がないとしてよい
    bad=0
    for i in range(n):
        if uf.find(i)!=i:
            continue
        size=uf.get_size(i)
        count=uf.get_count(i)
        if size>=6:
            print("Bob")
            return
        if size<=2:
            continue
        if size==5:
            bad+=1
        elif size==4:
            if count==4:
                print("Bob")
                return
            else:
                bad+=1
        elif size==3:
            bad+=1
    if bad>=2:
        print("Bob")
        return
    else:
        print("Alice")
        return
        
        


def solve():
    n,m=map(int,input().split())
    edge=[[]for _ in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        a-=1
        b-=1
        edge[a].append(b)
        edge[b].append(a)
    if n%2==1:
        solveodd(n,m,edge)
    else:
        solveeven(n,m,edge)
    

for _ in range(int(input())):
    solve()