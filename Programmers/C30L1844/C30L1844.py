# %%
import numpy as np


def solution(maps):
    bfs = [(0, 0, 1)]
    for x, y, depth in bfs:
        if 0 <= x < len(maps[0]) and 0 <= y < len(maps) and maps[y][x] == 1:
            bfs.extend(((x + 1, y, depth + 1), (x, y + 1, depth + 1), (x - 1, y, depth + 1), (x, y - 1, depth + 1)))
            maps[y][x] = -depth
    return -maps[-1][-1]


print(solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]))

# print(solution([
#     [1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 1]
# ]))

# print(solution([
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1, 1, 1]
# ]))
# print(solution([
#     [1, 1, 0, 0, 0, 1, 1],
#     [1, 1, 1, 1, 1, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1, 1, 1]
# ]))
