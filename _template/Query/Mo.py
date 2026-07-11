# Mo's algorithm
# 1<=u,v<=N のクエリ (u,v) が Q 個あり、f(u,v) から f(u+1,v), f(u-1,v), f(u,v+1), f(u,v-1) を十分高速に計算できるとき、全クエリの答えを O(N sqrt Q) で求めるアルゴリズム
# u_plus では f(u,v) の状態から f(u+1,v) の状態へ遷移する。変数の更新や ans の更新を行う。
# mo = MO(N)
# for u, v in queries:
#     mo.add_query(u, v)
# for ans in mo.solve(): 
#     print(ans)
class Mo:
    def __init__(self, n):
        self.n = n
        self.queries = []
        # 初期状態をよしなに
        self.ans = 0

    def u_plus(self, u, v):
        # f(u, v) -> f(u+1, v)
        pass

    def u_minus(self, u, v):
        # f(u, v) -> f(u-1, v)
        pass

    def v_plus(self, u, v):
        # f(u, v) -> f(u, v+1)
        pass

    def v_minus(self, u, v):
        # f(u, v) -> f(u, v-1)
        pass

    def get_ans(self):
        return self.ans

    def add_query(self, u, v):
        self.queries.append((u, v, len(self.queries)))

    def solve(self):
        q = len(self.queries)
        if q == 0:
            return []
        bsize = max(1, int(self.n / q**0.5))
        self.queries.sort(key=lambda x: (
            x[0] // bsize,
            x[1] if (x[0] // bsize) % 2 == 0 else -x[1]
        ))
        ans = [0] * q
        u, v = 0, 0
        for target_u, target_v, q_i in self.queries:
            while v < target_v:
                self.v_plus(u, v)
                v += 1
            while u > target_u:
                self.u_minus(u, v)
                u -= 1
            while v > target_v:
                self.v_minus(u, v)
                v -= 1
            while u < target_u:
                self.u_plus(u, v)
                u += 1
            ans[q_i] = self.get_ans()
        return ans