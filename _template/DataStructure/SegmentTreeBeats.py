# SegmentTreeBeats: 0-indexed、区間は半開区間 [l, r)
# SegmentTreeBeats(a): 初期リスト a から O(n) で構築。
# update_add(l, r, x): [l, r) の各要素に x を加算
# update_chmin(l, r, x): [l, r) の各要素を min(a[i], x) に更新
# update_chmax(l, r, x): [l, r) の各要素を max(a[i], x) に更新
# query_sum / query_min / query_max(l, r): [l, r) の和 / 最小値 / 最大値
# get(i) / set(i, x): 1点取得 / 代入。ともに O(log n)。
# 区間加算・各集約は O(log n)。chmin/chmax は償却解析が必要で、1操作 O(log n) の保証はない。（定数倍もやばい）
# 0 <= l <= r <= n。空区間の更新は何もしない。和は0、最小値は INF、最大値は -INF。

# 使用例:
# seg = SegmentTreeBeats([1, 5, 3])
# seg.update_chmin(0, 2, 2)  # [1, 2, 3]
# seg.update_add(1, 3, 4)    # [1, 6, 7]
# print(seg.query_sum(0, 3)) # 14
# print(seg.query_min(1, 3)) # 6

# 区間加算/chmin/chmax・区間和クエリ N, Q <= 2e5
# https://judge.yosupo.jp/submission/406684 / PyPy3 / 5490 ms


