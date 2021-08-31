# %%
import functools as ft
import itertools as it


def solution(n, a, b):
    return ft.reduce(
        lambda acc, e:
            (acc[0] + acc[0] % e, acc[1] + acc[1] % e, acc[2] + 1)
            if acc[0] != acc[1] else acc,
        it.takewhile(lambda e: e <= n, (2 ** n for n in it.count(1))),
        (a, b, 0)
    )[2]


print(solution(8, 4, 7))
print(solution(8, 4, 7))
