# %%
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

from dataclasses import dataclass
from typing import List, Literal, Optional
import itertools as it


@dataclass
class ShapeGraph:
    L: Optional['ShapeGraph']
    R: Optional['ShapeGraph']
    T: Optional['ShapeGraph']
    B: Optional['ShapeGraph']

    def isIn_0(self, dst, i, x, y, w, h):
        if not (0 <= x < w) or not (0 <= y < h) or dst[y][x] != i:
            return False
        if self.T is not None:
            if not self.T.isIn_0(dst, i, x, y-1, w, h):
                return False
        if self.R is not None:
            if not self.R.isIn_0(dst, i, x+1, y, w, h):
                return False
        if self.B is not None:
            if not self.B.isIn_0(dst, i, x, y+1, w, h):
                return False
        if self.L is not None:
            if not self.L.isIn_0(dst, i, x-1, y, w, h):
                return False
        return True

    def isIn_90(self, dst, i, x, y, w, h):
        if not (0 <= x < w) or not (0 <= y < h) or dst[y][x] != i:
            return False

        if self.T is not None:
            if not self.T.isIn_90(dst, i, x+1, y, w, h):
                return False
        if self.R is not None:
            if not self.R.isIn_90(dst, i, x, y+1, w, h):
                return False
        if self.B is not None:
            if not self.B.isIn_90(dst, i, x-1, y, w, h):
                return False
        if self.L is not None:
            if not self.L.isIn_90(dst, i, x, y-1, w, h):
                return False
        return True

    def isIn_180(self, dst, i, x, y, w, h):
        if not (0 <= x < w) or not (0 <= y < h) or dst[y][x] != i:
            return False

        if self.T is not None:
            if not self.T.isIn_180(dst, i, x, y+1, w, h):
                return False
        if self.R is not None:
            if not self.R.isIn_180(dst, i, x-1, y, w, h):
                return False
        if self.B is not None:
            if not self.B.isIn_180(dst, i, x, y-1, w, h):
                return False
        if self.L is not None:
            if not self.L.isIn_180(dst, i, x+1, y, w, h):
                return False
        return True

    def isIn_270(self, dst, i, x, y, w, h):
        if not (0 <= x < w) or not (0 <= y < h) or dst[y][x] != i:
            return False

        if self.T is not None:
            if not self.T.isIn_270(dst, i, x-1, y, w, h):
                return False
        if self.R is not None:
            if not self.R.isIn_270(dst, i, x, y-1, w, h):
                return False
        if self.B is not None:
            if not self.B.isIn_270(dst, i, x+1, y, w, h):
                return False
        if self.L is not None:
            if not self.L.isIn_270(dst, i, x, y+1, w, h):
                return False
        return True


@dataclass
class Shape:
    root: ShapeGraph
    nodes: List[ShapeGraph]
    size: int

    @classmethod
    def init(cls, board, n) -> Optional['Shape']:
        w, h = len(board[0]), len(board)
        first = next(((x, y) for y in range(h)
                      for x in range(w) if board[y][x] == n), None)
        if first == None:
            return None
        q = [(first)]
        p = [ShapeGraph(None, None, None, None)]
        i = 0
        while i < len(q):
            x, y = q[i]
            if x + 1 < w and (x + 1, y) not in q and board[y][x + 1] == n:
                q.append((x + 1, y))
                p.append(ShapeGraph(None, None, None, None))
                p[i].R = p[-1]
            if y + 1 < h and (x, y + 1) not in q and board[y + 1][x] == n:
                q.append((x, y + 1))
                p.append(ShapeGraph(None, None, None, None))
                p[i].B = p[-1]
            if x - 1 >= 0 and (x - 1, y) not in q and board[y][x - 1] == n:
                q.append((x - 1, y))
                p.append(ShapeGraph(None, None, None, None))
                p[i].L = p[-1]
            if y - 1 >= 0 and (x, y - 1) not in q and board[y - 1][x] == n:
                q.append((x, y - 1))
                p.append(ShapeGraph(None, None, None, None))
                p[i].T = p[-1]
            i += 1
        return Shape(p[0], p, len(q))

    def isFit(self, dst, i, stat) -> bool:
        if self.size != stat[i]:
            return False
        w, h = len(dst[0]), len(dst)
        for y, x in it.product(range(h), range(w)):
            if dst[y][x] == i and any((self.root.isIn_0(dst, i, x, y, w, h),
                                       self.root.isIn_90(dst, i, x, y, w, h),
                                       self.root.isIn_180(dst, i, x, y, w, h),
                                       self.root.isIn_270(dst, i, x, y, w, h))):
                return True
        return False


