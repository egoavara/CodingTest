# %%
import timeit
import itertools as it


def solution(arr):
    # [(first, sum, las), ...]
    arr = [int(v) if v.isnumeric() else v for v in arr]
    stack = [[None, 0, 0]]
    for e in arr:
        if e == '-':
            stack.append([None, 0, 0])
            pass
        elif e == '+':
            pass
        else:
            if stack[-1][0] is None:
                stack[-1][0] = e
            stack[-1][1] += e
            stack[-1][2] = e
    print(stack)
    return 0


# 3 5 + 1 - 8 -
print(solution(["1", "-", "3", "+", "5", "-", "8"]))
# timeit.timeit(lambda : solution(["1", "-", "3", "+", "5", "-", "8", "-", "3", "+", "5", "-", "8", "-", "3", "+", "5", "-", "8"]), number=1)
