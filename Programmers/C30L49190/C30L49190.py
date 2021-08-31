# %%

import numpy as np
import itertools as it


def delta(k, m, n, dx, dy):
    for y, x in it.product(range(m), range(m)):
        rx = x - dx
        ry = y - dy
        if 0 <= rx < n and 0 <= ry < n:
            yield k[ry][rx]
        else:
            yield 0
    return


def solution(key, lock):
    n = len(lock)
    m = len(key)
    krots = [
        key,
        list(zip(*reversed(key))),
        list(map(lambda e:list(reversed(e)), reversed(key))),
        list(map(lambda e:list(reversed(e)), reversed(list(zip(*reversed(key)))))),
    ]
    #
    for dy, dx in it.product(range(-m+1,n), range(-m+1, n)):
        for k in krots:
            if all(map(lambda ab: ab[0] ^ ab[1], zip(it.chain(*lock), delta(k, n, m, dx, dy)))):
                return True
    return False


# print(solution(
#     [[0, 0, 0],
#      [1, 0, 0],
#      [0, 1, 1]],
#     [[1, 1, 1],
#      [1, 1, 0],
#      [1, 0, 1]]
# ))
print(solution(
    [[0, 0],
     [0, 1]],
    [[1, 1, 1, 1],
     [1, 1, 0, 1],
     [1, 0, 1, 1],
     [1, 1, 1, 1]]
))
# %%
