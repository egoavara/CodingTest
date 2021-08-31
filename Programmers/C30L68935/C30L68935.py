# %%
import functools as ft
import itertools as it


def solution(n):
    return ft.reduce(
        lambda acc, e: acc + e[0] * e[1],
        zip(
            reversed(list(map(lambda e: e % 3, it.takewhile(lambda n: n > 0, it.accumulate(
                it.chain([n], it.repeat([1])), lambda acc, _: acc // 3))))),
            it.accumulate(
                it.count(1),
                lambda a, b: a * 3,
            )
        ),
        0
    )


print(solution(45))
