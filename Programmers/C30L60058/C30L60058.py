# %%
import re


def isvalid(s):
    oo = 0
    oc = 0
    for i, c in enumerate(s):
        if c == '(':
            oo += 1
        else:
            oc += 1
        if oo < oc:
            # invalid
            return False
    return True


def uv(p):
    oc = 0
    cc = 0
    for i, e in enumerate(p):
        if e == '(':
            oc += 1
        else:
            cc += 1
        if oc == cc:
            return p[:i+1], p[i+1:]
    return p, ""


def solution(p):
    mapping = {'(': ')', ')': '('}
    if len(p) == 0:
        return ""
    u, v = uv(p)
    if isvalid(u):
        return u + solution(v)
    return "(" + solution(v) + ")" + re.sub(r'.', lambda m: mapping[m[0]], u[1:-1])

# print(solution("(()())()"))
import timeit
# print(solution("()))((()" * 500)) #  정답 print
print(timeit.timeit(lambda:solution("()))((()" * 500), number=1)) #  걸리는 시간 측정
