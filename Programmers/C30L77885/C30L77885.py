# %%
import subprocess
import json

def solution(numbers):
    def f(x):
        if x == 0:
            return 0x1
        for connl in range(64):
            if (x >> connl) & 0x1 != 0x1:
                break
        return (x | (0x1 << connl)) ^ ((0x1) << (connl - 1) if connl > 0 else 0)
    return [f(e) for e in numbers]
print(solution([1000000000000000, 100000000000001]))