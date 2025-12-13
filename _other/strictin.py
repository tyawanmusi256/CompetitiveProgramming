"""
厳密入力パーサー
競技プログラミングの入力を想定

- read_space(): 1文字以上の SPACE/TAB を要求して消費
- read_eoln():
    行末改行を要求して消費
- read_eof():
    EOF を要求
- read_token(name="token"):
    現在行から1トークンを空白か改行が来るまで読む
- read_int(name="int", lo=None, hi=None):
    1トークンを10進整数として読む（負数/範囲チェック可）
- read_string(name="s", min_len=None, max_len=None):
    1トークンを文字列として読む（長さチェック可）

使用例:
ins = StrictIn.from_stdin_ascii()
N = ins.read_int("N", lo=1, hi=200000, allow_sign=False)
ins.read_eoln()
s = ins.read_string("S", min_len=1, max_len=N)
ins.read_eoln()
ins.read_eof()
"""

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
        while (not self._eof()) and (self._peek() in (0x20, 0x09)):  # space/tab
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
        if t[:1] == b"-":
            x = -x
        if lo is not None and x < lo:
            self._err(f"int out of range: {x} < {lo}")
        if hi is not None and x > hi:
            self._err(f"int out of range: {x} > {hi}")
        return x

    def read_string(self, min_len: int | None = None,
                          max_len: int | None = None) -> str:

        s = self.read_token()

        if min_len is not None and len(s) < min_len:
            self._err(f"str too short: len={len(s)} < {min_len}")
        if max_len is not None and len(s) > max_len:
            self._err(f"str too long: len={len(s)} > {max_len}")

        return s