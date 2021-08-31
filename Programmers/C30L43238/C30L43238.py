# %%
def prev_sol(n, times):
    tt = [t * (n // len(times) + (1 if i < n % len(times) else 0))
          for i, t in enumerate(times)]
    while (True):
        cmxi, cmx = max(enumerate(tt), key=lambda a: a[1])
        nmni, nmn = min(
            enumerate(map(lambda ab: ab[0] + ab[1], zip(times, tt))), key=lambda a: a[1])
        if cmx > nmn:
            tt[cmxi] -= times[cmxi]
            tt[nmni] += times[nmni]
        else:
            break
    return max(tt)


def solution(n, times):
    mnt, mxt = 0, max(times) * n
    while (mnt < mxt):
        mdt = (mxt + mnt) // 2
        nxt = sum(map(lambda t: mdt // t, times))
        if nxt >= n:
            mxt = mdt
        else:
            mnt = mdt + 1
    return mnt


cases = [
    ((6, [7, 10]), 28),
    # ((10, [6, 7, 10]), 28),
    # ((10, [1]), 10),
    # ((1000, [1, 10, 100]), 901),
    # ((20, [1, 2, 10]), 13),
]

for (args, ret) in cases:
    print(
        f'{f"solution({args[0]}, {args[1]})":40} : expected `{ret}`, real `{solution(*args)}`')
    # print(f'prev sol({args[0]}, {args[1]}) : expected `{ret}`, real `{prev_sol(*args)}`')
