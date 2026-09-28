# Mo's algorithm: 0-indexed、クエリは半開区間 [u, v)
# Mo_Base(n): 長さ n の固定配列に対するオフラインの区間クエリ。
# add_query(u, v): f(u, v) を求めるクエリを追加する。u, v は 0-indexed、0 <= u, v <= n。
# solve(block_size=None): 登録順の答えを返す。ブロック幅は省略時 N/sqrt(Q)。
# 1回の状態更新が O(1) なら、目安は O(N sqrt(Q) + Q log Q)、追加メモリ O(Q)。

# 派生クラスを作成し、空区間の状態と下記4メソッドを実装する（引数は移動前の端点）。
# u_plus: a[u] を削除、u_minus: a[u-1] を追加
# v_plus: a[v] を追加、v_minus: a[v-1] を削除
# get_ans は現在の答えを返す。可変オブジェクトの答えはコピーを返すこと。

# 使用例（区間和）:
# class Mo(Mo_Base):
#     def __init__(self, a):
#         super().__init__(len(a))
#         self.a = a
#     def u_plus(self, u, v): self.ans -= self.a[u]
#     def u_minus(self, u, v): self.ans += self.a[u-1]
#     def v_plus(self, u, v): self.ans += self.a[v]
#     def v_minus(self, u, v): self.ans -= self.a[v-1]
# mo = RangeSumMo([1, 2, 3])
# mo.add_query(0, 2)
# mo.add_query(1, 3)
# print(mo.solve())  # [3, 5]

# a[l, r) の要素の種類数クエリ N, Q <= 5e5
# https://judge.yosupo.jp/submission/406717 / PyPy3 / 4014 ms


class Mo_Base:
    def __init__(self, n):
        assert n >= 0
        self.n = n
        self.queries = []
        self._u = self._v = 0
        # 空区間 [0, 0) の状態を初期化する
        self.ans = 0

    def u_plus(self, u, v): raise NotImplementedError
    def u_minus(self, u, v): raise NotImplementedError
    def v_plus(self, u, v): raise NotImplementedError
    def v_minus(self, u, v): raise NotImplementedError

    def get_ans(self):
        return self.ans

    def add_query(self, u, v):
        self.queries.append((u, v, len(self.queries)))

    def solve(self, block_size=None):
        q = len(self.queries)
        if q == 0:
            return []
        bsize = max(1, int(self.n / q**0.5)) if block_size is None else block_size
        assert isinstance(bsize, int) and bsize > 0
        self.queries.sort(key=lambda x: (
            x[0] // bsize,
            x[1] if (x[0] // bsize) % 2 == 0 else -x[1]
        ))
        ans = [0] * q
        u, v = self._u, self._v
        u_plus, u_minus = self.u_plus, self.u_minus
        v_plus, v_minus = self.v_plus, self.v_minus
        get_ans = self.get_ans
        for target_u, target_v, q_i in self.queries:
            while v < target_v:
                v_plus(u, v)
                v += 1
            while u > target_u:
                u_minus(u, v)
                u -= 1
            while v > target_v:
                v_minus(u, v)
                v -= 1
            while u < target_u:
                u_plus(u, v)
                u += 1
            ans[q_i] = get_ans()
        self._u, self._v = u, v
        return ans

class Mo(Mo_Base):
    def __init__(self, n):
        if isinstance(n, int):
            super().__init__(n)
            self.a = [0] * n
        else:
            super().__init__(len(n))
            self.a = n

    def u_plus(self, u, v):
        # f(u, v) -> f(u+1, v)
        return
    def u_minus(self, u, v):
        # f(u, v) -> f(u-1, v)
        return
    def v_plus(self, u, v):
        # f(u, v) -> f(u, v+1)
        return
    def v_minus(self, u, v):
        # f(u, v) -> f(u, v-1)
        return

