# %%
import numpy as np
import itertools as it


def solution(places):
    TABLE = {'P': 0, 'O': 1, 'X': 2}

    def check(p):
        print([(x, y) for x, y in it.product(range(5), range(5)) if p[y][x] == 'P'])
        for l in p:
            print(l)
        print()
        for (ax, ay), (bx, by) in it.combinations(((x, y) for x, y in it.product(range(5), range(5)) if p[y][x] == 'P'), 2):
            dist = abs(bx - ax) + abs(by - ay)
            if dist == 2:
                if bx == ax:
                    dist = TABLE[p[(ay + by)//2][ax]]
                elif by == ay:
                    dist = TABLE[p[ay][(ax + bx)//2]]
                else:
                    dist = min(TABLE[p[ay][bx]], TABLE[p[by][ax]])
            print(ax, ay, ":", bx, by, "=", dist)
            if(dist < 2):
                return 0
        return 1
    return [check(p) for p in places]


print(solution([
    # ["PXXXX", "OPXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],

    # ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    # ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    # ["XPXPX", "PXPXP", "XPXPX", "PXPXP", "XPXPX"],
    # ["XPXPX", "XXPXP", "XPXPX", "PXPXP", "XPXPX"],
]))


# %%
from itertools import combinations
def solution(places):
    answer = []
    for pan in places:
        p_collect = []
        for l in pan:
            print(l)
        for r in range(5):#POOOP
            for c in range(5):
                if pan[r][c] == 'P':
                    p_collect.append((r,c))
        print(p_collect)
        combi = list(combinations(p_collect,2))
        flag = 1
        for i in combi:
            location1 = i[0]
            location2 = i[1]
            distance = calc_distance(location1,location2)
            if distance ==2:
                if location1[0] == location2[0] :
                    c = (location1[1]+location2[1])//2
                    if pan[location1[0]][c] == 'O':
                        answer.append(0)
                        flag = 0
                        break
                elif location1[1] == location2[1] :
                    r = (location1[0] + location2[0]) // 2
                    if pan[r][location1[1]] == 'O':
                        answer.append(0)
                        flag = 0
                        break
                elif pan[location1[0]][location2[1]] == 'O' or pan[location1[1]][location2[0]] == 'O':
                    answer.append(0)
                    flag = 0
                    break
            elif distance < 2:
                answer.append(0)
                flag = 0
                break
        if flag == 1:
            answer.append(1)
    return answer


def calc_distance(location1,location2):
    distance = abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])
    return distance
print(solution([
    ["PXXXX", "XPOXX", "PXXXX", "XXXXX", "XXXXX"],
]))