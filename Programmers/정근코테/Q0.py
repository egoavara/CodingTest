# %%
def solution(line1, line2):
    counter = 0
    for i in range(len(line1)-len(line2)+1):
        if line1[i] == line2[0]:
            for j in range(1, (len(line1) - i - len(line2)) // (len(line2) - 2)):
                print(j)
                if all((line1[i + k * j] == line2[k] for k in range(1, len(line2)))):
                    counter += 1
            # j = 1
            # while i + j * (len(line2) - 1) < len(line1):
            #     if all((line1[i + k * j] == line2[k] for k in range(1, len(line2)))):
            #         counter +=1
            #     j += 1

    return counter


print(solution("abbbcbbb", "bbb"))
print(solution("abcabcabc", "abc"))
print(solution("abacaba", "acb"))

# %%


def solution(row, column, swipes):
    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def rloc(ox, oy, dx, dy, w, h): return (
        oy + dy % h) * column + (ox + dx % w)

    answer = []
    mat = [i+1 for i in range(row * column)]
    swp = [e for e in mat]
    for sw in swipes:
        dx, dy = dxdy[sw[0] - 1]
        py, px = (sw[1] - 1, sw[2] - 1)
        stride = (sw[4] - sw[2] + 1) if dx != 0 else (sw[3] - sw[1] + 1)
        w, h = sw[4] - sw[2] + 1, sw[3] - sw[1] + 1
        sz = w * h
        for i in range(sz):
            relx, rely = (i % stride, i //
                          stride) if dx != 0 else (i // stride, i % stride)
            ploc = rloc(px, py, relx, rely, w, h)
            nloc = rloc(px, py, relx + dx, rely + dy,  w, h)
            swp[nloc] = mat[ploc]
        #
        lx, ly = ((dx + 1) // 2) * (w-1), ((dy + 1) // 2) * (h-1)
        lw, lh = w if dx == 0 else 1, h if dy == 0 else 1
        res = 0
        for dx in range(lw):
            for dy in range(lh):
                res += mat[rloc(px, py, lx + dx, ly+dy, w, h)]
        answer.append(res)
        #
        mat = [e for e in swp]
    return answer


print(solution(4, 3, [[1, 1, 2, 4, 3], [3, 2, 1, 2, 3],
      [4, 1, 1, 4, 3], [2, 2, 1, 3, 3]]))

print(solution(2, 4, [[3, 1, 2, 2, 4], [3, 1, 2, 2, 4],
      [4, 2, 1, 2, 3], [1, 1, 1, 2, 3]]))

print(solution(2, 2, [[3, 1, 1, 1, 2], [1,1,2,2,2], [4,2,1,2,2], [2,1,1,2,1]]))
