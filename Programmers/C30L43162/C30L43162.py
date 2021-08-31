# %%
import itertools as it


def solution(n, computers):
    disjointset = [i for i in range(n)]

    def find(sets, a):
        if sets[a] != a:
            sets[a] = find(sets, sets[a])
        return sets[a]

    def union(sets, a, b):
        sa = find(sets, a)
        sb = find(sets, b)
        sets[sa] = sb

    for a, b in it.combinations(range(n), 2):
        if computers[a][b] == 1:
            union(disjointset, a, b)
    return len({find(disjointset, i) for i in range(n)})


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# print(solution(5, [
#     [1, 1, 0, 1, 0],
#     [1, 1, 0, 1, 0],
#     [0, 0, 1, 1, 0],
#     [1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 1],
# ]))
print(solution(5, [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]))
# print(solution(5, [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
# ]))
# print(solution(5, [
#     [1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
# ]))

# %%