class SegmentTreeBeats:
    __slots__ = ["n0", "n", "h", "len", "sum", "max_v", "smax_v", "max_c", "min_v", "smin_v", "min_c", "add"]

    INF = 10**30

    def __init__(self, a):
        n = len(a)
        self.n0 = n
        self.n = 1 << (max(1, n) - 1).bit_length()
        self.h = self.n.bit_length() - 1
        size = 2 * self.n
        self.len = [0] * size
        self.sum = [0] * size
        self.max_v = [-self.INF] * size
        self.smax_v = [-self.INF] * size
        self.max_c = [0] * size
        self.min_v = [self.INF] * size
        self.smin_v = [self.INF] * size
        self.min_c = [0] * size
        self.add = [0] * size
        for i, v in enumerate(a):
            k = self.n + i
            self.len[k] = 1
            self.sum[k] = v
            self.max_v[k] = v
            self.min_v[k] = v
            self.max_c[k] = 1
            self.min_c[k] = 1
        for k in range(self.n - 1, 0, -1):
            self.len[k] = self.len[k << 1] + self.len[k << 1 | 1]
            self._pull(k)

    def _pull(self, k):
        l = k << 1
        r = l | 1
        self.sum[k] = self.sum[l] + self.sum[r]
        if self.max_v[l] > self.max_v[r]:
            self.max_v[k] = self.max_v[l]
            self.max_c[k] = self.max_c[l]
            self.smax_v[k] = max(self.smax_v[l], self.max_v[r])
        elif self.max_v[l] < self.max_v[r]:
            self.max_v[k] = self.max_v[r]
            self.max_c[k] = self.max_c[r]
            self.smax_v[k] = max(self.max_v[l], self.smax_v[r])
        else:
            self.max_v[k] = self.max_v[l]
            self.max_c[k] = self.max_c[l] + self.max_c[r]
            self.smax_v[k] = max(self.smax_v[l], self.smax_v[r])
        if self.min_v[l] < self.min_v[r]:
            self.min_v[k] = self.min_v[l]
            self.min_c[k] = self.min_c[l]
            self.smin_v[k] = min(self.smin_v[l], self.min_v[r])
        elif self.min_v[l] > self.min_v[r]:
            self.min_v[k] = self.min_v[r]
            self.min_c[k] = self.min_c[r]
            self.smin_v[k] = min(self.min_v[l], self.smin_v[r])
        else:
            self.min_v[k] = self.min_v[l]
            self.min_c[k] = self.min_c[l] + self.min_c[r]
            self.smin_v[k] = min(self.smin_v[l], self.smin_v[r])

    def _apply_add(self, k, x):
        if self.len[k] == 0:
            return
        self.sum[k] += x * self.len[k]
        self.max_v[k] += x
        self.min_v[k] += x
        if self.smax_v[k] != -self.INF:
            self.smax_v[k] += x
        if self.smin_v[k] != self.INF:
            self.smin_v[k] += x
        self.add[k] += x

    def _apply_chmin(self, k, x):
        if self.len[k] == 0 or self.max_v[k] <= x:
            return
        self.sum[k] += (x - self.max_v[k]) * self.max_c[k]
        if self.max_v[k] == self.min_v[k]:
            self.max_v[k] = self.min_v[k] = x
        elif self.max_v[k] == self.smin_v[k]:
            self.max_v[k] = self.smin_v[k] = x
        else:
            self.max_v[k] = x

    def _apply_chmax(self, k, x):
        if self.len[k] == 0 or self.min_v[k] >= x:
            return
        self.sum[k] += (x - self.min_v[k]) * self.min_c[k]
        if self.max_v[k] == self.min_v[k]:
            self.max_v[k] = self.min_v[k] = x
        elif self.min_v[k] == self.smax_v[k]:
            self.min_v[k] = self.smax_v[k] = x
        else:
            self.min_v[k] = x

    def _push(self, k):
        if k >= self.n:
            return
        l = k << 1
        r = l | 1
        if self.add[k] != 0:
            x = self.add[k]
            self._apply_add(l, x)
            self._apply_add(r, x)
            self.add[k] = 0
        pv_max = self.max_v[k]
        pv_min = self.min_v[k]
        if self.max_v[l] > pv_max:
            self._apply_chmin(l, pv_max)
        if self.max_v[r] > pv_max:
            self._apply_chmin(r, pv_max)
        if self.min_v[l] < pv_min:
            self._apply_chmax(l, pv_min)
        if self.min_v[r] < pv_min:
            self._apply_chmax(r, pv_min)

    def _push_to(self, k):
        for shift in range(self.h, 0, -1):
            self._push(k >> shift)

    def _rebuild_from(self, k):
        while k > 1:
            k >>= 1
            self._pull(k)

    def _prepare(self, l, r):
        l += self.n
        r += self.n
        ll = l // (l & -l)
        rr = r // (r & -r) - 1
        push = self._push
        for shift in range(ll.bit_length() - 1, 0, -1):
            push(ll >> shift)
        for shift in range(rr.bit_length() - 1, 0, -1):
            push(rr >> shift)
        return l, r, ll, rr

    def update_add(self, l, r, x):
        assert 0 <= l <= r <= self.n0
        if l == r or x == 0:
            return
        l, r, ll, rr = self._prepare(l, r)
        apply = self._apply_add
        while l < r:
            if l & 1:
                apply(l, x)
                l += 1
            if r & 1:
                r -= 1
                apply(r, x)
            l >>= 1
            r >>= 1
        self._rebuild_from(ll)
        self._rebuild_from(rr)

    def update_chmin(self, l, r, x):
        assert 0 <= l <= r <= self.n0
        if l == r:
            return
        l, r, ll, rr = self._prepare(l, r)
        stack = []
        while l < r:
            if l & 1:
                stack.append(l)
                l += 1
            if r & 1:
                r -= 1
                stack.append(r)
            l >>= 1
            r >>= 1
        max_v, smax_v = self.max_v, self.smax_v
        apply, push, pull = self._apply_chmin, self._push, self._pull
        while stack:
            k = stack.pop()
            if k < 0:
                pull(~k)
            elif max_v[k] <= x:
                continue
            elif smax_v[k] < x:
                apply(k, x)
            else:
                push(k)
                stack.append(~k)  # 子の処理後に再集計する印
                left = k << 1
                right = left | 1
                if max_v[right] > x:
                    stack.append(right)
                if max_v[left] > x:
                    stack.append(left)
        self._rebuild_from(ll)
        self._rebuild_from(rr)

    def update_chmax(self, l, r, x):
        assert 0 <= l <= r <= self.n0
        if l == r:
            return
        l, r, ll, rr = self._prepare(l, r)
        stack = []
        while l < r:
            if l & 1:
                stack.append(l)
                l += 1
            if r & 1:
                r -= 1
                stack.append(r)
            l >>= 1
            r >>= 1
        min_v, smin_v = self.min_v, self.smin_v
        apply, push, pull = self._apply_chmax, self._push, self._pull
        while stack:
            k = stack.pop()
            if k < 0:
                pull(~k)
            elif min_v[k] >= x:
                continue
            elif smin_v[k] > x:
                apply(k, x)
            else:
                push(k)
                stack.append(~k)
                left = k << 1
                right = left | 1
                if min_v[right] < x:
                    stack.append(right)
                if min_v[left] < x:
                    stack.append(left)
        self._rebuild_from(ll)
        self._rebuild_from(rr)

    def query_sum(self, l, r):
        assert 0 <= l <= r <= self.n0
        if l == r:
            return 0
        l, r, _, _ = self._prepare(l, r)
        values = self.sum
        res = 0
        while l < r:
            if l & 1:
                res += values[l]
                l += 1
            if r & 1:
                r -= 1
                res += values[r]
            l >>= 1
            r >>= 1
        return res

    def query_min(self, l, r):
        assert 0 <= l <= r <= self.n0
        if l == r:
            return self.INF
        l, r, _, _ = self._prepare(l, r)
        values = self.min_v
        res = self.INF
        while l < r:
            if l & 1:
                if values[l] < res:
                    res = values[l]
                l += 1
            if r & 1:
                r -= 1
                if values[r] < res:
                    res = values[r]
            l >>= 1
            r >>= 1
        return res

    def query_max(self, l, r):
        assert 0 <= l <= r <= self.n0
        if l == r:
            return -self.INF
        l, r, _, _ = self._prepare(l, r)
        values = self.max_v
        res = -self.INF
        while l < r:
            if l & 1:
                if values[l] > res:
                    res = values[l]
                l += 1
            if r & 1:
                r -= 1
                if values[r] > res:
                    res = values[r]
            l >>= 1
            r >>= 1
        return res

    def get(self, i):
        assert 0 <= i < self.n0
        k = i + self.n
        self._push_to(k)
        return self.sum[k]

    def set(self, i, x):
        assert 0 <= i < self.n0
        k = i + self.n
        self._push_to(k)
        self.sum[k] = x
        self.max_v[k] = self.min_v[k] = x
        self.smax_v[k] = -self.INF
        self.smin_v[k] = self.INF
        self.max_c[k] = self.min_c[k] = 1
        self.add[k] = 0
        self._rebuild_from(k)
