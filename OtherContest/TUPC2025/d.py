# BinaryIndexedTree
# add(i, x): a[i] += x
# sum(i, j): a[i:j) の和
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

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    bit = BinaryIndexedTree(n+5)
    tentou = [0]*k
    same = [0]*k
    for i in range(k):
        for j in range(i,n,k):
            if bit.sum(a[j],a[j]+1):
                same[i] = 1
            tentou[i] ^= bit.sum(0, a[j]) & 1
            bit.add(a[j], 1)
        for j in range(i,n,k):
           bit.add(a[j], -1)

    b = [0]*n
    sameflag = 0
    i = n%k
    x = i
    while True:
        # if i == n%k:
        #    sameflag = same[i]
        t = sorted([a[j] for j in range(i,n,k)])
        if same[i] == 0:
            if tentou[x] ^ tentou[i]:
                t[-1], t[-2] = t[-2], t[-1]
        # if same[i] == 0:
        #    sameflag = 0
        for j in range(len(t)):
            b[i+j*k]=t[j]
        i = (i+1)%k
        if i == n%k:
           break
    # t = sorted([a[j] for j in range(i,n,k)])
    # for j in range(len(t)):
    #     b[i+j*k]=t[j]
    print(*b)
    # print(same,tentou)

"""
5 2
5 4 6 2 1
- 5 2 1 4 6
- 1 4 5 2 6
- 1 2 6 4 5
"""
"""
7 3
6 4 5 6 2 3 7
"""
"""
7 3
1 1 1 2 2 2 1
- 1 2 2 1 1 1 2
"""
"""
7 3
1 2 3 6 4 5 1
- 1 4 5 1 2 3 6
- 1 2 3 1 4 5 6
"""