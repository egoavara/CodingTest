# %%
import functools as ft


def solution(left, right):
    return ft.reduce(
        lambda acc, bet: acc +
        bet if len([i for i in range(1, bet+1) if bet %
                   i == 0]) % 2 == 0 else acc - bet,
        range(left, right+1),
        0
    )


solution(13, 17)
solution(24, 27)
