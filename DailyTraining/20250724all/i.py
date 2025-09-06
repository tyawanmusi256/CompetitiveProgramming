class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

n=int(input())
a=list(map(int, input().split()))
#座標圧縮
b = sorted(set(a))
dic = {b[i]: i for i in range(len(b))}
ans=0
bita=BIT(len(b)+1)
biti=BIT(len(b)+1)
for i in range(n):
    ans+=a[i]*biti.sum(dic[a[i]]+1)-bita.sum(dic[a[i]]+1)
    bita.add(dic[a[i]]+1, a[i])
    biti.add(dic[a[i]]+1, 1)
print(ans)