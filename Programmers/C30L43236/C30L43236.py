# %%
import itertools as it

def solution(distance, rocks, n):
    rocks = sorted(rocks)
    rocks = list((i - j for i, j in zip(
        it.chain(rocks, [distance]),
        it.chain([0], rocks),
    )))
    mn = 1
    mx = distance
    while mn < mx:
        md = (mx + mn) // 2
        copyed = list(rocks)
        delcnt = 0
        for _ in range(n):
            iv = next(it.dropwhile(
                lambda e: e[1] > md, filter(lambda iv: iv[1] != -1, enumerate(copyed))), None)
            if iv == None:
                break
            if iv[0] + 1 < len(copyed):
                copyed[iv[0] + 1] += copyed[iv[0]]
            else:
                copyed[iv[0] - 1] += copyed[iv[0]]
            copyed[iv[0]] = -1
            delcnt += 1

        if delcnt != n:
            mn = md + 1
        elif min(filter(lambda v: v != -1, copyed)) > md:
            mn = md + 1
        else:
            mx = md
    return mn



def gen_dist(*dists):
    return it.islice(it.accumulate(dists), len(dists)-1)


print(solution(25, [2, 14, 11, 21, 17], 2))
print(solution(25, gen_dist(2, 9, 3, 4, 3, 4), 2))
