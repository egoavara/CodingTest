# %%
"""2차원 행렬 메서드"""


class Mat:
    def __init__(self, row, col, default=0, format={'width': 4}) -> None:
        self._row = row
        self._col = col
        self._dat = list(default for _ in range(row * col))
        self._format = format

    def __format__(self, format_spec: str) -> str:
        pass

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col

    def __getitem__(self, key):
        if type(key) is tuple and len(key) == 2:
            return self._dat[key[1] * self.col + key[0]]
        else:
            raise KeyError('key type must be tuple len 2')

    def __setitem__(self, key, value):
        if type(key) is tuple and len(key) == 2:
            self._dat[key[1] * self.col + key[0]] = value
        else:
            raise KeyError('key type must be tuple len 2')

    def __str__(self) -> str:
        res = ""
        for y in range(self.row):
            if y != 0:
                res += '\n'
            for x in range(self.col):
                res += f"{self[x, y]:>{self._format['width']}}"
        return res


m = Mat(10, 10, default=-1)
print(m)
print()
m[2, 2] = 0
print(m)
print()

