# BinaryIndexedTree
# 添字は 0-indexed、区間は半開区間 [l, r)（l を含み、r を含まない）
# BinaryIndexedTree(n): 長さ n のゼロ配列から構築、O(n)
# BinaryIndexedTree(a): リスト a をコピーして構築、O(len(a))
# add(i, x): a[i] += x、0 <= i < n、O(log n)
# sum(l, r): [l, r) の和、0 <= l <= r <= n、O(log n)
# sum_sub(r): [0, r) の和、0 <= r <= n、O(log n)

# 一点更新・区間和クエリ N, Q <= 5e5
# https://judge.yosupo.jp/submission/406676 / PyPy3 / 317 ms

class BinaryIndexedTree:
    __slots__ = ["bit"]

    def __init__(self, n):
        if isinstance(n, int):
            self.bit = [0] * n
        else:
            self.bit = n.copy()
            n = len(self.bit)
            for i in range(1, n + 1):
                j = i + (i & -i)
                if j <= n:
                    self.bit[j-1] += self.bit[i-1]

    def add(self, i, x):
        i += 1
        while i <= len(self.bit):
            self.bit[i-1] += x
            i += i & -i

    def sum_sub(self, r):
        total = 0
        while r:
            total += self.bit[r-1]
            r -= r & -r
        return total

    def sum(self, l, r):
        return self.sum_sub(r) - self.sum_sub(l)
