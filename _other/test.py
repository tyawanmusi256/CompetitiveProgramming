import sys

class InputError(Exception):
    pass

class StrictIn:

    def __init__(self, s: bytes, i: int = 0, line: int = 1, col: int = 1):
        self.s = s
        self.i = i
        self.line = line
        self.col = col

    @staticmethod
    def from_stdin_ascii() -> "StrictIn":
        raw = sys.stdin.buffer.read()
        for p, b in enumerate(raw):
            if b >= 0x80:
                raise InputError(f"non-ASCII byte at offset {p}: 0x{b:02x}")
            if b in (0x09, 0x0A, 0x0D):
                continue
            if 0x20 <= b <= 0x7E:
                continue
            raise InputError(f"disallowed control byte at offset {p}: 0x{b:02x}")
        return StrictIn(raw)

    def _eof(self) -> bool:
        return self.i >= len(self.s)

    def _peek(self):
        return None if self._eof() else self.s[self.i]

    def _advance(self) -> int:
        if self._eof():
            self._err("unexpected EOF")
        b = self.s[self.i]
        self.i += 1
        if b == 0x0A:
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return b

    def _err(self, msg: str) -> None:
        raise InputError(f"{msg} (line {self.line}, col {self.col})")

    def _consume_newline(self) -> None:
        b = self._peek()
        if b == 0x0A:
            self._advance()
            return
        if b == 0x0D:
            self._advance()
            if self._peek() != 0x0A:
                self._err("bare CR is not allowed (use LF or CRLF)")
            self._advance()
            self.line += 1
            self.col = 1
            return
        self._err("expected EOL")

    def skip_spaces(self) -> None:
        while (not self._eof()) and (self._peek() in (0x20, 0x09)):
            self._advance()

    def skip_ws(self) -> None:
        while not self._eof():
            b = self._peek()
            if b in (0x20, 0x09):
                self._advance()
            elif b in (0x0A, 0x0D):
                self._consume_newline()
            else:
                break

    def read_space(self) -> None:
        b = self._peek()
        if b not in (0x20, 0x09):
            self._err("expected SPACE/TAB")
        while (not self._eof()) and (self._peek() in (0x20, 0x09)):
            self._advance()

    def read_eoln(self) -> None:
        self._consume_newline()

    def read_eof(self) -> None:
        if not self._eof():
            self._err("expected EOF (extra data exists)")

    def read_token(self) -> str:
        b = self._peek()
        if b is None:
            self._err(f"unexpected EOF while reading token")
        if b in (0x20, 0x09):
            self._err(f"unexpected leading SPACE/TAB while reading token")
        if b in (0x0A, 0x0D):
            self._err(f"unexpected EOL while reading token")

        start = self.i
        while not self._eof():
            b = self._peek()
            if b in (0x20, 0x09, 0x0A, 0x0D):
                break
            self._advance()
        return self.s[start:self.i].decode("ascii")

    def read_int(self, lo=None, hi=None) -> int:
        t_str = self.read_token()
        t = t_str.encode("ascii")

        if t[:1] == b"-":
            body = t[1:]
            if len(body) == 0:
                self._err(f"int is not an integer")
        else:
            body = t

        if len(body) == 0 or (not all(48 <= c <= 57 for c in body)):
            self._err(f"int is not a base-10 integer")

        x = int(t_str)
        if lo is not None and x < lo:
            self._err(f"int out of range: {x} < {lo}")
        if hi is not None and x > hi:
            self._err(f"int out of range: {x} > {hi}")
        return x

    def read_string(self, min_len: int | None = None, max_len: int | None = None) -> str:

        s = self.read_token()

        if min_len is not None and len(s) < min_len:
            self._err(f"str too short: len={len(s)} < {min_len}")
        if max_len is not None and len(s) > max_len:
            self._err(f"str too long: len={len(s)} > {max_len}")

        return s

ins = StrictIn.from_stdin_ascii()

s = ins.read_string()
ins.read_eoln()
n = len(s)
assert 2 <= n <= 200000

