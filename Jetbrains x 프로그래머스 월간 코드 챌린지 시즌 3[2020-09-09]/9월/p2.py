# %%
from typing import overload


def solution(a, b, g, s, w, t):
    mn = 0
    mx = (a + b - 1) * max(t) * 2 + max(t)
    while True:
        md = (mx + mn) // 2
        mvd = [((md // t - 1) // 2 + 1) * m for m, t in zip(w, t)]
        print(md, mvd)
        gmvd = [min(m, eg) for m, eg in zip(mvd, g)]
        sgmvd = sum(gmvd)
        over_g = max(sgmvd - a, 0)
        gmvd = [e - over_g * () for e in gmvd]
        smvd = [min(m-mg, es) for m, mg, es in zip(mvd, gmvd, s)]
        if mx == mn:
            break
        print(mn, md, mx, ":", mvd, gmvd, smvd, over_g)
        if sum(gmvd) < a or sum(smvd) < b:
            if all((total - gold - silver) > 0 for total, gold, silver in zip(mvd, gmvd, smvd)):
                mx = md
            else:
                mn = md + 1
        else:
            mx = md
    return md


print(solution(10, 10, [100], [100], [7], [10]))
# print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
