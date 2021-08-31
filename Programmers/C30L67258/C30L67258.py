# %%
import functools as ft
import itertools as it


def solution(gems):
    sgems = set(gems)
    start, end = 0, 0
    curr = dict()
    mem = [1, len(gems)]
    while start <= end:
        if len(curr) >= len(sgems):
            mem = min(mem, [start + 1, end], key=lambda e: (e[1] - e[0], e[0]))
            if curr[gems[start]] == 1:
                del curr[gems[start]]
            else:
                curr[gems[start]] -= 1
            start += 1
        else:
            if end >= len(gems):
                break
            if gems[end] in curr:
                curr[gems[end]] += 1
            else:
                curr[gems[end]] = 1
            end += 1
    return mem


# print(solution(["DIA", "RUBY", "RUBY", "DIA",
#       "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# print(solution(["A", "B", "C", "D", "E", "A", "B", "X", "C", "D",]))
# print(solution(["A","A","A","B","B"]))
# print(solution(["A"]))
# print(solution(["A","B","B","B","B","B","B","C","B","A"]))
# print(solution(["A","B","B","B","A","B","C","B","B","C"]))
# print(solution(["A","B","B","B","A","B","C","B","B","C","A","B","C","B","C"]))
# print(solution(["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"] ))
# print(solution(["A", "A", "B"]))
# print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))
# print(solution(["A","A","A","B","B","C","B","B","A","B","C","A","A","A","A","B","B","C","B","B"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
