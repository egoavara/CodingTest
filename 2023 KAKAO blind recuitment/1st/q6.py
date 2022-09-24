# %%

# def solution(n, m, x, y, r, c, k):
#     queue = [(x, y, "")]
#     while len(queue) > 0:
#         [cx, cy, way] = queue.pop(0)
#         if (cx <= 0 or cx > n or cy <= 0 or cy > m):
#             continue
#         if(len(way) == k):
#             if(cx == r and cy == c):
#                 return way
#         else:
#             queue.append((cx + 1, cy, way + "d"))
#             queue.append((cx, cy - 1, way + "l"))
#             queue.append((cx, cy + 1, way + "r"))
#             queue.append((cx - 1, cy, way + "u"))
#     return "impossible"

import sys
sys.setrecursionlimit(2500)
# %%


def solution(n, m, x, y, r, c, k):
    def dfs(cx, cy, way):
        if (cx <= 0 or cx > n or cy <= 0 or cy > m):
            return None
        
        if(len(way) == k):
            if(cx == r and cy == c):
                return way
            return None
        #
        dx = abs(cx - r)
        dy = abs(cy - c)
        if((dx + dy) > (k - len(way))):
            return None
        #
        if (case := dfs(cx + 1, cy, way + "d")) != None:
            return case
        if (case := dfs(cx, cy - 1, way + "l")) != None:
            return case
        if (case := dfs(cx, cy + 1, way + "r")) != None:
            return case
        if (case := dfs(cx - 1, cy, way + "u")) != None:
            return case
        return None
    return v if (v := dfs(x, y, "")) != None else "impossible"


print(solution(50, 50, 3, 3, 3, 3, 2500))
# d l r u

# du
# lr
# rl
# ud
