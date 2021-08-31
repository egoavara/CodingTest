# %% 플로이드-와샬
import numpy as np
import math
import itertools as it

from numpy.lib.function_base import copy


def solution(N, road, K):
    table = [
        [math.inf for _ in range(N)]
        for _ in range(N)
    ]

    for a, b, l in road:
        table[a-1][b-1] = min(table[a-1][b-1], l)
        table[b-1][a-1] = min(table[b-1][a-1], l)
    for k in range(N):
        for a, b in it.permutations(range(N), 2):
            d = table[a][k] + table[k][b]
            table[a][b] = min(table[a][b], d)
            table[b][a] = min(table[b][a], d)
    return sum((
        1 for dst in range(N)
        if -1 != table[0][dst] <= K
    ))+1


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
      [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
# %% 다익스트라


def solution(N, road, K):
    table = [
        [math.inf for j in range(N)]
        for i in range(N)
    ]

    for a, b, l in road:
        table[a-1][b-1] = min(table[a-1][b-1], l)
        table[b-1][a-1] = min(table[b-1][a-1], l)
    distances = [0, *(math.inf for _ in range(N-1))]
    destinations = [(0, 0)]
    while len(destinations) > 0:
        dest, dist = destinations.pop(0)
        for ndest, ndist in enumerate(table[dest]):
            if dist + ndist < distances[ndest]:
                distances[ndest] = dist + ndist
                destinations.append((ndest, dist + ndist))
    return sum((1 for d in distances if d <= K))


# print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
#       [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))

print(solution(7,
               [[1, 2, 4],
                [1, 3, 1],
                [3, 4, 1],
                [4, 2, 1],
                [2, 5, 1], ],
               4)
      )

