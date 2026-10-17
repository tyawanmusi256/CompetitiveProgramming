# PointClass: 2次元の点・ベクトル（x, y は int または float）
# PointClass(x=0, y=0): 座標を保持。p.x, p.y は変更可能。
# p + q / p - q / -p: 座標ごとの加算・減算・符号反転
# p * k / k * p / p / k: スカラー倍・除算（除算は float、k != 0）
# p.dot(q): 内積 x1*x2 + y1*y2
# p.cross(q): 外積 x1*y2 - y1*x2（q が p の反時計回り側なら正）
# p.norm2() / p.norm(): 原点からの距離の二乗 / 距離
# p.distance2(q) / p.distance(q): 2点間の距離の二乗 / 距離
# p == q: 座標の完全一致。p < q: (x, y) の辞書順。
# x, y = p: 座標の取り出し。各演算は O(1)（整数の桁数を定数とみなす）。
# 演算は新しい点を返し、元の点を変更しない。可変なので set/dict のキーには使えない。
# 整数座標の加減算・整数倍・内積・外積・距離の二乗は整数のまま計算する。
# float の比較には誤差を含む。許容誤差は問題に応じて呼び出し側で扱う。
#
# 使用例:
# p, q = PointClass(3, 4), PointClass(1, 2)
# p + q                 # PointClass(4, 6)
# 2 * p                 # PointClass(6, 8)
# p.dot(q), p.cross(q)   # (11, 2)
# p.norm2(), p.norm()    # (25, 5.0)
# p.distance2(q)        # 8
# sorted([p, q])        # [PointClass(1, 2), PointClass(3, 4)]
#
# 幾何関数（引数の点はすべて PointClass）:
# ccw(a, b, p): a→b に対する p の位置。a != b が必要。
#   1: 反時計回り、-1: 時計回り、2: a の後方、-2: b より先、0: 線分上
# projection(a, b, p): 直線 ab への p の射影。a != b が必要。
# reflection(a, b, p): 直線 ab に関して p と対称な点。a != b が必要。
# segments_intersect(a, b, c, d): 線分 ab と cd が共有点を持つか。
# distance_to_segment(a, b, p): 点 p と線分 ab の最短距離。
# segment_distance(a, b, c, d): 2線分間の最短距離。
# polygon_area2(points): 周回順の頂点列から、符号付き面積の2倍を計算。
#   反時計回りで正。面積は abs(polygon_area2(points)) / 2。
#   自己交差しない多角形を想定。3頂点未満は 0、末尾の始点の重複は不要。
# 線分は両端点を含む。交差判定・距離は長さ0の線分にも対応。
# ccw・射影・反射で a == b の場合は ValueError。
# 面積は O(n)、ほかは O(1)。入力の点・頂点列は変更しない。
# 判定は誤差許容なし（整数座標なら厳密）。浮動小数点では問題に応じて調整する。
# 射影・反射・距離は float を使用する。
#
# a, b, p = PointClass(0, 0), PointClass(2, 0), PointClass(1, 3)
# ccw(a, b, p)                           # 1
# projection(a, b, p)                    # PointClass(1.0, 0.0)
# reflection(a, b, p)                    # PointClass(1.0, -3.0)
# segments_intersect(a, b, p, PointClass(1, -1))  # True
# distance_to_segment(a, b, p)           # 3.0
# segment_distance(a, b, p, PointClass(2, 3))    # 3.0
# polygon_area2([a, b, p])               # 6
#
# 検証問題（提出コード: _other/point_geometry/）:
# AOJ CGL_1_C「反時計回り」: ccw
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_C&lang=ja
# AOJ CGL_1_A「射影」: projection
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_A&lang=ja
# AOJ CGL_1_B「反射」: reflection
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_B
# AOJ CGL_2_B「交差判定」: segments_intersect
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_B
# AOJ CGL_2_D「距離」: segment_distance / distance_to_segment
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_D
# AOJ CGL_3_A「面積」: polygon_area2
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_3_A&lang=ja
# 提出 URL・実行時間: 未提出・AC 未確認

from math import hypot


class PointClass:
    __slots__ = ["x", "y"]

    def __init__(self, x: int | float = 0, y: int | float = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PointClass({self.x!r}, {self.y!r})"

    def __iter__(self):
        yield self.x
        yield self.y

    def __eq__(self, other):
        if not isinstance(other, PointClass):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if not isinstance(other, PointClass):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)

    def __add__(self, other):
        if not isinstance(other, PointClass):
            return NotImplemented
        return PointClass(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, PointClass):
            return NotImplemented
        return PointClass(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return PointClass(-self.x, -self.y)

    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return PointClass(self.x * k, self.y * k)

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return PointClass(self.x / k, self.y / k)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def norm2(self):
        return self.x * self.x + self.y * self.y

    def norm(self):
        return hypot(self.x, self.y)

    def distance2(self, other):
        dx, dy = self.x - other.x, self.y - other.y
        return dx * dx + dy * dy

    def distance(self, other):
        return hypot(self.x - other.x, self.y - other.y)


def ccw(a, b, p):
    if a == b:
        raise ValueError("ccw requires distinct endpoints")
    ab, ap = b - a, p - a
    cross = ab.cross(ap)
    if cross > 0:
        return 1
    if cross < 0:
        return -1
    if ab.dot(ap) < 0:
        return 2
    if ab.norm2() < ap.norm2():
        return -2
    return 0


def projection(a, b, p):
    if a == b:
        raise ValueError("projection requires distinct endpoints")
    ab = b - a
    return a + ab * ((p - a).dot(ab) / ab.norm2())


def reflection(a, b, p):
    return p + (projection(a, b, p) - p) * 2


def segments_intersect(a, b, c, d):
    if max(a.x, b.x) < min(c.x, d.x) or max(c.x, d.x) < min(a.x, b.x):
        return False
    if max(a.y, b.y) < min(c.y, d.y) or max(c.y, d.y) < min(a.y, b.y):
        return False
    ab, cd = b - a, d - c
    s, t = ab.cross(c - a), ab.cross(d - a)
    u, v = cd.cross(a - c), cd.cross(b - c)
    return ((s <= 0 <= t or t <= 0 <= s)
            and (u <= 0 <= v or v <= 0 <= u))


def distance_to_segment(a, b, p):
    ab, ap = b - a, p - a
    if a == b or ab.dot(ap) <= 0:
        return p.distance(a)
    if ab.dot(p - b) >= 0:
        return p.distance(b)
    return abs(ab.cross(ap)) / ab.norm()


def segment_distance(a, b, c, d):
    if segments_intersect(a, b, c, d):
        return 0.0
    return min(distance_to_segment(a, b, c), distance_to_segment(a, b, d),
               distance_to_segment(c, d, a), distance_to_segment(c, d, b))


def polygon_area2(points):
    n = len(points)
    if n < 3:
        return 0
    origin = points[0]
    # 原点を最初の頂点に移し、大きな平行移動による float の桁落ちを抑える。
    return sum((points[i] - origin).cross(points[i + 1] - origin)
               for i in range(1, n - 1))
