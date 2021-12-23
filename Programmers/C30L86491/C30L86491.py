# %%
import math
def solution(sizes):
    cx, cy = math.inf, math.inf
    for x, y in sizes:
        nw, nh = cx > x, cy > y
        nwh = nw and nh
        rw, rh = cy > x, cx > y
        rwh = rw and rh
        if nwh or rwh:
            continue
    return answer
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))