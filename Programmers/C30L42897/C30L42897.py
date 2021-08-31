# %%
import functools as ft
import timeit


def solution(money):
    @ft.lru_cache(maxsize=None)
    def calc0(start):
        if start > len(money) - 2:
            return 0
        if start == len(money) - 2:
            return money[start]
        return max(money[cur] + calc0(cur + 2) for cur in range(len(money) - 2, start-1, -1))

    @ft.lru_cache(maxsize=None)
    def calc1(start):
        if start > len(money) - 1:
            return 0
        if start == len(money) - 1:
            return money[start]
        return max(money[cur] + calc1(cur + 2) for cur in range(len(money) - 1, start-1, -1))
    return max(
        money[0] + calc0(2),
        calc1(1)
    )


# def solution2(money):
#     c0 = [(2, money[0])]
#     l0 = len(money) - 1
#     c1 = [(1, money[1])]
#     l1 = len(money) - 1
#     return max(
#         money[0] + calc0(2),
#         calc1(1)
#     )


# print(solution([i for i in range(30000)]))
# print(solution([i for i in range(10000)]))
# print(solution([i for i in range(9000)]))
# print(solution([i for i in range(8000)]))
# print(solution([i for i in range(7000)]))
# print(solution([i for i in range(6000)]))
# print(timeit.timeit(lambda: solution([i for i in range(3000)]), number=1))
# print(timeit.timeit(lambda: solution([i for i in range(6000)]), number=1))
# print(solution([i for i in range(5000)]))
# print(solution([i for i in range(3000)]))
# print(solution([i for i in range(2000)]))
# print(solution([i for i in range(1000)]))
print(solution([
    123, 230, 312, 125, 123, 127, 129
]))

# %% 첫번째 시도


def solution(money):
    @ft.lru_cache(maxsize=None)
    def calc(start, end):
        if start > end:
            return 0
        if start == end:
            return money[start]
        db = []
        for cur in range(start, end + 1):
            v = calc(cur + 2, (end - 1) if cur == 0 else end)
            db.append(money[cur] + v)
        return max(db)
    for i in range(1, len(money)-1):
        calc(len(money)-1 - i, len(money)-1)
    return calc(0, len(money)-1)

# 방법은 맞으나 크기가 커지면 recursive overflow 발생
