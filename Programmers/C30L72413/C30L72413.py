# %%
import math
import numpy as np
import itertools as it


def floyd_warshall(n, arr):
    for middle in range(n):
        for begin in range(n):
            for end in range(n):
                if arr[begin][end] > arr[begin][middle] + arr[middle][end]:
                    arr[begin][end] = arr[begin][middle] + arr[middle][end]


def solution(n, s, a, b, fares):
    edges = [[(math.inf if i != j else 0) for j in range(n)] for i in range(n)]
    for (src, dst, lng) in fares:
        edges[src-1][dst-1] = lng
        edges[dst-1][src-1] = lng
    floyd_warshall(n, edges)
    return min(edges[s-1][m] + edges[m][a-1] + edges[m][b-1] for m in range(n))


print(solution(
    6, 4, 6, 2,
    [[4, 1, 10],
     [3, 5, 24],
     [5, 6, 2],
     [3, 1, 41],
     [5, 1, 24],
     [4, 6, 50],
     [2, 4, 66],
     [2, 3, 22],
     [1, 6, 25]]
))
