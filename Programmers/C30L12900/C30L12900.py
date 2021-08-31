# %%
import itertools as it


def solution(n):
    if n <= 1 :
        return n
    a, b = 1, 2
    for _ in range(0, n - 1):
        c = a + b % 1000000007
        a = b
        b = c
    return a  % 1000000007

def allow(n):
    num1 = 1
    num2 = 2
    for i in range(0, n - 1):
        num2 = num1 + num2
        num1 = num2 - num1
    return num1 % 1000000007
for i in range(1, 100):
    print(solution(i), allow(i))
# solution(7)
