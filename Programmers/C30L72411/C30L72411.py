# %%
import functools as ft
import itertools as it


def solution(orders, course):
    orders = [{m for m in each} for each in orders]

    def reduce_menus(acc, e):
        used = sum((1 for o in orders if set(e).issubset(o)))
        if used < 2:
            return acc
        elif used == acc[1]:
            return ([*acc[0], e], acc[1])
        elif used > acc[1]:
            return ([e], used)
        else:
            return acc
    return sorted(set(
        ''.join((str(c) for c in sorted(tp)))
        for ln in (
            ft.reduce(
                reduce_menus,
                (
                    comb
                    for od in orders
                    for comb in it.combinations(od, c)
                ),
                ([], 0)
            ) for c in course
        )
        for tp in ln[0]
    ))


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
