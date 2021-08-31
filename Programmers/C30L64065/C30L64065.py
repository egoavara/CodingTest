# %%
import re
import functools as ft


def solution(s):
    return ft.reduce(
        lambda acc, e: [*acc, *(e - set(acc))],
        sorted(
            [{int(n.group()) for n in re.finditer(r'[1-9][0-9]*', l.group())}
             for l in re.finditer(r'{[1-9][0-9]*(,[1-9][0-9]*)*}', s)],
            key=lambda e: len(e)
        ),
        []
    )


# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
