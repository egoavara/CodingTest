# %%
# 다중 코어
import multiprocessing as mp
import itertools as it
import timeit
import numpy as np

# %%

import itertools as it


def solution(board, skill):
    CHUNKW = 2
    CHUNKH = 2
    bw = len(board[0])
    bh = len(board)
    cw = (bw + CHUNKW-1) // CHUNKW
    ch = (bh + CHUNKH-1) // CHUNKH
    chunk = [[0] * cw for _ in range(ch)]
    for tp, r0, c0, r1, c1, deg in skill:
        #
        deg = deg if tp == 2 else -deg
        #
        cr0 = r0 // CHUNKH
        cr1 = (r1+1) // CHUNKH
        cc0 = c0 // CHUNKW
        cc1 = (c1+1) // CHUNKW
        # print(r0, r1, c0, c1, deg)
        # print(cr0, cr1, cc0, cc1)
        for cy in range(cr0, cr1+1):
            for cx in range(cc0, cc1+1):
                print("C", cx, cy)
                chunk[cy][cx] += deg
        #
        for y in it.chain(range(r0, cr0 * CHUNKH), range(cr1 * CHUNKH, r1+1)):
            for x in it.chain(range(c0, cc0 * CHUNKH), range(cc1 * CHUNKH, c1+1)):
                board[y][x] += deg
    for cy in range(ch):
        for cx in range(cw):
            cval = chunk[cy][cx]
            for y in range(CHUNKH * cy, min(CHUNKH * (cy+1), bh)):
                for x in range(CHUNKW * cx, min(CHUNKW * (cx+1), bw)):
                    board[y][x] += cval
    # print(np.array(board))
    # print(np.array(chunk))
    return sum(1 for line in board for building in line if building > 0)


# print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [
#       [1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [
    #   [1, 1, 1, 2, 2, 4],
    #   [1, 0, 0, 1, 1, 2],
      [2, 2, 0, 2, 0, 100]
      ]))
# %%


def solution(board, skill):
    group = {}
    for tp, r0, c0, r1, c1, deg in skill:
        if (r0, c0, r1, c1) not in group:
            group[(r0, c0, r1, c1)] = 0
        group[(r0, c0, r1, c1)] += deg if tp == 2 else -deg
    #
    for (r0, c0, r1, c1), deg in group.items():
        for y in range(r0, r1+1):
            for x in range(c0, c1+1):
                board[y][x] += deg
    # print(np.array(board))
    return sum(1 for line in board for building in line if building > 0)


print('timeit : ', timeit.timeit(lambda: solution(
    [[0] * 1000] * 1000,
    [[1, 0, 0, 999, 999, 2]]*100
), number=1))

# %%


def solution(board, skill):
    for tp, r0, c0, r1, c1, deg in skill:
        for y in range(r0, r1+1):
            for x in range(c0, c1+1):
                board[y][x] += deg if tp == 2 else -deg
    print(np.array(board))
    return sum(1 for line in board for building in line if building > 0)


print('timeit : ', timeit.timeit(lambda: solution(
    [[0] * 1000] * 1000,
    [[1, 0, 0, 999, 999, 2]]*100
), number=1))
