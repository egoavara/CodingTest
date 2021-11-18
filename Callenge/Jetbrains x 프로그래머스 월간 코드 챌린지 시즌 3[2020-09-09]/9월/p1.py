# %%
def solution(grid):

    table = {
        'S': lambda dx, dy: (dx, dy),
        'R': lambda dx, dy: (-dy, dx),
        'L': lambda dx, dy: (dy, -dx),
    }
    rows = len(grid)
    cols = len(grid[0])

    def __mv(cx, cy, dx, dy):
        nx = (cx + dx) % cols
        ny = (cy + dy) % rows
        return nx, ny

    avs = set()
    for y in range(rows):
        for x in range(cols):
            avs.add(((x, y), (-1, 0)))
            avs.add(((x, y), (1, 0)))
            avs.add(((x, y), (0, -1)))
            avs.add(((x, y), (0, 1)))
    answer = []
    while avs:
        (startx, starty), (sdx, sdy) = avs.pop()
        print((startx, starty), (sdx, sdy))
        currx, curry = __mv(startx, starty, sdx, sdy)
        dx, dy = table[grid[curry][currx]](sdx, sdy)
        l = 1
        while not (startx == currx and starty == curry and sdx == dx and sdy == dy):
            print(l, ":", (currx, curry), (dx, dy))
            avs.remove(((currx, curry), (dx, dy)))
            currx, curry = __mv(currx, curry, dx, dy)
            (dx, dy) = table[grid[curry][currx]](dx, dy)
            l += 1
        answer.append(l)

    return answer


print(solution(["S"]))
print(solution(["R", "R"]))
print(solution(["SL","LR"]))
# print( -1 % 3)
