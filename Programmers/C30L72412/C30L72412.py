# %%
import re


def solution(info, query):
    table = {
        'langs': {'-': set(), 'cpp': set(), 'java': set(), 'python': set()},
        'sides': {'-': set(), 'backend': set(), 'frontend': set()},
        'cureers': {'-': set(), 'junior': set(), 'senior': set()},
        'favors': {'-': set(), 'chicken': set(), 'pizza': set()},
        'scores': {}
    }
    for i, v in enumerate(info):
        spt = v.split(" ")
        lang, side, cureer, favor, score = spt[0], spt[1], spt[2], spt[3], int(
            spt[4])
        table['langs'][lang].add(i)
        table['langs']['-'].add(i)
        table['sides'][side].add(i)
        table['sides']['-'].add(i)
        table['cureers'][cureer].add(i)
        table['cureers']['-'].add(i)
        table['favors'][favor].add(i)
        table['favors']['-'].add(i)
        table['scores'][i] = score

    query = [(((spt := re.split(r'(?: and | )', l))[0], spt[1], spt[2], spt[3], spt[4] if spt[4] == '-' else int(spt
                                                                                                                 [4])))
             for l in query]
    return [
        sum(1 for _ in filter(
            lambda i: q[4] == '-' or q[4] <= table['scores'][i],
            table['langs'][q[0]] & table['sides'][q[1]] & table['cureers'][q[2]] & table['favors'][q[3]]))
        for q in query
    ]


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
))
