# %%
import itertools as it


def solution(relation):
    n = len(relation[0])
    used = set()
    for r in range(1, n + 1):
        for keys in it.combinations(range(n), r):
            if any((
                k in used 
                for scnt in range(1, len(keys))
                for k in it.combinations(keys, scnt)
            )):
                continue
            tps = {tuple(tp[k] for k in keys) for tp in relation}
            if len(tps) == len(relation):
                used.add(keys)
    return len(used)


# print(solution([
#     ["100", "ryan", "music", "2"],
#     ["200", "apeach", "math", "2"],
#     ["300", "tube", "computer", "3"],
#     ["400", "con", "computer", "4"],
#     ["500", "muzi", "music", "3"],
#     ["600", "apeach", "music", "2"]
# ]))

print(solution([
    ["a", "1", "4"],
    ["2", "1", "5"],
    ["a", "2", "4"],
]))

# solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']])