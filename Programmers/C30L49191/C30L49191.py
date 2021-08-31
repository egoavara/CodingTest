# %%
import itertools as it
import math
import numpy as np
import functools as ft


def solution(n, results):
    table = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    def setup(tb, winner, loser):
        if tb[winner][loser] != 0:
            return
        tb[winner][loser] = 1
        tb[loser][winner] = -1
        for i in range(n):
            if tb[winner][i] == -1:
                setup(tb, i, loser)
        for i in range(n):
            if tb[loser][i] == 1:
                setup(tb, winner, i)
    for a, b in results:
        setup(table, a-1, b-1)
    return sum((
        1
        for i in range(n)
        if sum(map(lambda e: abs(e), table[i])) == n - 1
    ))


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(4, [[1, 2], [3, 4]]))
print(solution(4, [[1, 2], [3, 4], [2, 3]]))
print(solution(5, [[1, 2], [3, 4], [2, 3]]))

# %%


def floyd_warshall(table, n, kernel=lambda ori, a, b: min(ori, a + b)):
    for k in range(n):
        for a, b in it.permutations(range(n), 2):
            if k == a or k == b:
                continue
            table[a][b] = kernel(table[a][b], table[a][k], table[k][b])


def solution(n, results):
    table = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for a, b in results:
        table[a-1][b-1] = 1
        table[b-1][a-1] = -1
    floyd_warshall(table, n, 
        kernel= lambda ori, a, b : a if a != 0 and a == b else ori
    )
    return sum((
        1
        for i in range(n)
        if sum(map(lambda e: abs(e), table[i])) == n - 1
    ))


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(4, [[1, 2], [3, 4]]))
# print(solution(4, [[1, 2], [3, 4], [2, 3]]))
