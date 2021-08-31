# %%
import functools as ft
import itertools as it
import math

# BFS
# def solution(strs, t):
#     words = [(w, 1) for w in strs]
#     q = [(0, t)]
#     while q:
#         d, tmp = q.pop(0)
#         if len(tmp) == 0:
#             return d
#         for w, v in words:
#             if tmp.startswith(w):
#                 q.append((d + v, tmp[len(w):]))
#     return -1

# 
# 어캐풀엇누
def solution(strs, t):
    n = len(t)
    memo = [float("inf")] * (n + 1)
    memo[0] = 0
    sizes = set(len(s) for s in strs)
    strs = set(strs)
    for i in range(n + 1):
        for size in sizes:
            if i + size < n + 1 and t[i:i + size] in strs:
                memo[i + size] = min(memo[i + size], memo[i] + 1)
    return memo[n] if memo[n] < float("inf") else -1

print(solution(["ba", "na", "n", "a"], "banana"))
# print(solution(["ba", "na", "n", "a"], "ana"))
# print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))
# print(solution(["ba", "an", "nan", "ban", "n"], "banana"))
# print(solution(["ba", "an", "nan", "ban", "n"], "xv"))
