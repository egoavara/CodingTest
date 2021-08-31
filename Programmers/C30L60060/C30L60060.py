# %%
import json
import itertools as it
import functools as ft


def wtree(words):
    wt = dict()
    rwt = dict()
    for w in words:
        if len(w) not in wt:
            wt[len(w)] = {'CNT': 0}
        if len(w) not in rwt:
            rwt[len(w)] = {'CNT': 0}
        curr = wt[len(w)]
        curr['CNT'] += 1
        rcurr = rwt[len(w)]
        rcurr['CNT'] += 1
        for c in w:
            if c not in curr:
                curr[c] = {'CNT': 0}
            curr = curr[c]
            curr['CNT'] += 1
        for c in reversed(w):
            if c not in rcurr:
                rcurr[c] = {'CNT': 0}
            rcurr = rcurr[c]
            rcurr['CNT'] += 1
    return wt, rwt


def wt_findall(wt, rwt, q):
    if q[0] == '?':
        return (ft.reduce(lambda acc, c: acc[c] if c in acc else {'CNT': 0}, reversed(q[q.rindex('?') + 1:]), rwt[len(q)])['CNT']) \
            if len(q) in rwt else 0
    else:
        return (ft.reduce(lambda acc, c: acc[c] if c in acc else {'CNT': 0}, q[:q.index('?')], wt[len(q)])['CNT']) \
            if len(q) in wt else 0


def solution(words, queries):
    wt, rwt = wtree(words)
    return [
        wt_findall(wt, rwt, q)
        for q in queries
    ]


print(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao", "a"],
    ["fro??", "????o", "fr???", "fro???", "pro?", "???st"]
))