def union(mapping, a, b):
    a = find(mapping, a)
    b = find(mapping, b)
    mapping[find(mapping, min(a, b))] = find(mapping, max(a, b))


def find(mapping, a):
    if mapping[a] == a:
        return a
    mapping[a] = find(mapping, mapping[a])
    return mapping[a]


def categorize(tb, non_target=0, replacing=False):
    res = [[0 for __ in _]for _ in tb]
    mapping = dict()
    gen_id = 1
    for y in range(len(tb)):
        for x in range(len(tb[0])):
            if tb[y][x] == non_target:
                continue
            top_id = res[y-1][x] if y > 0 else 0
            left_id = res[y][x-1] if x > 0 else 0
            if top_id == left_id == 0:
                res[y][x] = gen_id
                mapping[gen_id] = gen_id
                gen_id += 1
            elif top_id == left_id:
                res[y][x] = top_id
            elif top_id == 0:
                res[y][x] = left_id
            elif left_id == 0:
                res[y][x] = top_id
            else:
                res[y][x] = top_id
                union(mapping, top_id, left_id)
    stat = None
    if replacing:
        stat = {k: 0 for k, v in mapping.items() if k == v}
        for y in range(len(tb)):
            for x in range(len(tb[0])):
                if res[y][x] != 0:
                    res[y][x] = find(mapping, res[y][x])
                    stat[res[y][x]] += 1
    return res, mapping, stat


def solution(game_board, table):
    block_map, mbck, _ = categorize(table, replacing=True)
    board_map, mbrd, stat = categorize(
        game_board, non_target=1, replacing=True)
    blocks = {k: Shape.init(block_map, k) for k, v in mbck.items() if k == v}
    availables = {
        ibnk: [ibck for ibck, bck in blocks.items(
        ) if bck.isFit(board_map, ibnk, stat)]
        for ibnk, p in mbrd.items() if ibnk == p
    }
    unused = set(blocks.keys())
    result = 0
    for ibnk, ibcks in availables.items():
        if (trg := next((i for i in ibcks if i in unused), None)) is not None:
            unused.discard(trg)
            result += blocks[trg].size
    return result


print(solution(
    [[1, 1, 0, 0, 1, 0],
     [0, 0, 1, 0, 1, 0],
     [0, 1, 1, 0, 0, 1],
     [1, 1, 0, 1, 1, 1],
     [1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 0]],
    [[1, 0, 0, 1, 1, 0],
     [1, 0, 1, 0, 1, 0],
     [0, 1, 1, 0, 1, 1],
     [0, 0, 1, 0, 0, 0],
     [1, 1, 0, 1, 1, 0],
     [0, 1, 0, 0, 0, 0]]
))
# print(solution(
#     [[0, 0, 1],
#      [0, 0, 1],
#      [0, 0, 1]],
#     [[0, 1, 1],
#      [0, 1, 1],
#      [0, 1, 1]]
# ))
# print(solution(
#     [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#      [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
#      [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
#      [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#      [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
#      [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
#      [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
#      [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
#      [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
#      [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
#      [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
#     [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
#      [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
#      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
#      [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
#      [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
#      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#      [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
#      [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
#      [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
#      [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
#      [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
#      [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]
# ))
# %%
