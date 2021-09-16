# %%
import itertools as it

def solution(food_times, k):
    l = len(food_times)
    f = sorted(food_times)
    food_acc = list(it.accumulate(f))
    start = 0
    for i in range(l):
        end = food_acc[i] + (l-(i+1))*f[i]
        if end > k:
            idx = (k - start) % (l-i)
            return [index+1 for index, food in enumerate(food_times) if food >= f[i]][idx]
        start = end
    return -1


# print(f'> {solution([10, 1, 2], 0)}')
# print(f'> {solution([10, 1, 2], 1)}')
# print(f'> {solution([10, 1, 2], 2)}')
# print(f'> {solution([10, 1, 2], 3)}')
# print(f'> {solution([10, 1, 2], 4)}')
# print(f'> {solution([10, 1, 2], 5)}')
# print(f'> {solution([10, 1, 2], 6)}')
# print(f'> {solution([10, 1, 2], 7)}')
print(f'> {solution([10, 1, 3], 8)}')
print(f'> {solution([10, 1, 3], 9)}')
