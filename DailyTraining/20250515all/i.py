import sys
sys.setrecursionlimit(10**7)
# BinaryIndexedTree
class BinaryIndexedTree:
    def __init__(self, n):
        self.bit = [0] * n

    def add(self, i, x):
        i += 1
        while i <= len(self.bit):
            self.bit[i-1] += x
            i += i & -i

    def sum_sub(self, i):
        a = 0
        while i:
            a += self.bit[i-1]
            i -= i & -i
        return a

    def sum(self, i, j):
        return self.sum_sub(j) - self.sum_sub(i)
    
n=int(input())
a=list(map(int,input().split()))
bit1=BinaryIndexedTree(200001)
bit2=BinaryIndexedTree(200001)
ans=a[0]
print(ans)
bit1.add(a[0],1)
bit2.add(a[0],a[0])
mod=998244353
for i in range(1,n):
    ans+=a[i]
    ans+=bit1.sum(0,a[i]+1)*a[i]*2
    ans+=bit2.sum(a[i]+1,200001)*2
    print(ans*pow((i+1)**2,mod-2,mod)%mod)
    bit1.add(a[i],1)
    bit2.add(a[i],a[i])