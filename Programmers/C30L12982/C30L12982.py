# %%
import functools as ft
import itertools as it


def solution(d, budget):
    return ft.reduce(
        lambda acc, ie: ie[0]+1,
        enumerate(it.takewhile(lambda x: x <= budget, it.accumulate(sorted(d)))),
        0
    )


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2,2,3,3], 10))
print(solution([2,2,3,3], 0))
