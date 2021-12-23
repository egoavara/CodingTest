# %%
import itertools as it


def intersection_point(A, B):
    aA, bA, cA = A
    aB, bB, cB = B
    under = aA * bB - bA * aB
    if under == 0:
        return None
    return (
        int((bA * cB - cA * bB) / under),
        int((cA * aB - aA * cB) / under),
    )


def is_line_point(L, P):
    a, b, c = L
    x, y = P
    return (a * x + b * y + c) == 0


def solution(line):
    points = [point for a, b in it.combinations(line, 2) if
              (point := intersection_point(a, b)) and is_line_point(a, point) and is_line_point(b, point)]
    minx = min(map(lambda e: e[0], points))
    maxx = max(map(lambda e: e[0], points))
    miny = min(map(lambda e: e[1], points))
    maxy = max(map(lambda e: e[1], points))
    width = maxx - minx + 1
    height = maxy - miny + 1

    answer = [['.' for _ in range(width)] for _ in range(height)]
    for x, y in points:
        answer[y - miny][x - minx] = "*"
        
    return ["".join(line) for line in reversed(answer)]


for l in solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]):
    print(f'"{l}"')
