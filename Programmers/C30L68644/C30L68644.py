# %%
import itertools as it
def solution(numbers):
    return sorted(set(map(lambda ab : ab[0] + ab[1], it.combinations(numbers, 2))))


print(solution([2, 1, 3, 4, 1]))
