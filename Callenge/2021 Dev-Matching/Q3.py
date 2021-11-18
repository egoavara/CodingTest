# %%
import numpy as np


def connect_at(table, r, c):
    def recur(r, c, target, visited):
        if not 0 <= r < 6 or not 0 <= c < 6:
            return
        if table[r][c] == target and (r, c) not in visited:
            visited.add((r, c))
            recur(r-1, c, target, visited)
            recur(r+1, c, target, visited)
            recur(r, c-1, target, visited)
            recur(r, c+1, target, visited)
    res = set()
    recur(r, c, table[r][c], res)
    return res


def gravity(table):
    for c in range(6):
        for bot in reversed(range(6)):
            if table[bot][c] == 0:
                break
        for r in reversed(range(bot)):
            table[bot][c] = table[r][c]
            table[r][c] = 0
            if table[bot][c] != 0:
                bot -= 1
def validate(table):
    remd = False
    for r in range(6):
        for c in range(6):
            if table[r][c] == 0:
                continue
            cnts = connect_at(table, r, c)
            if len(cnts) >= 3:
                remd = True
                for remr, remc in cnts:
                    table[remr][remc] = 0
                gravity(table)
    if remd:
        validate(table)

def solution(macaron):
    table = [[0 for _ in range(6)] for _ in range(6)]
    for mloc, mclr in macaron:
        table[0][mloc -1] = mclr
        gravity(table)
        validate(table)
    return ["".join(str(e)for e in l) for l in table]


print(solution([[1, 1], [2, 1], [1, 2], [3, 3], [
      6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]]))
