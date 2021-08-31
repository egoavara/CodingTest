# %%
import re
import itertools as it


def solution(expression):
    expr = [e for z in it.zip_longest((int(n) for n in re.split(
        r"[+\-*]", expression)), re.findall(r"[+\-*]", expression))for e in z if e is not None]
    TABLE_OP = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
    }

    answer = 0
    for first, second, last in it.permutations(('+', '-', '*'), 3):
        stack = list(expr)
        while first in stack:
            at = stack.index(first)
            stack[at] = TABLE_OP[first](stack[at-1], stack[at+1])
            del stack[at+1], stack[at-1]
        while second in stack:
            at = stack.index(second)
            stack[at] = TABLE_OP[second](stack[at-1], stack[at+1])
            del stack[at+1], stack[at-1]
        while last in stack:
            at = stack.index(last)
            stack[at] = TABLE_OP[last](stack[at-1], stack[at+1])
            del stack[at+1], stack[at-1]
        answer = max(answer, abs(stack[0]))
    return answer


print(solution("100-200*300-500+20"))
