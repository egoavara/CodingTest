# %%
solution = lambda weights, head2head : list(map(lambda e: e[0] + 1, sorted(enumerate([((sum(1 for r in h2h if r == 'W') / c) if (c := sum(1 for r in h2h if r != 'N')) != 0 else 0, sum(1 for i, r in enumerate(h2h) if r == 'W' and w < weights[i]), w) for w, h2h in zip(weights, head2head)]), key=lambda e: e[1], reverse=True)))
# %%
def solution(weights, head2head):
    rate = [((sum(1 for r in h2h if r == 'W') / c) if (c := sum(1 for r in h2h if r != 'N')) != 0 else 0, sum(1 for i, r in enumerate(h2h) if r == 'W' and w < weights[i]), w) for w, h2h in zip(weights, head2head)]
    return list(map(lambda e: e[0] + 1, sorted(enumerate(rate), key=lambda e: e[1], reverse=True)))


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))
