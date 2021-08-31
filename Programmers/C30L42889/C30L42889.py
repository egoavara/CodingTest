# %%
import itertools as it


def solution(N, stages):
    reached = [0 for _ in range(N)]
    for s in stages:
        if s - 1 < N:
            reached[s - 1] += 1
    return list(map(
        lambda e: e[0] + 1,
        sorted(
            enumerate(
                map(
                    lambda e: e[0] / e[1] if e[1] != 0 else 0,
                    zip(
                        reached,
                        it.accumulate(
                            it.chain([len(stages)], reached[:-1]),
                            lambda acc, e: acc - e,
                        ),
                    )
                )
            ),
            key=lambda ea: ea[1],
            reverse= True
        )
    ))


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