# 括弧列を木構造に変換する
# 対応する括弧のペアを同じ頂点とみなし、括弧の深さ=頂点の深さ、括弧の内包関係=親子関係とみなす
# 仮想根を 0 として、頂点番号は 1 から始める
pair = n // 2
parent = [0] * (pair + 1)
deg = [0] * (pair + 1) # deg[i] = 頂点 i の子の数
idx = [0] * (pair + 1) # idx[i] = 頂点 i がその親の子の中で左から何番目か (1-indexed)
pair_id = [0] * (n + 1)

# 括弧列から木構造を構築
cur = 0
next = 1
check = 0
for i in range(1, n + 1):
    assert s[i - 1] in '()'
    if s[i - 1] == '(':
        check += 1
        node = next
        next += 1
        parent[node] = cur
        deg[cur] += 1
        idx[node] = deg[cur]
        pair_id[i] = node
        cur = node
    else:
        check -= 1
        assert check >= 0
        pair_id[i] = cur
        cur = parent[cur]
assert check == 0

# 子から親へ移動する際のコストを計算
# 親-子1-子2-...-親のようなサイクルが存在するため、子から親へのコストは idx[i] と deg[p] - idx[i] + 1 の小さい方
to_p_cost = [0] * (pair + 1)
for i in range(1, pair + 1):
    p = parent[i]
    if p == 0:
        # 仮想根まわりはクエリ処理の際に別途考慮する
        to_p_cost[i] = 0
    else:
        to_p_cost[i] = min(idx[i], deg[p] - idx[i] + 1)
        
depth = [0] * (pair + 1) # depth[i] = 頂点 i の深さ
dist = [0] * (pair + 1) # dist[i] = 仮想根から頂点 i までの距離
for i in range(1, pair + 1):
    p = parent[i]
    depth[i] = depth[p] + 1
    dist[i] = dist[p] + to_p_cost[i]
    
# LCA
lca_num = pair.bit_length()
double = [[0] * (pair + 1) for _ in range(lca_num)]
for i in range(1, pair + 1):
    double[0][i] = parent[i]
for i in range(1, lca_num):
    for j in range(pair + 1):
        double[i][j] = double[i - 1][double[i - 1][j]]

def get_lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for i in range(lca_num):
        if (diff >> i) & 1:
            u = double[i][u]
    if u == v:
        return u
    for i in range(lca_num - 1, -1, -1):
        if double[i][u] != double[i][v]:
            u = double[i][u]
            v = double[i][v]
    return double[0][u]

# u の祖先であり、a を親に持つ頂点を取得する関数 u - ... - ans - ancestor
def get_child_ancestor(u, a):
    diff = depth[u] - depth[a] - 1
    for i in range(lca_num):
        if (diff >> i) & 1:
            u = double[i][u]
    return u

# クエリ処理
q = ins.read_int(1, 200000)
ins.read_eoln()
for _ in range(q):
    l = ins.read_int(1, n)
    ins.read_space()
    r = ins.read_int(1, n)
    ins.read_eoln()
    assert l != r

    u = pair_id[l]
    v = pair_id[r]

    # u と v が同じ頂点に対応する場合
    if u == v:
        print(0)
        continue
    
    lca = get_lca(u, v)

    if u == lca:
        # v が u の子孫にある場合、そのまま距離の差が答え
        ans = dist[v] - dist[u]
    elif v == lca:
        # 同様
        ans = dist[u] - dist[v]
    else:
        # u と v が別々の枝にある場合、 lca を経由する場合と、 lca を含むサイクル上を横移動する場合を考慮する必要がある
        uu = get_child_ancestor(u, lca)
        vv = get_child_ancestor(v, lca)

        # lca の直下の子まで登るコスト
        ans = dist[u] - dist[uu]
        ans += dist[v] - dist[vv]
        
        # lca を含むサイクル上での横移動コスト
        diff = abs(idx[uu] - idx[vv])
        if lca == 0:
            # lca が仮想根の場合、サイクル上の横移動しか行えない
            ans += diff
        else:
            ans += min(diff, deg[lca] + 1 - diff)

    print(ans)
ins.read_eof()
